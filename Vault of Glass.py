#A dictionary for Vault of Glass text-based dungeon game.
#The dictionary links a room to other rooms.
rooms = {
        'Ishtar Sink, Venus': {'Down': 'The Spire'},
        'The Spire': {'Left': 'Trial of Kabr', 'Right': 'The Confluxes', 'Down': 'Templar\'s Well', 'Item': 'Chest Armor'},
        'Trial of Kabr': {'Right': 'The Spire', 'Item': 'None'},
        'The Confluxes': {'Left': 'The Spire', 'Down': 'Hall of Oracles', 'Item': 'Leg Armor'},
        'Hall of Oracles': {'Left': 'Templar\'s Well', 'Down': 'The Gate', 'Up': 'The Confluxes', 'Item': 'Fatebringer'},
        'The Gate': {'Left': 'Gorgon\'s Labyrinth', 'Up': 'Hall of Oracles','Item': 'Gauntlets'},
        'Gorgon\'s Labyrinth': {'Up': 'Templar\'s Well', 'Left': 'The Disappearing Platforms', 'Right': 'The Gate'},
        'Templar\'s Well': {'Left': 'The Glass Throne', 'Up': 'The Spire', 'Right': 'Hall of Oracles', 'Down': 'Gorgon\'s Labyrinth','Item': 'Cloak'},
        'The Disappearing Platforms': {'Up': 'The Glass Throne', 'Right': 'Gorgon\'s Labyrinth', 'Item': 'Vex Mythoclast'},
        'The Glass Throne': {'Item': 'Atheon'}
}

def main():


#Function to display movement commands.
def show_instructions():
    # Show player move commands and explain backstory
    print('Welcome to the Vault of Glass, Guardian!')
    print('Collect the six items left behind by Kabr\'s fireteam.\nThen take down Atheon once and for all before he destroys The Last City.''\nNow head down into the Vault and show them what you are made of.')
    print('\nInstructions:')
    print('Move commands: Go Up, Go Down, Go Left, Go Right, or Exit')

#Function for determining location
def get_new_location(location, direction):
    new_location = location #Declaring new location
    for i in rooms:
        if i == location:
            if direction in rooms[i]:
                new_location = rooms[i][direction]
    return new_location #Loop returns player's new location within the dungeon

# def user_input():
#     pass
#
# def valid_directions():
#     pass


show_instructions() #Call funtion to display intro/movements to player.
Inventory = []
location = 'Ishtar Sink, Venus' #Player starting location. Will always be the first room.

while True: #Loops the main gameplay until player wins, loses, or exits.

    if len(Inventory) != 6 and location == 'The Glass Throne':
        print('The Last City has been lost. The Vex have won.')
        break

    if len(Inventory) == 6 and location == 'The Glass Throne':
        print('Congratulations, Guardian! You have collected all items and stopped Atheon once and for all!')
        break

    print('You have reached', location)
    print('Inventory:', Inventory)

    if "Item" in rooms[location]:
        if not rooms[location]["Item"] in Inventory:
            item = rooms[location]["Item"]
            print('You found', item)
            question = input('Would you like to retrieve item and add it to inventory? (yes/no): ')
            if "yes" in question:
                Inventory.append(item)
                print(item, "has been added to the inventory")

    print('--------------------')


    direction = input('Enter your move: ').lower() #Get player movement input
    if direction == 'go down' or direction == 'go up' or direction == 'go left' or direction == 'go right': #Valid commands to get to each room. Player will be prompted with instructions before starting.
        direction = direction[3:].capitalize()
        new_location = get_new_location(location, direction)
        if new_location == location:
            print('That room is sealed off try another direction!') #Message pops up when location is invalid
        else:
            location = new_location

    elif direction.lower() == 'exit': #If player chooses to exit game will play message and end program
        print('We hope to see you again soon, Guardian!')
        break #Player has chosen to exit. This ends the game.
    else:
        print('Invalid input. Please try again.') #Message to let player know input was incorrect. May want to re-display directions after as well