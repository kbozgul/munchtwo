import time
import os


def add_new_line(filename, message):
    with open(filename, 'a') as f:
        f.write(message + '\n')

def start_reading(message, read_filename = "logs/telegram.log", write_filename = "logs/game.log", interval=0.2):
    add_new_line(write_filename, message)
    with open(read_filename, 'r') as f:
        # Move the pointer to the end of the file
        f.seek(0, os.SEEK_END)
        position = f.tell()
        while True:
            # Sleep for a while
            time.sleep(interval)
            # Check if the file size has changed
            f.seek(0, os.SEEK_END)
            current_position = f.tell()
            if current_position <= position:
                continue
            # Read new lines and print
            f.seek(position, os.SEEK_SET)
            new_lines = f.readlines()  # Read all new lines into a list
            return new_lines[-1][:-1]  # Return the list of new lines
        
def read_lines(filename = "logs/telegram.log", strip = False): #requires using .strip() for exracting content
    with open(filename, 'r') as f:
        if not strip:
            lines = f.readlines()
            return lines
        else:
            lines = [line.strip() for line in f.readlines()]
            return lines

def remove_last_lines(n, filename = "logs/telegram.log"):
    with open(filename, 'r+') as f:
        lines = read_lines(filename)
        # Go back to the start of the file
        f.seek(0)
        # Write all but the last line back to the file
        f.writelines(lines[:-n])
        # Truncate the file to remove any leftover content
        f.truncate()