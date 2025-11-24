"""
Represents a single location in the game fortress.
It holds all static data (descriptions, exits) and controls
item presence within the room.
"""

class Room:
    def __init__(self, name, desc_with_item, desc_no_item, exits, item_name=None):

        """ Initializes a Room object """
        self.name = name  # (str) The unique name of the room
        self.desc_with_item = desc_with_item  # (str) Description to show when item is present
        self.desc_no_item = desc_no_item  # (str) Description to show when item has already been obtained
        self.exits = exits  # (dict) A dictionary mapping directions (ex. 'North') to destination room names
        self.item_name = item_name  # (str, optional): The name of the collectible item in the room. Defaults to None
        self.has_item = item_name is not None  # Boolean flag for quick checking

    def get_description(self):
        """
        Returns the appropriate description based on whether the item
        is still present in the room vs already been collected.
        """
        if self.has_item:
            # If the item is still here, return the full description (with item details)
            return self.desc_with_item
        else:
            # If the item has been collected, return the description without the item.
            return self.desc_no_item

    def is_exit_valid(self, direction):
        """
        Checks if the provided direction is a valid exit from
        the current room.
        """
        # Checks if the input direction (str) is a key in the self.exits dictionary
        return direction in self.exits

    def get_item_name(self):
        """
        Retrieves the item name from the room and removes the item,
        ensuring it can only be collected once.

        Returns:
            str or None: The name of the item if present, otherwise None.
        """
        if self.has_item:
            # Store the item name before clearing the room
            collected_item = self.item_name

            # --- State Change for OOP ---
            self.item_name = None  # Clear the item
            self.has_item = False  # Update the flag
            # ---------------------------

            return collected_item
        return None

    def check_item_name(self, attempted_item):
        """
        Checks if the given item name matches the collectible item in the room,
        but DOES NOT remove the item.

        Args:
            attempted_item (str): The item name provided by the player ('Get <item>').

        Returns:
            bool: True if the item is present and matches the attempted item name.
        """
        return self.has_item and self.item_name == attempted_item
