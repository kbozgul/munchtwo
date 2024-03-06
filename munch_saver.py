import json
from datetime import datetime
import os


def json_saver(munchkin):
    # Get the current date and time
    current_time = datetime.now()
    # Format the current date and time as a string in the format "DD MM YYYY"
    formatted_time = current_time.strftime("%d %m %Y %H:%M:%S")
    # Create a Python dictionary with one of the values being another dictionary

    one_game = {
        "date": formatted_time,
        "is_complete": str(not munchkin.manuelly_ended),
        "winner": str(munchkin.winners),
        "number of turns": munchkin.turn,
        "levels": munchkin.snapshots
    }
    
    # Attempt to read the existing data from my_data.json
    try:
        with open('munchkin_data.json', 'r') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, initialize an empty list or dictionary
        data = {}
        data["total number of games"] = 0
        data["total wins"] = {
            "k": 0,
            "s": 0,
            "m": 0,
            "z": 0,
        }
        data["games"] = {}
    
    # Add the new game data to the existing data structure
    # If data is a list of games, append one_game
    data["total number of games"] += 1
    data["games"][str(data["total number of games"])] = one_game
    for winner in munchkin.winners:
        try:
            data["total wins"][winner] += 1
        except (KeyError):
            data["total wins"][winner] = 1
    # If data should be a dictionary with unique keys for each game, you'd need to define a unique key strategy
    
    # Save the updated data back to the file
    with open('munchkin_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
