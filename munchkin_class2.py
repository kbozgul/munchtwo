from read_and_write import start_reading, add_new_line, remove_last_lines
from munch_saver import json_saver
from command_list import YesNo_to_TrueFalse


class Munchkin:
    def __init__(self): #Takes names as single letters and creates a dictionary with keys as letters and values as Munchkin_player instances
        self.is_complete = False
        self.manuelly_ended = False
        self.turn = 1
        self.winners = []
        names_list = [letter for letter in start_reading("Please enter the names of the players:\n") if letter != " "]
        self.players = {}
        self.snapshots = {}
        for player_name in names_list:
            self.players[player_name] = [1]
            self.snapshots[player_name] = [1]


    
    def LevelUp(self, player_name, level):
        self.players[player_name].append(self.players[player_name][-1] + level)
    
    def giveLevels(self, player_list, level_list):
        for i in range(len(player_list)):
            self.LevelUp(player_list[i], level_list[i])
        blanck_players = [element for element in self.players.keys() if element not in player_list]
        for player_name in blanck_players:
            self.LevelUp(player_name, 0)
    
    def TakeSnapshot(self):
        self.turn += 1
        print(f"self.turn is: {self.turn}")
        for player_name in self.players.keys():
            current_level = self.players[player_name][-1]
            self.snapshots[player_name].append(current_level)
    
    def SendToSaver(self):
        for player_name in self.snapshots.keys(): #stringify the levels for visual reasons
            self.snapshots[player_name] = str(self.snapshots[player_name])
        json_saver(self)
    
    def CancelSnapshot(self):
        self.turn -= 1
        for player_snapshot_list in self.snapshots.values():
            player_snapshot_list.pop()
    
    def CancelLevels(self):
        for player_level_list in self.players.values():
            player_level_list.pop()

    def DisplayLevels(self):
        display_list = []
        display_list.append(f"Turn Number: {self.turn}")
        for player_name in self.players.keys():
            display_list.append(f"{player_name}: " + str(self.players[player_name][-10:]))
        modified = "\n".join(display_list)
        add_new_line("logs/game.log", modified)

    def ManuelEnd(self):#printing the winners will be done by checkLevelLimit
        max_level = max([level_list[-1] for level_list in self.players.values()])
        for player_name in self.players.keys():
            if self.players[player_name][-1] == max_level: #ended by hand. nobody is 10 or above
                self.winners.append(player_name)

        self.manuelly_ended = True
        self.is_complete = True
    
    def checkLevelLimit(self): #checks who wins and then displays their name. changes munchkin.
        somebody_won = False
        win_list = []  

        for player_name in self.players.keys():
            if self.players[player_name][-1] >= 10:
                somebody_won =True
                win_list.append(player_name)
        
        if somebody_won:
            we_sure = YesNo_to_TrueFalse(start_reading("Somebody reached level 10 or above! Are you sure? [y/n]: "))
            if we_sure:
                self.winners = win_list  
                self.is_complete = True
            else:
                self.CancelLevels()
    

    def GameOver(self):
        if self.is_complete:
            if len(self.winners) == 1:
                add_new_line("logs/game.log", f"GAME OVER! The winner is {self.winners[0]}")
            elif len(self.winners) > 1:
                add_new_line("logs/game.log", f"GAME OVER! The winners are {self.winners}")

            self.TakeSnapshot()
            self.SendToSaver()
    
    def CheckGameOver(self):
        self.checkLevelLimit()
        if self.is_complete:
            self.GameOver()
            