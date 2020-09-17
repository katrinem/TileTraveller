# Assignment 8: TileTraveller
# T-111-PROG, Reykjavik University, fall term 2020
# Students: Karítas Etna, Katrín Edda, Lára Sóllilja

# This program is a computer game in which the player is located in a certain tile in a grid.
# At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.
# The player starts in tile (1,1). There are 12 tiles in total and the 'victory tile' is tile (3,1).

def display_directions(tile):
    '''This function takes the position as input and prints the directions the player can choose from,
    depending on the position.'''
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

def get_direction():
    '''This function prompts the user for a direction for the next move. It returns a string variable in lowercase letters.'''
    dir = input("Direction: ")
    dir = dir.lower()
    return dir

def error_check_direction(pos,dir):
    '''This function takes the player's position and direction as input. Depending on the position, it chekcs if
    the direction is valid. It returns True if valid, False if invalid.'''
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
    '''This funciton takes the player's position and direction as input. If the direction is valid, it updates the position
    according to the direction and returns a new position. If it is invalid, it prints an error message and returns the old position.'''
    new_position = ""
    if error_check_direction(old_position,direction): # Call a function to error check, returns True if direction is valid
        if direction == "n":
            new_position = old_position[0] + str(int(old_position[1])+1)
        elif direction == "s":
            new_position = old_position[0] + str(int(old_position[1])-1)
        elif direction == "w":
            new_position = str(int(old_position[0])-1) + old_position[1]
        elif direction == "e":
            new_position = str(int(old_position[0])+1) + old_position[1]
        return new_position
    else: # If direction is invalid
        print("Not a valid direction!")
        return old_position

# Initialize a string variable for the player's location. It has 2 digits that specify the row and column:
position = "11"

while position != '31':                # The position (3,1) is the victory tile.
    display_directions(position)
    direction = get_direction()        # Prompt user for direction
    position = update_position(position,direction)
else:
    print("Victory!")