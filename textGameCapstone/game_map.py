"""
Manages all Room objects and the static map structure.
"""

import random
from room import Room
from database_manager import DatabaseManager

class GameMap:
    def __init__(self):
        """
        Initializes the GameMap by loading and instantiating all Room objects.
        """
        self.rooms = {}
        self.start_room_name = 'Bedroom'

        self.db = DatabaseManager() # Initialize Database Manager

        self.generate_map()  # Calls method to create random dungeon layout

    def generate_map(self):
        """
        Generates a new random map using a modified Prim's Algorithm.
        This method creates all room objects, hardcodes the Bedroom/Closet
        link, and then randomly connects the rest, ensuring all item
        rooms are reachable without *having* to go through the Arcane Dungeon room (which ends the game).
        """

        # --- Create all Room objects from Database ---

        # List of room names to fetch from the DB
        target_rooms = [
            'Bedroom', 'Great Hall', 'Closet', 'Armory',
            'Magic Sanctum', 'Apothecary', 'Mage Tower', 'Arcane Dungeon'
        ]

        for name in target_rooms:
            # Query the database for this room's data
            room_data = self.db.get_room_data(name)

            if room_data:
                # Extract data from the MongoDB document
                desc_with_item = room_data['desc_with_item']
                desc_no_item = room_data['desc_no_item']
                item_name = room_data['item']

                # Create the Room object (exits are empty for now)
                self.rooms[name] = Room(
                    name=name,
                    desc_with_item=desc_with_item,
                    desc_no_item=desc_no_item,
                    exits={},
                    item_name=item_name
                )
            else:
                print(f"ERROR: Could not load room '{name}' from database.")


        # ----- Apply Generation Rules & Prep Algorithm -----

        # Hardcode the link between Bedroom and Closet
        self.rooms['Bedroom'].exits['WEST'] = 'Closet'
        self.rooms['Closet'].exits['EAST'] = 'Bedroom'

        # Prep for Prim's Algorithm
        # The "Forest" (rooms already connected) starts with our required rooms.
        forest = {'Bedroom', 'Closet'}

        # The "Wall" (potential connections) starts with all rooms *except*
        # the ones already in the forest and the boss room.
        unconnected_rooms = [
            'Great Hall', 'Armory', 'Magic Sanctum',
            'Apothecary', 'Mage Tower'
        ]

        # Shuffle the list to ensure a random map layout
        random.shuffle(unconnected_rooms)


        # ----- Connect all 5 item rooms to the forest -----

        # Helper map for finding the opposite direction
        opposite_direction = {
            'NORTH': 'SOUTH',
            'SOUTH': 'NORTH',
            'EAST': 'WEST',
            'WEST': 'EAST'
        }

        # All possible directions to try
        all_directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

        # Loop through each unconnected room and attach it to the 'forest'
        for room_name in unconnected_rooms:

            # Get the Room object for the new room we are adding
            new_room = self.rooms[room_name]

            # Find a valid connection point
            connected = False
            while not connected:

                # Get a list of all rooms we can build from.
                # This is all rooms in the forest *except* the 'Closet'.
                # (This was a personal choice not to have a second room branching from the closet)
                valid_anchor_rooms = [room_name for room_name in forest if room_name != 'Closet']

                # Pick a random room from the valid list to connect to
                current_forest_room_name = random.choice(valid_anchor_rooms)
                current_forest_room = self.rooms[current_forest_room_name]

                # Pick a random direction to try and build a door
                random.shuffle(all_directions)
                for direction in all_directions:
                    # Check if the potential exit is already taken
                    if direction not in current_forest_room.exits:
                        # --- Valid Exit Found ---
                        # Add exit from the forest room to the new room
                        current_forest_room.exits[direction] = new_room.name

                        # Add the opposite exit from the new room back to the forest
                        opposite = opposite_direction[direction]
                        new_room.exits[opposite] = current_forest_room.name

                        # Add the new room to the forest so it can be built upon
                        forest.add(new_room.name)

                        # Mark as connected and break the inner loops
                        connected = True
                        break

                # If we failed (e.g., picked a forest room with 4 full exits),
                # the 'while not connected' loop will try again with a new random forest room.


        # ----- Connect the Boss Room ('Arcane Dungeon') -----

        boss_room = self.rooms['Arcane Dungeon']
        connected = False
        while not connected:
            # Get a list of all rooms we can build from (all rooms excluding closet)
            valid_anchor_rooms = [r_name for r_name in forest if r_name != 'Closet']

            # Pick a random valid room to connect the boss room to
            anchor_room_name = random.choice(valid_anchor_rooms)
            anchor_room = self.rooms[anchor_room_name]

            # Pick a random direction
            random.shuffle(all_directions)
            for direction in all_directions:
                # Check if the exit is free
                if direction not in anchor_room.exits:
                    # --- Valid Exit Found ---
                    # Add exit from the anchor room to the boss room
                    anchor_room.exits[direction] = boss_room.name

                    # Add the opposite exit from the boss room back
                    opposite = opposite_direction[direction]
                    boss_room.exits[opposite] = anchor_room.name

                    # Add boss room to the forest
                    forest.add(boss_room.name)
                    connected = True
                    break

            # If we fail, the loop repeats until it finds a free slot.


        # ----- Add Extra Random Loops -----

        # To make the map more interesting, we add a few extra doors (loops).
        num_extra_loops = 3
        for _ in range(num_extra_loops):

            # Pick two random, different rooms from the forest excluding closet
            valid_rooms = [r_name for r_name in self.rooms.keys() if r_name != 'Closet']

            room1_name = random.choice(valid_rooms)
            room2_name = random.choice(valid_rooms)

            # Ensure we didn't pick the same room twice
            if room1_name == room2_name:
                continue  # Skip this attempt

            room1 = self.rooms[room1_name]
            room2 = self.rooms[room2_name]

            # Check if they are already connected
            already_connected = False
            for exit_name in room1.exits.values(): # Key = Direction | Value = Room Name
                if exit_name == room2.name:
                    already_connected = True
                    break

            if already_connected:
                continue  # Skip this attempt

            # Find a free exit slot to connect them
            random.shuffle(all_directions)
            for direction in all_directions:
                if direction not in room1.exits:
                    # Found an available exit space on room1
                    opposite = opposite_direction[direction]

                    if opposite not in room2.exits:
                        # Found opposite available exit space on room2 as well

                        # Create the loop
                        room1.exits[direction] = room2.name
                        room2.exits[opposite] = room1.name
                        break  # Done with this loop attempt


        # ----- BFS Validation -----

        # Validate the map to ensure all 6 item rooms are reachable
        # from the start without *having* to passing through the 'Arcane Dungeon'.

        # List of all rooms we must be able to reach.
        required_rooms = {
            'Bedroom', 'Closet', 'Great Hall', 'Armory',
            'Magic Sanctum', 'Apothecary', 'Mage Tower'
        }

        # Start BFS
        queue = [self.rooms['Bedroom']]  # Start the queue with the starting room
        visited = {'Bedroom'}  # Keep track of visited rooms

        while queue:
            current_room = queue.pop(0)  # Get the next room to check

            # Look at all its neighbors
            for exit_name in current_room.exits.values():

                # IMPORTANT: If the neighbor is the boss room,
                # do NOT add it to the queue. This prevents the
                # search from "crossing" the boss room.
                if exit_name == 'Arcane Dungeon':
                    continue

                if exit_name not in visited:
                    visited.add(exit_name)
                    queue.append(self.rooms[exit_name])

        # After the BFS is done, check if we visited all required rooms
        if not required_rooms.issubset(visited):
            # The validation FAILED.
            # We must scrap this map and generate a new one.
            # We do this by simply calling the method again (recursion).
            self.generate_map()

    def load_map_from_save(self, map_data):
        """
        Reconstructs the map from saved data.
        Overrides the current map state with the data from the save file.

        Args:
            map_data (list): A list of dictionaries, where each dictionary
                             contains the data for one room (exits, items, etc.).
        """
        # Clear the existing map
        self.rooms = {}

        # Iterate through the saved data
        for room_dict in map_data:
            name = room_dict['name']

            # Recreate the Room object using the saved state
            new_room = Room(
                name=name,
                desc_with_item=room_dict['desc_with_item'],
                desc_no_item=room_dict['desc_no_item'],
                exits=room_dict['exits'],  # Restore the specific connections
                item_name=room_dict['item_name']  # Restore the item (or None if taken)
            )

            # Store it in the map
            self.rooms[name] = new_room

        print("Map layout and state restored from save file.")

    def get_room(self, name):
        """
        Retrieves a Room object by its name.
        This is the method called by Player.move() in its line 3.
        """
        return self.rooms.get(name)
