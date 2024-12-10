import json
import random

# Class representing a room in the game
class Room:
    def __init__(self, name, exits=None, tool=None):
        """
        Initializes a room with a name, exits, and an optional tool.

        :param name: Name of the room.
        :param exits: Dictionary mapping directions to connected rooms.
        :param tool: The tool present in the room, if any.
        """
        self.name = name
        self.exits = exits if exits else {}  # Directions to connected rooms
        self.tool = tool  # Optional tool in the room

    def has_tool(self):
        """
        Checks if the room contains a tool.

        :return: True if a tool is present, False otherwise.
        """
        return self.tool is not None


# Class representing the overall game
class Game:
    def __init__(self):
        """
        Initializes the game, setting up the rooms, player inventory, and the villain's location.
        """
        # Set up rooms with their connections and tools
        self.rooms = self.create_rooms()

        # Set starting room for the player
        self.current_room = self.rooms['Main Hub']

        # Set random starting room for the villain
        self.villain_room = random.choice(list(self.rooms.values()))

        # Player's inventory
        self.inventory = []

    def create_rooms(self):
        """
        Creates all the rooms in the game and their connections.

        :return: Dictionary mapping room names to Room objects.
        """
        rooms = {
            'Main Hub': Room('Main Hub', {'North': 'Med Bay', 'East': 'Main Terminal', 'South': 'Sleeping Quarters', 'West': 'Gym'}),
            'Main Terminal': Room('Main Terminal', {'North': 'Med Bathroom', 'South': 'Engine Room', 'West': 'Main Hub'}),
            'Engine Room': Room('Engine Room', {'North': 'Main Terminal', 'West': 'Sleeping Quarters'}, tool='Toolbox'),
            'Med Bathroom': Room('Med Bathroom', {'South': 'Main Terminal', 'West': 'Med Bay'}),
            'Med Bay': Room('Med Bay', {'East': 'Med Bathroom', 'South': 'Main Hub', 'West': 'Storage'}, tool='Space Suit'),
            'Sleeping Quarters': Room('Sleeping Quarters', {'North': 'Main Hub', 'East': 'Engine Room', 'South': 'Bathroom', 'West': 'Dining Room'}, tool='Helmet'),
            'Bathroom': Room('Bathroom', {'North': 'Sleeping Quarters'}),
            'Dining Room': Room('Dining Room', {'North': 'Gym', 'East': 'Sleeping Quarters'}, tool='Pliers'),
            'Gym': Room('Gym', {'North': 'Storage', 'East': 'Main Hub', 'South': 'Dining Room'}, tool='Hammer'),
            'Storage': Room('Storage', {'East': 'Med Bay', 'South': 'Gym'}, tool='Oxygen Tank'),
        }
        # Set up connections between rooms
        for room in rooms.values():
            room.exits = {direction: rooms[connected_room] for direction, connected_room in room.exits.items()}
        return rooms

    def move(self, direction):
        """
        Moves the player to a connected room if possible and moves the villain.

        :param direction: Direction to move (e.g., 'North', 'South').
        """
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You moved to the {self.current_room.name}.")
            self.move_villain()  # Move the villain after the player moves
        else:
            print("You can't move in that direction.")

    def move_villain(self):
        """
        Moves the villain to a random connected room.
        """
        if self.villain_room.exits:
            self.villain_room = random.choice(list(self.villain_room.exits.values()))
            print(f"The Ghost has moved to another room!")

    def obtain_item(self):
        """
        Collects a tool from the current room, if available, and adds it to the player's inventory.
        """
        if self.current_room.has_tool():
            print(f"You found a {self.current_room.tool}.")
            self.inventory.append(self.current_room.tool)
            self.current_room.tool = None  # Remove the tool from the room
            print(f"Inventory: {self.inventory}")
        else:
            print("There's no tool in this room.")

    def check_win_lose(self):
        """
        Checks win or lose conditions after each action.

        :return: 'win', 'lose', or 'continue' based on the game's state.
        """
        # Lose condition: Player encounters the villain
        if self.current_room == self.villain_room:
            print("You lose: You ran into the Ghost!")
            print("Thank you for playing.")
            return 'lose'

        # Win condition: Player collects all tools
        if len(self.inventory) == 6:
            print("You win: You gathered all the tools!")
            print("Thank you for playing.")
            return 'win'

        return 'continue'

    def save_game(self):
        """
        Saves the game's current state to a file.
        """
        save_data = {
            'current_room': self.current_room.name,
            'villain_room': self.villain_room.name,
            'inventory': self.inventory
        }
        with open('savegame.json', 'w') as save_file:
            json.dump(save_data, save_file)
        print("Game saved.")

    def load_game(self):
        """
        Loads the game's state from a file.
        """
        try:
            with open('savegame.json', 'r') as save_file:
                save_data = json.load(save_file)
                self.current_room = self.rooms[save_data['current_room']]
                self.villain_room = self.rooms[save_data['villain_room']]
                self.inventory = save_data['inventory']
                print("Game loaded.")
        except FileNotFoundError:
            print("No save file found.")

    def show_instructions(self):
        """
        Displays the game's instructions.
        """
        print("Welcome to the Ghost Text Adventure Game!")
        print("Collect all 6 items before encountering the Ghost.")
        print("Commands: go <direction>, collect item, save, load, exit")

    def start(self):
        """
        Starts the main game loop.
        """
        self.show_instructions()
        while True:
            print(f"\nYou are in the {self.current_room.name}.")
            print("Available exits:", list(self.current_room.exits.keys()))

            # Display tool in the room, if any
            if self.current_room.has_tool():
                print(f"This room has a tool: {self.current_room.tool}")

            # Notify if the villain is in the room
            if self.current_room == self.villain_room:
                print("The Ghost is here! Beware!")

            user_input = input("Enter a command: ").strip().lower()  # Normalize input
            if user_input == "exit":
                break
            elif user_input.startswith("go "):
                direction = user_input[3:].capitalize()  # Match room keys
                self.move(direction)
            elif user_input == "collect item":
                self.obtain_item()
            elif user_input == "save":
                self.save_game()
            elif user_input == "load":
                self.load_game()
            else:
                print("Unknown command. Try 'go <direction>', 'collect item', 'save', or 'load'.")

            # Check win/lose conditions
            result = self.check_win_lose()
            if result in ("win", "lose"):
                break


# Run the game
if __name__ == "__main__":
    game = Game()
    game.start()
