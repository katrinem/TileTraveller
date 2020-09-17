# TileTraveller

## Program description: 
# This program is a computer game in which the player is located in a certain tile in a grid.
# At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.
# The player starts in tile (1,1). There are 12 tiles in total and the 'victory tile' is tile (3,1).

## Algorithm: 

# ...

# Function 1: display_directions(tile) Display the directions available (function 1)

def display_directions(tile):
    if tile[1] == "1":
        print("You can travel: (N)orth.")
    elif tile == "12":
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif tile == "13":
        print("You can travel: (E)ast or (S)outh.")
    elif tile == "23":
        print("You can travel: (E)ast or (W)est")
    elif tile == "22" or tile == "33":
        print("You can travel: (S)outh or (W)est")
    elif tile == "32":
        print("You can travel: (N)orth or (S)outh")

# Function 2: get_direction(position) Get input from user to choose direction (function 2)
#   Input: position
def get_direction(pos):
    dir = input("Direction: ")
    dir = dir.lower()
    return dir

# Function 3: error_check_direction(direction,position) Error-check the user's choice (function3, function 2 will call it)
def error_check_direction(pos,dir):
    if pos[1] == "1" and dir == "n":
        return True
    elif pos == "12" and dir != "w":
        return True
    elif pos == "13" and (dir == "e" or dir == "s"):
        return True
    elif pos == "23" and (dir == "e" or dir == "w"):
        return True
    elif (pos == "22" or pos == "33") and (dir == "s" or dir == "w"):
        return True
    elif pos == "32" and (dir == "n" or dir == "s"):
        return True
    else:
        return False

# Function 4: update_position() Update position (function 4)
def update_position(old_position,direction):
    new_position = ""
    if error_check_direction(old_position,direction):
        if direction == "n":
            new_position = old_position[0] + str(int(old_position[1])+1)
        elif direction == "s":
            new_position = old_position[0] + str(int(old_position[1])-1)
        elif direction == "w":
            new_position = str(int(old_position[0])-1) + old_position[1]
        elif direction == "e":
            new_position = str(int(old_position[0])+1) + old_position[1]
        return new_position
    else:
        print("Not a valid direction!")
        return old_position

## The main program:

# Initialize a string variable for the player's location. It has 2 characters that specify the row and column, e.g. position = '11'.
position = "11"

while position != '31':                   
    display_directions(position)
    direction = get_direction(position)
    position = update_position(position,direction)
else:
    print("Victory!")


