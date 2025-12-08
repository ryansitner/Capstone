"""
This script is responsible for creating the MongoDB database and
populating it with the initial room and item data.
Run this script ONCE to set up the database.
"""

import pymongo
import config


def seed_database():
    """
    Connects to MongoDB, clears any existing 'text_adventure_db',
    and inserts the room data documents.
    """
    try:
        # Connect to MongoDB using the URI from config.py
        client = pymongo.MongoClient(config.MONGO_URI)

        # Drop the database if it exists to ensure a clean slate
        client.drop_database(config.DB_NAME)
        print(f"Cleared existing '{config.DB_NAME}'.")

        # Create/Access the database and collection
        db = client[config.DB_NAME]
        rooms_collection = db["rooms"]

        # Define the Room Data
        rooms_data = [
            {
                "name": "Bedroom",
                "desc_with_item": (
                    "The bedroom seems warm and cozy.\n"
                    "Your bed is neatly made and you have a small fire\n"
                    "going in the fireplace."
                ),
                "desc_no_item": (
                    "The bedroom seems warm and cozy.\n"
                    "Your bed is neatly made and you have a small fire\n"
                    "going in the fireplace."
                ),
                "item": None,
                "image_path": "images/bedroom.png"
            },
            {
                "name": "Great Hall",
                "desc_with_item": (
                    "The Great Hall is vast and a bit chilly as you\n"
                    "feel the cold wind flow across the large vacant\n"
                    "room. You smell it before you see it. On one of the tables, you\n"
                    "see a delicious bowl of hearty stew. You're not sure who\n"
                    "prepared it, but who are you to question free food?"
                ),
                "desc_no_item": (
                    "The Great Hall is vast and a bit chilly as you\n"
                    "feel the cold wind flow across the large vacant\n"
                    "room. Nothing in here seems to catch your eye."
                ),
                "item": "Stew",
                "image_path": "images/great_hall.png"
            },
            {
                "name": "Closet",
                "desc_with_item": (
                    "The walk-in closet is a small, snug room,filled with various clothes.\n"
                    "Sitting nicely on the mannequin are your magical robes.\n"
                    "There is no other door than the one you entered."
                ),
                "desc_no_item": (
                    "The walk-in closet is a small, snug room,filled with various clothes.\n"
                    "You see the bare mannequin where your robes used to be.\n"
                    "There is no other door than the one you entered."
                ),
                "item": "Robes",
                "image_path": "images/closet.png"
            },
            {
                "name": "Armory",
                "desc_with_item": (
                    "As you walk into the armory, you see most of the shelves are stocked\n"
                    "with different miscellaneous staves, shortswords, and scepters.\n"
                    "Mounted on the wall you see one of the Mage Guild's relics:\n"
                    "the Shield of Reflection. You feel a magical aura pulsating from it."
                ),
                "desc_no_item": (
                    "As you walk into the armory, you see most of the shelves are still\n"
                    "stocked with different miscellaneous staves, shortswords, and scepters.\n"
                    "You see the now empty area on the wall, void of dust, from\n"
                    "where the shield was once mounted."
                ),
                "item": "Shield",
                "image_path": "images/armory.png"
            },
            {
                "name": "Magic Sanctum",
                "desc_with_item": (
                    "As you walk into the Magic Sanctum, you can feel the energy\n"
                    "radiating in the air. As you look around, rows of books, scrolls,\n"
                    "and tomes plaster the walls. You notice up against one of the walls,\n"
                    "a display case holding a familiar item you're attuned to: the Cloak of Levitation."
                ),
                "desc_no_item": (
                    "As you walk into the Magic Sanctum, you can feel the energy\n"
                    "radiating in the air. As you look around, rows of books, scrolls,\n"
                    "and tomes plaster the walls. You see against the wall, the empty\n"
                    "display case that was once holding the Cloak of Levitation."
                ),
                "item": "Cloak",
                "image_path": "images/sanctum.png"
            },
            {
                "name": "Apothecary",
                "desc_with_item": (
                    "As you walk into the apothecary, your nostrils are assaulted by\n"
                    "different herbs, animal parts, and other miscellaneous reagents.\n"
                    "As you refocus your mind, you see a mana potion sealed and sitting on\n"
                    "the table."
                ),
                "desc_no_item": (
                    "You try to brace yourself but your nostrils are once again assaulted by\n"
                    "different herbs, animal parts, and other miscellaneous reagents.\n"
                    "The table that once held a mana potion is now empty omitting a few\n"
                    "bits and bobbles."
                ),
                "item": "Potion",
                "image_path": "images/apothecary.png"
            },
            {
                "name": "Mage Tower",
                "desc_with_item": (
                    "Within the Mage Tower and you see your arcane desk. It's covered\n"
                    "with different trinkets and books. Leaning against the desk you\n"
                    "see your tried and true, trusted weapon. Your mage staff pulsates\n"
                    "with power."
                ),
                "desc_no_item": (
                    "You enter the Mage Tower and you see your arcane desk.\n"
                    "It's covered with different trinkets and books."
                ),
                "item": "Staff",
                "image_path": "images/tower.png"
            },
            {
                "name": "Arcane Dungeon",
                "desc_with_item": (
                    "You enter the Arcane Dungeon. You can hear the sounds of the elemental hydra waiting for you."
                ),
                "desc_no_item": (
                    "You enter the Arcane Dungeon. You can hear the sounds of the elemental hydra waiting for you."
                ),
                "item": None,
                "image_path": "images/dungeon.png"
            }
        ]

        # Insert data into MongoDB
        result = rooms_collection.insert_many(rooms_data)
        print(f"Successfully inserted {len(result.inserted_ids)} room documents into '{config.DB_NAME}'.")

        # Create a unique index on the "name" field.
        # This ensures fast lookups and prevents duplicate room names.
        rooms_collection.create_index("name", unique=True)
        print("Created unique index on 'rooms.name'.")

        client.close()

    except Exception as e:
        print(f"An error occurred while seeding the database: {e}")


if __name__ == "__main__":
    seed_database()