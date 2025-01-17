import random

# Define the tetromino shapes using a list of 2D arrays.
# Each sub-array represents a specific shape and its initial configuration.
tetrominos = [
    [[1, 1, 1],
     [0, 1, 0]],  # T-shape
    [[1, 1],
     [1, 1]],  # Square
    [[0, 0, 0, 0],
     [1, 1, 1, 1]],  # Line
    [[1, 1, 0],
     [0, 1, 1]],  # Z-shape
    [[0, 1, 1],
     [1, 1, 0]],  # S-shape
    [[1, 0, 0],
     [1, 1, 1]],  # L-shape
    [[0, 0, 1],
     [1, 1, 1]]  # J-shape
]


# The Blocks class manages the behavior of tetromino blocks, including movement,
# collision detection, and drawing on the game grid.
class Blocks:
    def __init__(self, background, scoreboard):
        # Initialize collision detection flag to False.
        self.isColliding = False
        # Randomly select a block shape (0 to 6 corresponds to tetrominos indices).
        self.random_block = random.randint(0, 6)
        # List to store the coordinates of each square in the block.
        self.each_block = []
        # Size of each square in the block (in pixels).
        self.size = 28
        # Randomly assign a color to the block (1 to 9).
        self.color = random.randint(1, 9)
        # Flag to check if a block is already active in the game.
        self.isBlock = False
        # The Y-coordinate of the lowest part of the block.
        self.anchor_blockY = 0
        # The X-coordinate of the rightmost part of the block.
        self.anchor_block_R = 0
        # The X-coordinate of the leftmost part of the block.
        self.anchor_block_L = 0
        # Reference to the scoreboard for score updates.
        self.scoreboard = scoreboard
        # Reference to the game background for grid management.
        self.background = background

    def setup(self):
        # Determine the boundaries of the block by finding the leftmost, rightmost, and lowest squares.
        self.anchor_block_R = self.each_block[0][0]  # Initialize right boundary with the first square.
        self.anchor_block_L = self.each_block[0][0]  # Initialize left boundary with the first square.
        for block in self.each_block:
            # Update the right boundary if the current square is farther right.
            if block[0] > self.anchor_block_R:
                self.anchor_block_R = block[0]
            # Update the lowest boundary if the current square is farther down.
            if block[1] >= self.anchor_blockY:
                self.anchor_blockY = block[1]
            # Update the left boundary if the current square is farther left.
            if block[0] < self.anchor_block_L:
                self.anchor_block_L = block[0]

    def draw(self):
        # Draw the block on the grid, or initialize it if it has not yet been placed.
        self.isColliding = False  # Reset collision flag.
        if not self.isBlock:  # If no block is currently active:
            self.each_block = []  # Clear any previous block data.
            self.anchor_blockY = 0  # Reset the Y-anchor position.
            shape = tetrominos[self.random_block]  # Get the shape of the current block.
            for y in range(len(shape)):  # Loop through the rows of the shape.
                for x in range(len(shape[y])):  # Loop through the columns of the shape.
                    if shape[y][x] != 0:  # If the cell is part of the block:
                        self.background.change_grid(self.color, x + 4, y)  # Draw it on the grid.
                        self.each_block.append([x + 4, y])  # Add its position to the block list.
            self.isBlock = True  # Mark that a block is now active.
        else:  # If a block is already active:
            self.setup()  # Update the block's boundary positions.
            for i in range(len(self.each_block)):  # Loop through the block's squares.
                self.background.change_grid(self.color, self.each_block[i][0], self.each_block[i][1])  # Draw them.

    def down(self):
        # Move the block down by one row, handling collisions and clearing rows.
        new_block = []  # Temporary list to store the new positions.
        old_block = self.each_block.copy()  # Copy the current positions.
        if self.anchor_blockY < 19:  # If the block is not at the bottom:
            for x, y in self.each_block:  # Calculate the new positions.
                new_block.append([x, y + 1])
            for x, y in old_block:  # Clear the old positions on the grid.
                self.background.change_grid(0, x, y)
            for x, y in new_block:  # Check for collisions at the new positions.
                if self.background.grid[y][x] != 0:  # If the new position is occupied:
                    self.each_block = old_block  # Revert to the old positions.
                    self.draw()  # Redraw the block.
                    self.background.clear_row(self.scoreboard)  # Clear any completed rows.
                    self.update()  # Prepare a new block.
                    self.isColliding = True  # Set the collision flag.
                    return
            self.each_block = new_block  # Update to the new positions.
            self.draw()  # Draw the block in its new position.
        else:  # If the block is at the bottom:
            self.background.clear_row(self.scoreboard)  # Clear any completed rows.
            self.update()  # Prepare a new block.

    def right(self):
        # Move the block to the right, if possible.
        new_block = []  # Temporary list to store the new positions.
        old_block = self.each_block.copy()  # Copy the current positions.
        if self.anchor_block_R != 9:  # If the block is not at the right boundary:
            for x, y in self.each_block:  # Calculate the new positions.
                new_block.append([x + 1, y])
            for x, y in old_block:  # Clear the old positions on the grid.
                self.background.change_grid(0, x, y)
            for x, y in new_block:  # Check for collisions at the new positions.
                if self.background.grid[y][x] != 0:  # If the new position is occupied:
                    self.each_block = old_block  # Revert to the old positions.
                    self.draw()  # Redraw the block.
                    return
            self.each_block = new_block  # Update to the new positions.
            self.draw()  # Draw the block in its new position.

    def left(self):
        # Move the block to the left, if possible.
        new_block = []  # Temporary list to store the new positions.
        old_block = self.each_block.copy()  # Copy the current positions.
        if self.anchor_block_L != 0:  # If the block is not at the left boundary:
            for x, y in self.each_block:  # Calculate the new positions.
                new_block.append([x - 1, y])
            for x, y in old_block:  # Clear the old positions on the grid.
                self.background.change_grid(0, x, y)
            for x, y in new_block:  # Check for collisions at the new positions.
                if self.background.grid[y][x] != 0:  # If the new position is occupied:
                    self.each_block = old_block  # Revert to the old positions.
                    self.draw()  # Redraw the block.
                    return
            self.each_block = new_block  # Update to the new positions.
            self.draw()  # Draw the block in its new position.

    def rotate(self):
        # Rotate the block around its center, if possible.
        old_block = self.each_block.copy()  # Copy the current positions.
        new_block = []  # Temporary list to store the rotated positions.
        if self.random_block == 1:  # Square blocks do not need to rotate.
            return
        if self.anchor_blockY < 19 and self.anchor_blockY != 0:  # If the block is within bounds:
            center_x = sum(x for x, y in self.each_block) // len(self.each_block)  # Calculate the center for x
            center_y = sum(y for x, y in self.each_block) // len(self.each_block)  # Calculate the center for y
            # Rotate each block in the current block by 90 degrees around its center.
            for x, y in self.each_block:
                new_x = center_x + (y - center_y)  # Calculate the new x-coordinate after rotation
                new_y = center_y - (x - center_x)  # Calculate the new y-coordinate after rotation
                new_block.append([new_x, new_y])  # Append the rotated block's new coordinates

            # Check if the new block positions are within the valid grid boundaries (0 ≤ x < 10, 1 ≤ y < 20).
            if all(0 <= x < 10 and 1 <= y < 20 for x, y in new_block):
                if len(new_block) != 0:
                    # Clear the old block positions from the background grid.
                    for x, y in old_block:
                        self.background.change_grid(0, x, y)

                    # Check if any new block position collides with an already filled grid cell.
                    for x, y in new_block:
                        if self.background.grid[y][x] != 0:
                            # If there's a collision, revert back to the old block positions and redraw.
                            self.each_block = old_block
                            self.draw()
                            return

                    # Update the current block to the new rotated positions and redraw it.
                    self.each_block = new_block
                    self.draw()

                    # Check if the block is one of the specified random blocks (block 6, 5, or 2) and apply a
                    # downward movement.
                    if self.random_block == 6 or 5 or 2:
                        self.down()  # Move the block downward if conditions are met.
            else:
                # If the new block positions are out of bounds, revert back to the old block positions.
                self.each_block = old_block

    def check_game_end(self):
        # Check if the game has ended (if the top of the grid is blocked by a falling block).
        if self.anchor_blockY <= 2 and self.isColliding:
            return True  # Game over condition: block collides at the top
        else:
            self.isColliding = False  # Reset collision state
            return False  # Game continues

    def update(self):
        # Reset block attributes for the creation of a new block.
        self.color = random.randint(1, 9)  # Assign a new random color to the block.
        self.random_block = random.randint(0, 6)  # Choose a random block type.
        self.isBlock = False  # Reset block status for the new block.
