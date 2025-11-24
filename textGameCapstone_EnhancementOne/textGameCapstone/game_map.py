"""
Manages all Room objects and the static map structure.
For Enhancement 1, it loads data from the static dictionary.
For Enhancement 2, it will implement procedural map generation.
"""

from room import Room

class GameMap:
    def __init__(self, room_data):
        """
        Initializes the GameMap by loading and instantiating all Room objects.

        Args:
            room_data (dict): The original static rooms_dict from the original game.
        """
        self.rooms = {}
        self.start_room_name = 'Bedroom'  # Fixed starting room for now (changing in Enhancement 2)

        self._load_rooms(room_data)  # Call method to process the dictionary and create Room objects

    def _load_rooms(self, room_data):
        """
        Private method to process the dictionary data and instantiate Room objects,
        using the unique description strings from the original game file.

        The descriptions{} dict, is a placeholder to reflect the Description Strings
        from the original textbasedgame.py, these will be altered during Enhancement 2
        and then migrated to the MongoDB in Enhancement 3.
        """
        descriptions = {
            # Bedroom has no collectible item, so desc_with_item == desc_no_item
            'Bedroom': {
                'desc_no_item': (
                    "The bedroom, it seems warm and cozy.\n"
                    "You see a door to the North, and a door to the West."
                ),
            },
            # Great Hall (Item: Stew)
            'Great Hall': {
                'desc_with_item': (
                    "The Great Hall is vast and a bit chilly as you\n"
                    "feel the cold wind flow across the large vacant\n"
                    "room. You see doors on the Southern, Western, and Northern\n"
                    "ends of the room.\n"
                    "You smell it before you see it. On one of the tables, you\n"
                    "see a delicious bowl of hearty stew. You're not sure who\n"
                    "prepared it, but who are you to question free food?"
                ),
                'desc_no_item': (
                    "The Great Hall is vast and a bit chilly as you\n"
                    "feel the cold wind flow across the large vacant\n"
                    "room. You see doors on the Southern, Western, and Northern\n"
                    "ends of the room. Nothing else catches your eye."
                ),
            },
            # Closet (Item: Robes)
            'Closet': {
                'desc_with_item': (
                    "The walk-in closet is a small, snug room,\n"
                    "filled with various clothes.\n"
                    "Sitting nicely on the mannequin are your magical robes.\n"
                    "There is no other door than the one you entered,\n"
                    "the door to the East, heading back to the bedroom."
                ),
                'desc_no_item': (
                    "The walk-in closet is a small, snug room,\n"
                    "filled with various clothes.\n"
                    "You see the bare mannequin where your robes used to be.\n"
                    "There is no other door than the one you entered,\n"
                    "the door to the East, heading back to the bedroom."
                ),
            },
            # Armory (Item: Shield)
            'Armory': {
                'desc_with_item': (
                    "As you walk into the armory, you see a door to the North\n"
                    "and a door to the East. Most of the shelves are stocked\n"
                    "with different miscellaneous staves, shortswords, and scepters.\n"
                    "Mounted on the wall you see one of the Mage Guild's relics:\n"
                    "the Shield of Reflection. You feel a magical aura pulsating from it."
                ),
                'desc_no_item': (
                    "You walk into the armory, you see a door to the North\n"
                    "and a door to the East. Most of the shelves are stocked\n"
                    "with different miscellaneous staves, shortswords, and scepters.\n"
                    "You see the now empty area on the wall, void of dust, from\n"
                    "where the shield was once mounted."
                ),
            },
            # Magic Sanctum (Item: Cloak)
            'Magic Sanctum': {
                'desc_with_item': (
                    "As you walk into the Magic Sanctum, you can feel the energy\n"
                    "radiating in the air. There are doors to the East and South.\n"
                    "As you look around, rows of books, scrolls, and tomes plaster the walls.\n"
                    "You notice up against one of the walls, a display case holding\n"
                    "a familiar item you're attuned to: the Cloak of Levitation."
                ),
                'desc_no_item': (
                    "As you walk into the Magic Sanctum, you can feel the energy\n"
                    "radiating in the air. There are doors to the East and South.\n"
                    "As you look around, rows of books, scrolls, and tomes plaster the walls.\n"
                    "You see against the wall, the empty display case that was once\n"
                    "holding the Cloak of Levitation."
                ),
            },
            # Apothecary (Item: Potion)
            'Apothecary': {
                'desc_with_item': (
                    "As you walk into the apothecary, your nostrils are assaulted by\n"
                    "different herbs, animal parts, and other miscellaneous reagents.\n"
                    "As you refocus your mind, you see a mana potion sealed and sitting on\n"
                    "the table. There are doors to the East, South, and West of the room."
                ),
                'desc_no_item': (
                    "You try to brace yourself but your nostrils are once again assaulted by\n"
                    "different herbs, animal parts, and other miscellaneous reagents.\n"
                    "The table that once held a mana potion is now empty omitting a few\n"
                    "bits and bobbles. There are doors to the East, South, and West of the room."
                ),
            },
            # Mage Tower (Item: Staff)
            'Mage Tower': {
                'desc_with_item': (
                    "Within the Mage Tower and you see your arcane desk. It's covered\n"
                    "with different trinkets and books. Leaning against the desk you\n"
                    "see your tried and true, trusted weapon. Your mage staff pulsates\n"
                    "with power. There are doors to the South and West."
                ),
                'desc_no_item': (
                    "You enter the Mage Tower and you see your arcane desk.\n"
                    "It's covered with different trinkets and books.\n"
                    "There are doors to the South and West."
                ),
            },
            # Arcane Dungeon (Boss Room - No item collected here)
            'Arcane Dungeon': {
                'desc_no_item': (
                    "You enter the Arcane Dungeon. You can hear the sounds of the elemental hydra waiting for you.\n"
                    "There is only a door to the North, leading back to the Mage Tower."
                ),
            },
        }
        # ---------------------------------------------------------------------

        for name, data in room_data.items():
            # Extract Item Name from Rooms Dict
            item_name = data.get('item')

            # Extract Exits (Using the keys in the dictionary that are directions)
            # Filter the dict to only include directional exits:
            exits_data = {key.upper(): value for key, value in data.items() if key in ['North', 'East', 'South', 'West']}

            # Retrieve the correct, full description strings
            if name in descriptions:
                desc_set = descriptions[name]
                # For rooms with no items (such as Bedroom), set desc_with_item to desc_no_item
                desc_with_item = desc_set.get('desc_with_item', desc_set['desc_no_item'])
                desc_no_item = desc_set['desc_no_item']
            else:
                # Should not happen, but a fallback for safety
                desc_with_item = desc_no_item = "ERROR: Room description missing."

            # Object Instantiation: Create the new Room object
            new_room = Room(
                name=name,
                desc_with_item=desc_with_item,
                desc_no_item=desc_no_item,
                exits=exits_data,
                item_name=item_name
            )

            # Storage: Store the Room object
            self.rooms[name] = new_room

    def get_room(self, name):
        """
        Retrieves a Room object by its name.
        This is the method called by Player.move() in its line 3.
        """
        return self.rooms.get(name)
