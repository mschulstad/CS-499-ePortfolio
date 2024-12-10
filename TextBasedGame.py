#Michael Schulstad

#A dictionary for the simplified text game

#The dictionary links a room to other rooms.
rooms = {
        'Main Hub': {'North': 'Med Bay', 'East': 'Main Terminal', 'South': 'Sleeping Quarters', 'West': 'Gym'},
        'Main Terminal': {'North': 'Med Bathroom', 'South': 'Engine Room', 'West': 'Main Hub'},
        'Engine Room': {'North': 'Main Terminal', 'West': 'Sleeping Quarters', 'tool': 'Toolbox'},
        'Med Bathroom': {'South': 'Main Terminal', 'West': 'Med Bay', 'villian': 'Ghost'},
        'Med Bay': {'East': 'Med Bathroom', 'South': 'Main Hub', 'West': 'Storage', 'tool': 'Space Suit'},
        'Sleeping Quarters': {'North': 'Main Hub', 'East': 'Engine Room', 'South': 'Bathroom', 'West': 'Dining Room',
                              'tool': 'Helmet'},
        'Bathroom': {'North': 'Sleeping Quarters', 'villian': 'Ghost'},
        'Dining Room': {'North': 'Gym', 'East': 'Sleeping Quarters', 'tool': 'Pliers'},
        'Gym': {'North': 'Storage', 'East': 'Main Hub', 'South': 'Dining Room', 'tool': 'Hammer'},
        'Storage': {'East': 'Med Bay', 'South': 'Gym', 'tool': 'Oxygen Tank'}
    }
# initialize player inventory
backpack = []
# Initialize the starting room
current_room = 'Main Hub'

def move(direction):
    # check for valid direction to move and update current room
    global current_room

    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print('You cant move in that direction')

def obtain_item():
    # check dictionary for tool in room and ask player if they want to collect if tool is in current room
    if 'tool' in rooms[current_room]:
        tool = rooms[current_room]['tool']
        print('There is a', tool)
        while True:
            collect = input('Do you want to collect the tool? (yes/no) ').lower()
            if collect == 'yes':
                backpack.append(tool)
                del rooms[current_room]['tool']
                print(backpack)
                print('You have obtained', tool)
                break
            elif collect == 'no':
                break
            else:
                print('Invalid response. Please enter "yes" or "no".')
    else:
        print('There is no tool in this room')

def check_win_lose():
    # if player enters room with villian they lose
    if 'villian' in rooms[current_room]:
        print('You lose: You ran into the ghost')
        print('Thank you for playing')
        return 'lose'
    # if player collects all 6 items they win
    if len(backpack) == 6:
        print('You win: you gathered all the tools')
        print('Thank you for playing')
        return 'win'

    return 'continue'

def show_instructions():
   #print a main menu and the commands
   print("Welcome to the Ghost Text Adventure Game")
   print("Collect all 6 items before encountering the Ghost.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: collect item")

show_instructions()
while True:
    print('You are in the ', current_room)
    print(rooms[current_room])

    user_input = input('Enter a command: ')
    words = user_input.split()

    if 'exit' in words:
        while True:
            exit_input = input('Do you wish to exit? (yes/no) ').lower()
            if exit_input == 'yes':
                break
            elif exit_input == 'no':
                break
            else:
                print('Invalid response. Please enter "yes" or "no".')
        if exit_input == 'yes':
            break
        else:
            continue

    if len(words) < 2:
        print('Invalid command')
        continue

    first = words[0]

    command = words[1]
    command = command.capitalize()

    if 'Go' in first.capitalize():
        print('Direction:', command)
        move(command)

    obtain_item()

    check_result = check_win_lose()
    if check_result == 'lose' or check_result == 'win':
        break






