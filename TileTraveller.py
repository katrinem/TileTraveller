# TileTraveller

## Program description: 
# This program is a computer game in which the player is located in a certain tile in a grid.
# At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.
# The player starts in tile (1,1). There are 12 tiles in total and the 'victory tile' is tile (3,1).

## Algorithm: 

# ...

## Description of the functions:

# Display the directions available (function 1)
#   Input: position
#   Do: Print directions available
#   Return: None

# Get input from user to choose direction (function 2)
#   Input: direction
#   Do: Call error-check function
#   If True: Return direction
#   If False: Call direction function again AND calls itself again

# Error-chekc the user's choice (function3, function 2 will call it)
#   Input: direction
#   Do: Error-check and print the result
#   Return: True or False

# Update position (function 4)
#   Input: position, direction
#   Do: Update position
#   Return: new position


## The main program:

# Initialize a string variable for the player's location. It has 2 characters that specify the row and column, e.g. position = '11'.

# Wile position != '31'
#   Call display_directions function
#   Call Input function
#         Error check input within Input function (or update_position)
#   Call update_position function

