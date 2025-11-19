#Module Seven Text Based Gamer - Ryan Sitner

def bedroom_description():
    print('You are in the bedroom, it seems warm and cozy.')
    print('You see a door to the North, and a door to the West.')
    print('-' * 30)
    return ''

def greathall_description():
    if rooms_dict[current_room]['item'] in inventory: # description 1) if room item is already in inventory
        print('You have entered the Great Hall. It\'s a bit chilly\n'
          'as you feel the cold wind flow across the large vacant\n'
          'room. You see doors on the Southern, Western, and Northern\n'
          'ends of the room.')
    else: # description 2) if the room item hasn't been picked up yet
        print('You have entered the Great Hall. It\'s a bit chilly\n'
              'as you feel the cold wind flow across the large vacant\n'
              'room. You see doors on the Southern, Western, and Northern\n'
              'ends of the room.')
        print('You smell it before you see it. On one of the tables, you\n'
              'see a delicious bowl of meat stew. You\'re not sure who\n'
              'prepared it, but who are you to question free food?')
    print('-' * 30)
    return ''

def closet_description():
    if rooms_dict[current_room]['item'] in inventory: # description 1) if room item is already in inventory
        print('You have entered the closet. It\'s a small, snug room,\n'
          'filled with various clothes.')
        print('You see the naked mannequin where your robes used to be.\n'
              'There is no other door than the one you entered.\n'
              'The door to the East, heading back to the bedroom.')
    else: # description 2) if the room item hasn't been picked up yet
        print('You have entered the closet. It\'s a small, snug room,\n'
              'filled with various clothes.')
        print('Sitting nicely on the mannequin are your magical robes.\n'
              'There is no other door than the one you entered.\n'
              'The door to the East, heading back to the bedroom.')
    print('-' * 30)
    return ''

def armory_description():
    if rooms_dict[current_room]['item'] in inventory: # description 1) if room item is already in inventory
        print('You walk into the armory, you see a door to the North\n'
              'and a door to the East. Most of the shelves are stocked\n'
              'with different miscellaneous swords, spears, and halberds.\n'
              'You see an area on the wall void of dust from where the\n'
              'the shield was once mounted.')
    else: # description 2) if the room item hasn't been picked up yet
        print('You walk into the armory, you see a door to the North\n'
              'and a door to the East. Most of the shelves are stocked\n'
              'with different miscellaneous swords, spears, and halberds.\n'
              'Mounted on the wall you see one of the Mage Guild\'s relics:\n'
              'the Shield of Reflection. You feel a magical aura pulsating from it.')
    print('-' * 30)
    return ''

def sanctum_description():
    if rooms_dict[current_room]['item'] in inventory:  # description 1) if room item is already in inventory
        print('As you walk into the Magic Sanctum, you can feel the energy\n'
              'radiating from the floor. There are doors to the East and South.\n'
              'As you look around, rows of books, scrolls, and tomes plaster the walls.\n'
              'You see against the wall, the empty display case that was once\n'
              'holding the Cloak of Levitation.')
    else: # description 2) if the room item hasn't been picked up yet
        print('As you walk into the Magic Sanctum, you can feel the energy\n'
              'radiating from the floor. There are doors to the East and South.\n'
              'As you look around, rows of books, scrolls, and tomes plaster the walls.\n'
              'You notice up against one of the walls, a display case holding\n'
              'a familiar item you\'re attuned to: the Cloak of Levitation.')
    print('-' * 30)
    return ''

def apothecary_description():
    if rooms_dict[current_room]['item'] in inventory:  # description 1) if room item is already in inventory
        print('You try to brace yourself but your nostrils are once again assaulted by\n'
              'different herbs, animal parts, and other miscellaneous ingredients.\n'
              'The table that once held a mana potion is now empty omitting a few\n'
              'odds and ends. There are doors to the East, South, and West of the room.')
    else: # description 2) if the room item hasn't been picked up yet
        print('As you walk into the apothecary, your nostrils are assaulted by\n'
              'different herbs, animal parts, and other miscellaneous ingredients.\n'
              'As you refocus your mind, you see a mana potion sealed and sitting on\n'
              'the table. There are doors to the East, South, and West of the room.')
    print('-' * 30)
    return ''

def magetower_description():
    if rooms_dict[current_room]['item'] in inventory:  # description 1) if room item is already in inventory
        print('You enter the Mage Tower and you see your arcane desk.\n'
              'It\'s covered with different trinkets and bobbles.\n'
              'There are doors to the South and West.')
    else: # description 2) if the room item hasn't been picked up yet
        print('You enter the Mage Tower and you see your arcane desk. It\'s covered\n'
              'with different trinkets and bobbles. Leaning against the desk you\n'
              'see your tried and true trusted weapon, your mage staff pulsates\n'
              'with power. There are doors to the South and West.')
    print('-' * 30)
    return ''

def arcanedungeon_description():
    inventory.sort()
    if inventory == ['Cloak', 'Potion', 'Robes', 'Shield', 'Staff', 'Stew']: # winner outcome
        print('~' * 90)
        print('As you step into the Arcane Dungeon, you are hit with a wave of immense heat and flames.\n'
              'Your magical robes are able to protect you from burning up, and you push forward.\n'
              'Looming in the dark you see five sets of eyes, glowing shades of green, red, blue,\n'
              'purple, and white. As the light from your staff illuminates around you, the heads of \n'
              'the hydra loom out of the darkness, they seem to almost surround you on three sides.\n'
              'You hear crackling as one of the heads prepares to attack!\n\n'
              'You see a beam of lightning shoot out of one of the hydra\'s mouths. With your\n'
              'quick reflexes you raise your shield and brace for impact. As the lightning hits\n'
              'your shield, you feel the vibration and a small charge of electricity run through your hands.\n'
              'With a quick incantation, you activate the shields ability - blasting the lightning back at\n'
              'the hydra. As you look over your shield the hydra readies a second attack.\n\n'
              'Suddenly, giant 8ft spikes of ice rain to the ground from the hyrda\'s gaping maw, you use\n'
              'your cloak of levitation to fly above. As you rise to the eye level of the hydra, you\'re\n'
              'caught off guard and are quickly surrounded by a thick cloud of poisonous gas. Unable to see\n'
              'around you, and as your lungs fill with poison, you are struck by one of the hydra\'s massive claws.\n\n'
              'The force of the blow knocks you to the ground. As you try to cough the poison out of your lungs\n'
              'you see the main head of the hydra prepare its devistating hyperbeam attack. With the last of your\n'
              'strength you slam your staff to the ground, errecting a wall of crystal to protect you.\n'
              'The emense energy errupts on either side of the wall and shakes the ground beneath you.\n'
              'With this moment of protection you quickly consume the stew and mana potion to regain your health and magic.\n'
              'As the hydra\'s hyperbeam continues to berate your crystal wall, the other heads join in, blasting the wall\n'
              'with fire, frost, lightning, and acid.\n\n'
              'You see the crystal wall begin to crack as you quickly run your hand over the crown of your staff,\n'
              'causing the gems to glow brightly and spin tightly around the top of the staff. You feel immense energy\n'
              'flow into you. As the crystal wall shatters around you, you hold up your hand, seemingly freezing everything\n'
              'in place. With a swift flick of your hand, you absorb all of the energy from the hydra\'s attack. Once more\n'
              'running your hand over the crown of your staff and muttering an ancient spell, you blast the hydra with all\n'
              'your might. As the smoke settles, you see the hydra on the ground unconcious. With the hydra subdued you are\n'
              'able to send it back into it\'s chamber and restore the runes, repairing the seal.\n\n'
              'CONGRATULATIONS! You have saved they city and won the game!')
        print('~' * 90)
    else: # loser outcome
        print('~' * 90)
        print('As you step into the Arcane Dungeon you are hit with a wave of immense heat and flames.\n'
              'The fire starts to burn your skin as you try to push forward. Looming in the dark you see\n'
              'five sets of eyes, glowing shades of green, red, blue, purple, and white. Before you know\n'
              'what\'s going on your are blasted with beams of lightning, fire, frost, and acid.\n'
              'Everything goes dark. You have been defeated, the hydra has escaped the wizard tower\n'
              'and leveled the city, killing countless civilians.\n'
              'GAME OVER')
        print('~' * 90)
    return ''

def instructions():
    print('-' * 30)
    print('To move between rooms, enter the word \'Go\' followed by a direction:\n'
          '(North, East, South, West)\n'
          'Enter the word \'Get\' followed by an object to pick up items you find.\n'
          '(ie: Get Potion)\n'
          'Or type \'Exit\' to exit the game.')
    print('-' * 30)
    return ''

def introduction(): # general game into to the plot and goal of the game
    print('You are one of the head mages of the wizard tower in the City of the Radiant Citadel.\n'
          'An alarm has been triggered, alerting you that a magical barrier in the Arcane Dungeon\n'
          'has been dispelled. The barrier was containing an elemental hydra who is going on a rampage\n'
          'and is currently trying to escape the dungeon.\n'
          'You must gather your supplies (6 items), head to the dungeon, subdue the hydra, and re-seal the magical barrier.\n\n'
          'WARNING: What ever you do, do not face the hydra until you have gathered your supplies.\n'
          'You will NOT survive without them. Good luck!')
    return ''

def error_message(): # message displayed if user input is invalid
    print("Sorry the command you entered was unrecognized.")
    print('Either type \'Go\' followed by a direction (ie \'Go West\'),\n'
          'type \'Get\' followed by an item (ie \'Get Potion\' to pick it up.\n'
          'Type \'help\' to view game instructions, or type \'exit\' to exit the game.')
    print('-' * 30)
    return ''

# list of rooms and how they connect, main item in rooms, and misc. items in rooms
# misc items are added in case player tries to pick up an item that exists in room description, but isn't the collectible item
rooms_dict = {
        'Great Hall': {'South':'Bedroom', 'West':'Armory', 'North':'Apothecary', 'item':'Stew', 'desc':greathall_description,
                       'misc':{}},
        'Bedroom': {'West':'Closet', 'North':'Great Hall', 'desc':bedroom_description, 'item':{},'misc':{}},
        'Closet': {'East':'Bedroom', 'item':'Robes', 'desc':closet_description, 'misc':'Mannequin'},
        'Armory': {'East':'Great Hall', 'North':'Magic Sanctum', 'item':'Shield', 'desc':armory_description,
                   'misc':{'Sword', 'Spear', 'Halberd', 'Swords', 'Spears', 'Halberds'}},
        'Magic Sanctum': {'South':'Armory', 'East':'Apothecary', 'item':'Cloak', 'desc':sanctum_description,
                          'misc':{'Book', 'Scroll', 'Tome', 'Books', 'Scrolls', 'Tombs'}},
        'Apothecary': {'West':'Magic Sanctum', 'South':'Great Hall', 'item':'Potion', 'East':'Mage Tower', 'desc':apothecary_description,
                       'misc':{'Herb', 'Skull', 'Ingredient', 'Herbs', 'Skulls', 'Ingredients'}},
        'Mage Tower': {'West':'Apothecary', 'South':'Arcane Dungeon', 'item':'Staff', 'desc':magetower_description,
                       'misc':{'Trinket', 'Bobble', 'Tinkets', 'Bobbles'}},
        'Arcane Dungeon': {'North':'Mage Tower', 'desc':arcanedungeon_description} # villian room
}

directions = ['North', 'East', 'West', 'South']
inventory = []

# function for moving between rooms
def player_movement(dir_input, room):
    direction = dir_input
    if direction in rooms_dict[room]: # check to see if the direction entered is valid for the current room player is in
        x = rooms_dict[room][dir_input] # change current room to newly entered room
        return x
    else:
        print('There isn\'t a door to the {}. Please choose a valid direction.'.format(direction)) # invalid direction entered by player
        return current_room

# function to obtain items
def get_item (item_input, current_inv):
    x = current_inv
    if item_input == rooms_dict[current_room]['item']: # verify item player is trying to get exists in the current room
        if item_input in x: # making sure player doesn't already have that item
            print('You already have the {}'.format(item_input))
            return inventory
        else: # adding item to player's inventory
            x.append(rooms_dict[current_room]['item'])
            print('You\'ve retrieved the {}!'.format(rooms_dict[current_room]['item']))
            return x
    elif item_input in rooms_dict[current_room]['misc']: # item exists within room description, but isn't the main item to obtain
        if item_input.endswith('s'):
            print('You have no need for any {}'.format(item_input.lower()))
        else:
            print('You have no need for a {}.'.format(item_input.lower()))
        return inventory
    else: #item does not exist
        print('There is no {} in the {}'.format(item_input.lower(), current_room))
        print('HINT: Items should be a single word.\n'
              'For example, instead of \'Get Mana Potion\' try \'Get Potion\'')
        return inventory

# Main function
if __name__ == '__main__':
    current_room = 'Bedroom' #declare starting room
    introduction()
    instructions()
    print('You are currently in the {}.\n'
          'It feels warm and cozy.\n'
          'You see a door to the North, and a door to the West.\n'
          'What would you like to do?'.format(current_room))
    user_input = input().title().split()  #inclued formatting 'title' to prevent any caplitalization issues

# main gaming loop
    while not user_input or user_input[0] != 'Exit':

        if not user_input: # player hits Enter with no input
            error_message()
        # calling funtion to move between rooms
        elif user_input[0] == 'Go' and user_input[1] in directions and len(user_input) == 2:
            current_room = player_movement(user_input[1], current_room)
            if not inventory: # inventory printing as None, when empty, this is a workaround to prevent that
                print('Inventory: [ ]')
            else:
                print('Inventory: {}'.format(inventory))
            print(rooms_dict[current_room]['desc']()) # display description of the room player is in
        # calling funtion to retrieve items
        elif user_input[0] == 'Get':
            if len(user_input) >= 2:
                inventory = get_item(user_input[1], inventory)
                inventory.sort()
                if not inventory:
                    print('Inventory: [ ]') # inventory printing as None, when empty, this is a workaround to prevent that
                else:
                    print('Inventory: {}'.format(inventory))
            else:
                print('What are you trying to get?')
        elif user_input[0] == 'Help':
            instructions()
            print(rooms_dict[current_room]['desc']())
        else:
            error_message()


        if current_room == 'Arcane Dungeon':
            user_input = 'Exit'.split() # win or lose, the game is over once player enters the dungeon, set input to exit command
        else:
            user_input = input("What would you like to do?\n").title().split()

    print('Thanks for playing, goodbye.')