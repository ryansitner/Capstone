Text Adventure Game Capstone
============================

An enhanced, object-oriented text adventure game featuring procedural map generation, persistent data storage using MongoDB, and a custom command-line interface.

Project Overview
----------------

This project is the culmination of a computer science capstone, enhancing a basic Python script into a full-stack application. It demonstrates mastery in:

*   **Software Design:** Modular OOP architecture.
    
*   **Algorithms:** Randomized Prim's algorithm for dungeon generation and BFS for map validation.
    
*   **Databases:** MongoDB integration for data persistence (Save/Load).


To transparently showcase the iterative evolution of this project, the repository is organized into distinct branches. Each branch corresponds to a specific phase of enhancement, allowing reviewers to examine the code's progression from its initial procedural state to its final modular form. The **main** branch represents the fully integrated, polished application, incorporating all three major enhancements: Software Design, Algorithms, and Databases.
    

Setup and Installation
----------------------

### 1\. Prerequisites

*   Python 3.8+
    
*   MongoDB Community Server (running locally on default port 27017)
    

### 2\. Installation

1.  Clone the repository or extract the project files.
    
2.  Create a virtual environment (optional but recommended).
    
3.  Install required dependencies:

```
pip install pymongo python-dotenv

```
    

### 3\. Configuration (.env)

Create a file named .env in the root directory of the project. Add your MongoDB connection details:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=text_adventure_db

```
_Note: The .env file is excluded from version control for security._

### 4\. Database Seeding

Before running the game for the first time, you must populate the database with the static game data (rooms and items). Run the seeding script:

```
python build_database.py

```

Running the Game
----------------

To start the application, run the main script:

```
python main.py

```

Database Serialization Schema
-----------------------------

The application uses MongoDB to store two types of documents: **Room Data** (static content) and **Save States** (dynamic player data).

### 1\. Room Collection (rooms)

Stores the template data for every room in the game.

```
{
  "_id": "ObjectId('...')",
  "name": "Great Hall",
  "desc_with_item": "String (Description when item is present)",
  "desc_no_item": "String (Description when item is taken)",
  "item": "Stew",  // String name of the item, or null
  "image_path": "images/great_hall.png" // Placeholder for assets
}

```

### 2\. Save Collection (saves)

Stores the serialized state of a specific playthrough, including the procedurally generated map layout.

```
{
  "_id": "ObjectId('...')",
  "save_id": "player_1_save",
  "timestamp": "Date",
  "player": {
    "name": "Hero",
    "current_room": "Armory",
    "inventory": ["Stew", "Sword"] // List converted from Python Set
  },
  "map_data": [
    {
      "name": "Great Hall",
      "exits": {
        "NORTH": "Bedroom",
        "WEST": "Armory"
      },
      "item_name": null, // null indicates item was taken
      "has_item": false,
      "desc_with_item": "...",
      "desc_no_item": "..."
    },
    // ... one entry for every room in the generated map ...
  ]
}

```

# Code Review Video
[![Watch the video](https://img.youtube.com/vi/LoU2TGlupmc/hqdefault.jpg)](https://youtu.be/LoU2TGlupmc)
