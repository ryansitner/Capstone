"""
Represents the player avatar in the game.
Manages the player's current location and inventory.
"""

from room import Room

class Player:
    def __init__(self, start_room: Room, name="Hero"):
        """ Initializes the player """
        self.name = name  # (str, optional): The player's name. Defaults to "Hero".
        self.current_room = start_room  # (Room) holds a reference to a Room object (the player's location)
        self.inventory = []  # inventory starts as a list (will be changed to a Set in Week 2)

    def collect_item(self, item_name):
        """
        Attempts to collect the item from the current room.

        Args:
            item_name (str): The item name provided by the player ('Get <item>').

        Returns:
            str: A status code indicating the result: 'SUCCESS', 'ALREADY_HAVE',
                 'WRONG_ITEM', or 'NO_ITEM'.
        """
        # Check if the player already has the item they are trying to get (redundancy check)
        if item_name in self.inventory:
            return 'ALREADY_HAVE'

        # Check if the room has the item the player is trying to get AND if the name matches.
        if self.current_room.check_item_name(item_name):

            # If valid, retrieve the item (which removes it from the Room state).
            item_to_collect = self.current_room.get_item_name()

            # Add the item to the player's inventory
            self.inventory.append(item_to_collect)
            self.inventory.sort()
            return 'SUCCESS'  # Item collected successfully

        # If the name didn't match, check if there's an item in the room.
        elif self.current_room.has_item:
            # The room has an item, but the player typed the wrong name (e.g., 'Get Broom' when 'Staff' is present)
            return 'WRONG_ITEM'

        # If the room doesn't have an item, or it was already collected via a previous failed attempt.
        return 'NO_ITEM'

    def move(self, direction, game_map_manager):
        """
        Attempts to move the player in the given direction.

        Args:
            direction (str): The direction of movement (e.g., 'North').
            game_map_manager (GameMap): A reference to the central map manager
                                        to look up the new room object.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        # Check if the exit is valid from the current room
        if self.current_room.is_exit_valid(direction):
            # Get the name of the destination room
            destination_room_name = self.current_room.exits[direction]

            # Use the GameMap manager to get the actual Room object for the destination
            new_room_object = game_map_manager.get_room(destination_room_name)

            # Update the player's location reference
            self.current_room = new_room_object
            return True

        return False  # Move failed
