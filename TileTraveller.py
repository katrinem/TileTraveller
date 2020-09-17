# TileTraveller

## Program description: 
# This program is a computer game in which the player is located in a certain tile in a grid.
# At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.
# The player starts in tile (1,1). There are 12 tiles in total and the 'victory tile' is tile (3,1).

## Algorithm: 

# ...

## Description of the functions:

# Function 1: display_directions(tile) Display the directions available (function 1)

def display_directions(tile):
    if tile[1] == "1":
        print("You can travel: (N)orth.")
    elif tile == "12":
        print("You can travel: (N)orth, (E)ast or (S)outh.")
    elif tile == "13":
        print("You can travel: (E)ast or (S)outh.")
    elif tile == "23":
        print("You can travel: (E)ast or (W)est")
    elif tile == "22" or tile == "33":
        print("You can travel: (S)outh or (W)est")
    elif tile == "32":
        print("You can travel: (N)orth or (S)outh")

#   Input: position
#   Do: Print directions available
#   Return: None

# Function 2: get_direction(position) Get input from user to choose direction (function 2)
#   Input: position
#   Do: prompt user for direction (s,w,e,n)
#   Do: Call error-check function
#   If True: Return direction
#   If False: Call direction function again AND calls itself again

# Function 3: error_check_direction(direction,position) Error-check the user's choice (function3, function 2 will call it)
#   Input: direction
#   Do: Error-check and print the result
#   Return: True or False

# Function 4: update_position() Update position (function 4)
#   Input: position, direction
#   Do: Update position
#   Return: new position


## The main program:

# Initialize a string variable for the player's location. It has 2 characters that specify the row and column, e.g. position = '11'.
position = "11"

while position != '31':                   # Call display_directions function
    direction = display_directions(position)             #   Call Input function
                                                    #   Error check input within Input function (or update_position)
    #position = update_position(position, direction) #   Call update_position function
#print("Victory")


