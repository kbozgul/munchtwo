import re
from read_and_write import read_lines, remove_last_lines, start_reading, add_new_line


def YesNo_to_TrueFalse(yes_or_no):
    if yes_or_no == "y":
        remove_last_lines(1)
        return True
    elif yes_or_no == "n":
        remove_last_lines(1)
        return False
    else:
        remove_last_lines(1)
        raise KeyError


def commandIdentifier(munchkin, command):
    print(f"we are inside commandIdentifier with command {command}")
    matchLevel = re.findall(r'([a-zA-Z])(-?\d+)', command)  
    if matchLevel:
        player_list = [match[0] for match in matchLevel]
        level_list = [int(match[1]) for match in matchLevel]
        if not len(player_list) == len(level_list):
            raise KeyError
        elif len(player_list) == len(level_list):
            munchkin.giveLevels(player_list, level_list)

    elif command == "cancel":
        if read_lines("logs/telegram.log", strip = True)[-2] == ".": #requires using strip
            munchkin.CancelSnapshot()
        else:
            munchkin.CancelLevels()
        
        remove_last_lines(2)

    elif command == "end":
        we_sure = YesNo_to_TrueFalse(start_reading("Are you sure? [y/n]"))
        if we_sure:
            munchkin.ManuelEnd()
        else:
            remove_last_lines(1) #for erasing end command

    elif command == ".":
        munchkin.TakeSnapshot()
    
    elif command == "serhatin annesi":
        add_new_line("logs/game.log","<3 <3 <3")

    else:
        remove_last_lines(1)
        raise KeyError



    