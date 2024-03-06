
from command_list import commandIdentifier
from munchkin_class2 import Munchkin
from read_and_write import start_reading, add_new_line







munchkin = Munchkin()

while not munchkin.is_complete:

    munchkin.DisplayLevels()

    command = start_reading("Insert command: ")
    try:
        commandIdentifier(munchkin, command)
        munchkin.CheckGameOver()
    except:
        add_new_line("logs/game.log",f"something went wrong")









