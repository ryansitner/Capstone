"""
--- Main Application File (main.py) ---
This file is the main entry point for the text adventure game.
It imports all necessary classes, defines the game's static data,
contains the MainGame orchestrator class, and runs the game.
"""

# --- IMPORTS (Connecting the files) ---
from player import Player
from game_map import GameMap
# ----------------------------------------

# --- GLOBAL DATA (To be replaced by MongoDB in Enhancement 3) ---
# Cleaned and consolidated map data
rooms_dict = {
    'Great Hall': {'South': 'Bedroom', 'West': 'Armory', 'North': 'Apothecary', 'item': 'Stew'},
    'Bedroom': {'West': 'Closet', 'North': 'Great Hall', 'item': None},
    'Closet': {'East': 'Bedroom', 'item': 'Robes'},
    'Armory': {'East': 'Great Hall', 'North': 'Magic Sanctum', 'item': 'Shield'},
    'Magic Sanctum': {'South': 'Armory', 'East': 'Apothecary', 'item': 'Cloak'},
    'Apothecary': {'West': 'Magic Sanctum', 'South': 'Great Hall', 'item': 'Potion', 'East': 'Mage Tower'},
    'Mage Tower': {'West': 'Apothecary', 'South': 'Arcane Dungeon', 'item': 'Staff'},
    'Arcane Dungeon': {'North': 'Mage Tower', 'item': None}
}

# Command output messages (Separating UI text from logic)
COMMAND_MESSAGES = {
    'SUCCESS': "You've retrieved the {} and added it to your inventory!",
    'ALREADY_HAVE': "You already have the {}!",
    'WRONG_ITEM': "There is an item you need in here, its not {}...\nNOTE: All items will be a single word.",
    'NO_ITEM': "There is no item in this room for you to pick up.",
    'INVALID_MOVE': "There isn't a door to the {} from here. Please choose a valid direction.",
    'UNRECOGNIZED': "Sorry the command you entered was unrecognized. Type 'help' for commands.",
    'WINNER': """~""" * 90 + """
As you breach the Arcane Dungeon, a wave of stifling heat and flame washes over you.
Your magical robes flare with protective wards, turning the inferno aside as you press
forward. Looming in the shadows, five pairs of menacing eyes—glowing green, red, blue,
purple, and white—fix upon you. The light of your staff pierces the gloom, revealing the 
colossal heads of the hydra as they uncoil from the darkness, surrounding you. 
A sharp crackle heralds the first attack.

A torrent of lightning erupts from one of the hydra's maws. With arcane reflexes, you
raise your shield, bracing as the raw energy slams into it. The impact vibrates up your arm,
you feel the electricity surging through you, empowering you. With a quick incantation, the
shield's runes illuminate, hurling the lightning back at its source. Before the smoke even
clears, the hydra readies a second assault.

Suddenly, jagged spears of ice rain from the gaping maw of the blue head. You invoke your cloak of
levitation, soaring above the deadly volley. As you rise, you come face-to-face with the green hydra
head. Caught off guard, a noxious, thick cloud of poison engulfs you. Your lungs burn, vision vanishing
as a massive claw tears through the gas, striking you from the air.

You crash to the ground, the poison searing your lungs. Gasping, you see the central head inhale, focusing a
devastating hyperbeam. With the last of your strength, you raise to your feet and slam the butt of your staff
into the ground, erecting a shimmering wall of crystal. The immense energy released from the hydra lances past,
shaking the dungeon to its foundations. In these fleeting, precious moments, you consume the restorative stew
and potent mana potion, feeling vitality and magic surge back into you. The hyperbeam sends cracks through your
crystal defense as the other heads join, blasting the wall with fire, frost, lightning, and acid.

Fractures spiderweb across the crystal. You channel your will into the crown of your staff, its gems whirling into a
blinding nimbus as immense power surges within you. The wall explodes into infinite tiny shards. You raise your hand,
and the world around you falls silent. With a flick of you hand, you siphon the elemental fury, drawing the chaotic
energies of the hydra's assault into your own form. Muttering an ancient incantation, you focus the stolen power into
your staff... and unleash it all with a final, deafening blast. As the dust settles, the hydra lies collapsed, its
many heads still. With the beast subdued, you channel your remaining magic, forcing it back into its chamber and renewing
the ancient runes, repairing the seal.

CONGRATULATIONS! You have saved the city and won the game!
""" + """~""" * 90,

    'LOSER': """~""" * 90 + """
As you step into the Arcane Dungeon you are hit with a wave of immense heat and flames.
The fire starts to burn your skin as you try to push forward. Looming in the dark you see
five sets of eyes, glowing shades of green, red, blue, purple, and white. Before you know
what's going on your are blasted with beams of lightning, fire, frost, and acid.
Everything goes dark. You have been defeated, the hydra has escaped the mage's guild
and leveled the city, killing thousands.
GAME OVER
""" + """~""" * 90,
}

# Directions constant
DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']


class MainGame:
    """
    The main game orchestrator. It manages the game loop, handles user I/O,
    and checks the win/loss conditions.
    """
    REQUIRED_ITEMS = ['Cloak', 'Potion', 'Robes', 'Shield', 'Staff', 'Stew']

    def __init__(self, room_data):
        # Initialize Map Manager to create all Room objects
        self.game_map = GameMap(room_data)

        # Get the starting room object
        start_room = self.game_map.get_room(self.game_map.start_room_name)

        # Initialize Player, giving them the starting Room object
        self.player = Player(start_room)

        # Control flag for the game loop
        self.is_running = True

    def _display_game_state(self, message=None):
        """Prints the current room description, inventory, and a status message."""
        # Separator and Room Info
        print("-" * 87)
        # Display room name and description
        # TODO: Remove first print line before after testing
        print(f"You are currently in the {self.player.current_room.name}.")
        print(self.player.current_room.get_description())

        # Inventory:
        # Sorts the inventory list before displaying
        inventory_list = sorted(self.player.inventory)
        print(f"Inventory: {inventory_list}")

    def _display_message(self, message):
        """Prints only a status message, used for errors or action feedback."""
        print(f"\n{message}")

    def _process_input(self, user_input):
        """Parses and executes player commands, then displays feedback."""

        # Check for empty string
        if not user_input:
            self._display_message(COMMAND_MESSAGES['UNRECOGNIZED'])
            return

        command = user_input[0].upper()

        # Handle Movement (GO)
        if command == 'GO':
            if len(user_input) < 2:
                self._display_message("GO what direction?")
                return

            direction = user_input[1].upper()

            # Check for valid direction
            if direction not in DIRECTIONS:
                # If the direction isn't one of the 4 valid words,
                # display an error and stop processing.
                self._display_message(f"'{direction}' is not a valid direction. Try NORTH, SOUTH, EAST, or WEST.")
                return

            # The Player object attempts the move, using the GameMap for lookups
            success = self.player.move(direction, self.game_map)

            if not success:
                # Display message if move fails (e.g., direction is invalid)
                self._display_message(COMMAND_MESSAGES['INVALID_MOVE'].format(direction))
            else:
                # If successful, the full game state (new room) is displayed later
                pass

        # Handle Item Collection (GET)
        elif command == 'GET':
            if len(user_input) < 2:
                self._display_message("GET what item?")
                return

            item_name = user_input[1].title()

            # The player object handles all the logic and returns a status code
            status = self.player.collect_item(item_name)

            # Translate status code into the UI message
            if status == 'SUCCESS':
                self._display_message(COMMAND_MESSAGES['SUCCESS'].format(item_name))
            elif status == 'ALREADY_HAVE':
                self._display_message(COMMAND_MESSAGES['ALREADY_HAVE'].format(item_name))
            elif status == 'WRONG_ITEM':
                # Custom message to reflect the item the player tried to grab
                self._display_message(COMMAND_MESSAGES['WRONG_ITEM'].format(item_name))
            elif status == 'NO_ITEM':
                self._display_message(COMMAND_MESSAGES['NO_ITEM'])

        # Handle Utility Commands
        elif command == 'HELP':
            self._display_message(
                "COMMANDS: GO [Direction], GET [Item], EXIT.\n"
                "GOAL: Collect all 6 items before entering the Arcane Dungeon."
            )

        elif command == 'EXIT':
            # Set the control flag to stop the game loop
            self.is_running = False

        # Handle Unrecognized Commands
        else:
            self._display_message(COMMAND_MESSAGES['UNRECOGNIZED'])

    def _check_win_loss(self):
        """Checks if the player has entered the Arcane Dungeon and determines win/loss state."""

        # Check if player entered the boss room
        if self.player.current_room.name == 'Arcane Dungeon':
            # Check Win Condition (inventory vs required items)
            player_items_sorted = sorted(self.player.inventory)

            if player_items_sorted == self.REQUIRED_ITEMS:
                # Win outcome: Display the success narrative and end the game
                self._display_message(COMMAND_MESSAGES['WINNER'])
            else:
                # Loss outcome: Display the failure narrative and end the game
                self._display_message(COMMAND_MESSAGES['LOSER'])

            # Stop the game regardless of win or loss
            self.is_running = False

            # Block 3: Return success status
            return True # Indicates that the check was performed (game is over)

        return False # Indicates that the game is still running (boss room not entered)

    def run_game(self):
        """
        The main game loop. Handles initialization, input, and state updates.
        Replaces the complex procedural loop from the original file.
        """

        # Game Introduction and Initial Display
        print("~" * 87)
        print("| You are one of the head mages of the Wizard Guild in the City of the Radiant Izar.  |")
        print("| A hydra has broken out of its magical restraints and threatens to destroy the city. |")
        print("| You must gather your 6 supplies and subdue the Hydra in the tower's Arcane Dungeon. |")
        print("|                                                                                     |")
        print("| NOTE: All items will be a single word.                                              |")
        print("| WARNING: Do not try to face the hydra until you have gathered all your supplies!    |")
        print("~" * 87)

        self._display_game_state()

        # The Main Execution Loop
        while self.is_running:
            try:
                # Get user input
                user_input_raw = input("What would you like to do?\n> ").strip()
                user_input = user_input_raw.split()

                # Process the command (move, get, exit, help, error)
                self._process_input(user_input)

                # Check for game termination conditions after processing input
                self._check_win_loss()

                # Display state if game is still running
                if self.is_running:
                    # After a move, the state needs re-displayed. After GET, _process_input handles messaging.
                    # We just call it to ensure display updates if the player successfully moved.
                    self._display_game_state()

            except EOFError:
                # Handles Ctrl+D or other termination signals cleanly
                self.is_running = False
            except Exception as e:
                # General error handling message
                self._display_message(f"An unexpected error occurred: {e}")

        # Game End Message
        print("\nThanks for playing, goodbye.")


if __name__ == '__main__':
    """
    This is the main entry point of the application.
    It initializes the MainGame orchestrator by passing in the
    globally defined rooms_dict and then calls run_game()
    to start the application loop.
    """

    # Initialize and run the game
    # 'rooms_dict' is the global constant defined at the top of this file.
    game = MainGame(rooms_dict)
    game.run_game()