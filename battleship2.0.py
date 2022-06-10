"""
Legend:
1. "." = water or empty space 
2. "0" = part of a ship 
3. "X" = part of a ship that was hit
3. "#" = water that was hit with no ship

"""

# global variable for grid 
grid = [[]]
# global variable for grid size
grid_size = 10
# global variable for number of ships 
num_of_ships = 8
# global variable for bullets left
bullets_left = 50
# game over
game_over = False
# global variable for number of ships sunk 
num_of_ships_sunk = 0
# global variable for ship position
ship_positions = [[]]
# global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """ will check row and column to see if it is a valid area to place ship
        return True or False"""
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
            grid[r][c] = "0"
    return all_valid


def try_to_place_ship_on_grid(row, col, direction, length):
  """based on direction will call on helped method to help ship placement"""
    global grid_size
    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
        
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length
    
    return validate_grid_and_place_ship(0, 0, 0, 0)


def create_grid():
    """will create 10X10 grid and place ships at random
       has no return but will run try_to_place_ships_on_grid"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    pass

    try_to_place_ship_on_grid(0, 0, 0, 0)
