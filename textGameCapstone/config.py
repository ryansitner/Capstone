"""
This file loads environment variables from the .env file.
It provides a central place to access configuration settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")