"""
This file handles all interactions with the MongoDB database.
It manages the connection, retrieves room data, and handles
saving/loading player progress.
"""

import pymongo
import sys

class DatabaseManager:
    """
    A class to manage the MongoDB connection and operations.
    """

    def __init__(self, db_name="text_adventure_db"):
        """
        Initializes the connection to the local MongoDB instance.

        Args:
            db_name (str): The name of the database to connect to.
                           Defaults to 'text_adventure_db'.
        """
        self.client = None
        self.db = None

        try:
            # Connect to the local MongoDB server
            # 27017 is the default port
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")

            # Access the specific database
            # If it doesn't exist, MongoDB creates it automatically when we add data.
            self.db = self.client[db_name]

            print(f"Connected to database: {db_name}")

        except pymongo.errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")
            sys.exit(1)  # Exit the game if we can't connect to the DB

    def close_connection(self):
        """Closes the connection to the database."""
        if self.client:
            self.client.close()
            print("Database connection closed.")

    def get_room_data(self, room_name):
        """
        Retrieves the document for a specific room from the 'rooms' collection.

        Args:
            room_name (str): The name of the room to find (e.g., 'Great Hall').

        Returns:
            dict: The room data document, or None if not found or error.
        """
        if self.db is not None:
            try:
                rooms_collection = self.db["rooms"]

                # Query the database: Find the document where "name" matches room_name
                # find_one returns a single dictionary (or None)
                data = rooms_collection.find_one({"name": room_name})
                return data

            except pymongo.errors.PyMongoError as e:
                print(f"Error retrieving room data: {e}")
        return None

    def save_game_state(self, player, game_map):
        """
        Saves the ENTIRE game state (Player + Map Layout) to the 'saves' collection.

        Args:
            player (Player): The player object containing inventory and location.
            game_map (GameMap): The map object containing all Room objects and their dynamic exits.
        """
        if self.db is not None:
            try:
                saves_collection = self.db["saves"]
                save_id = "player_1_save"

                # --- Serialize the Map Data ---
                # Save the state of every room because the exits are random
                # and items might have been picked up.
                map_data = []
                for room_name, room_obj in game_map.rooms.items():
                    room_state = {
                        "name": room_obj.name,
                        "exits": room_obj.exits,  # Save the dynamic exits
                        "item_name": room_obj.item_name,  # Save if item is still there (or None)
                        "has_item": room_obj.has_item,  # Save the boolean flag
                        "desc_with_item": room_obj.desc_with_item,  # Persist descriptions
                        "desc_no_item": room_obj.desc_no_item
                    }
                    map_data.append(room_state)

                # Prepare the Save Document
                save_document = {
                    "save_id": save_id,
                    "player": {
                        "current_room": player.current_room.name,  # Save name, not object
                        "inventory": list(player.inventory)  # Convert Set to List
                    },
                    "map_data": map_data,  # The full list of room states
                }

                # Upsert the save
                saves_collection.update_one(
                    {"save_id": save_id},
                    {"$set": save_document},
                    upsert=True
                )
                print("Game saved successfully.")
                return True

            except pymongo.errors.PyMongoError as e:
                print(f"Error saving game: {e}")
        return False

    def load_game_state(self):
        """
        Retrieves the saved game state document.
        """
        if self.db is not None:
            try:
                saves_collection = self.db["saves"]
                save_id = "player_1_save"
                return saves_collection.find_one({"save_id": save_id})
            except pymongo.errors.PyMongoError as e:
                print(f"Error loading game: {e}")
        return None

    def save_exists(self):
        """Checks if a save file currently exists."""
        return self.load_game_state() is not None

    def delete_save(self):
        """
        Deletes the current save file.
        Used when starting a new game to ensure a clean state.
        """
        if self.db is not None:
            try:
                saves_collection = self.db["saves"]
                save_id = "player_1_save"

                # Delete the document with the matching ID
                result = saves_collection.delete_one({"save_id": save_id})

                if result.deleted_count > 0:
                    print("Previous save file deleted.")
                    return True
                else:
                    print("No save file found to delete.")
                    return False

            except pymongo.errors.PyMongoError as e:
                print(f"Error deleting save: {e}")
        return False