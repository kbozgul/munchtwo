import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



def string_to_float_list(s):
    # Remove the square brackets and split the string by commas
    str_list = s.strip("[]").split(",")
    # Convert each item to an integer and return the list
    return [float(item) for item in str_list if item.strip()]


class munch_plot:
    def __init__(self, game_number):
        # The path to your JSON file
        file_path = 'munchkin_data.json'

        # Open the JSON file for reading
        with open(file_path, 'r') as file:
            # Load the JSON content from the file into a dictionary
            self.all_games = json.load(file)["games"]

        if game_number == -1:
            self.game_number = max([int(number) for number in self.all_games.keys()])       
        else:
            self.game_number = game_number
    
        self.strlevels = self.all_games[str(self.game_number)]["levels"]
        self.levels = {}
    
    def Listyfy(self):
        legit_dict = {}        
        for player_name in self.strlevels.keys():
            legit_dict[player_name] = string_to_float_list(self.strlevels[player_name])
        self.levels = legit_dict
    
    def Plot(self):
        self.Listyfy()
        x_values = list(range(1, len(next(iter(self.levels.values()))) + 1))
    
        plt.figure(figsize=(10, 6))

        colors = ['blue', 'green', 'red','brown', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple']
        enum = 0
        for player_name in self.levels.keys():
            plt.plot(x_values, self.levels[player_name], marker='o', linestyle='-', color=colors[enum], label=player_name)
            enum += 1

        plt.title(f"game {self.game_number}")  # Customize the title
        plt.xlabel('Turns')  # Customize with the appropriate time unit
        plt.ylabel('Levels')  # Customize the y-axis label
        plt.grid(True)  # Show grid
        plt.legend(loc="upper left")
        plt.tight_layout()  # Adjust layout
        plt.ylim(0.75, 12.0)
        plt.yticks(range(1, 13))
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.axhline(y=10, color='black', linewidth=2, linestyle='-')

        plt.show()

munch = munch_plot(4)
munch.Plot()
