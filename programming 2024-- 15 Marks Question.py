#A computer game has a 5x5 grid.

#The player starts at top left of the grid, and a random cell is selected to be a secret cell. All the other cells would also be cleared.

'''A player is tasked to find the secret cell in 10 moves.
The player an move left, right, up, and down around the grid.
However, the player cannot go out of bounds of the grid.'''

#If the player fails to find the secret cell in under 10 moves then a message of losing is displayed. If the player does suceed then a message of him winning is displayed.

# Initialize the starting position
x, y = 0, 0
moves_left = 10

def down(x, y):
    """Move down (increase y-coordinate)."""
    return x, y + 1

def up(x, y):
    """Move up (decrease y-coordinate)."""
    return x, y - 1

def left(x, y):
    """Move left (decrease x-coordinate)."""
    return x - 1, y

def right(x, y):
    """Move right (increase x-coordinate)."""
    return x + 1, y

def create_grid(x, y):
    """Create a 5x5 grid and mark the current position and destination."""
    grid_size = 5
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    if 0 <= y < grid_size and 0 <= x < grid_size:
        grid[y][x] = 'P'  # Mark current position
    grid[4][1] = 'X'  # Mark destination
    return grid

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(' '.join(row))
    print()

# Main loop to handle user input and move the position
while moves_left > 0:
    # Create and print the grid with the current position
    grid = create_grid(x, y)
    print_grid(grid)
    
    # Check if "P" has found "X"
    if x == 1 and y == 4:
        print("Congratulations! You found 'X' and won the game!")
        break
    
    # Take the next move as input
    move = int(input("Enter Next Move! (Press 0 for down, 2 for up, 1 for left, and 3 for right, or 9 to exit): "))
    
    # Determine the move and update coordinates
    if move == 0:
        print("Moving Down")
        x, y = down(x, y)
    elif move == 2:
        print("Moving Up")
        x, y = up(x, y)
    elif move == 1:
        print("Moving Left")
        x, y = left(x, y)
    elif move == 3:
        print("Moving Right")
        x, y = right(x, y)
    elif move == 9:
        print("Exiting...")
        break
    else:
        print("Not a valid key press")
        continue  # Skip the rest of the loop and prompt for a valid move
    
    # Ensure the point stays within the grid boundaries
    if x < 0 or x > 4 or y < 0 or y > 4:
        print("Game Over! 'P' went out of bounds.")
        break
    
    # Decrement the move counter
    moves_left -= 1
    print(f"Moves left: {moves_left}")
    
    # Clear the console for better readability
    print("\n" * 5)

# Check if the game ended without finding 'X'
if moves_left == 0 and (x != 0 or y != 2):
    print("Game Over! You didn't find 'X' within 10 moves.")
