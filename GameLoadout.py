import pygame
import time

class Background:
    def __init__(self):
        # Initialize grid dimensions and create a blank grid (10 columns and 20 rows)
        self.columns = 10
        self.rows = 20
        self.size = 30  # Size of each grid cell
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]  # 2D list to represent the grid
        self.colour = self.colors()  # Get the color palette for the grid
        self.total_val = 0

    def change_grid(self, value, x, y):
        # Update the value at the specific grid position (x, y)
        self.grid[y][x] = value

    def colors(self):
        # Define the color palette for different block types and empty space
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        white = (255, 255, 255)
        dark_blue = (44, 44, 127)
        light_blue = (59, 85, 162)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue, white, dark_blue, light_blue]

    def reset_grid(self):
        # Reset the grid to its initial empty state
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]

    def play_again(self):
        # Ask the user if they want to play again after the game ends
        yes_or_no = input("Would you like to play the game again?").lower()
        if yes_or_no == "yes":
            self.reset_grid()  # Reset grid if the user wants to play again
            return True
        elif yes_or_no == "no":
            return False  # Exit if the user doesn't want to play again
        else:
            self.play_again()  # Ask again if the input is invalid

    def draw_grid(self, screen):
        # Draw the grid on the screen by iterating through each cell and drawing a rectangle
        for row in range(self.rows):
            for column in range(self.columns):
                cell_value = self.grid[row][column]  # Get the color index for the cell
                cell_rect = pygame.Rect(column * self.size + 30, row * self.size + 120, self.size - 1, self.size - 1)
                pygame.draw.rect(screen, self.colour[cell_value], cell_rect)

    def clear_row(self, scoreboard):
        # Check and clear filled rows and shift the above rows down
        for y in range(self.rows - 1, -1, -1):  # Iterate from bottom to top
            if all(self.grid[y][x] != 0 for x in range(self.columns)):  # If the row is filled
                time.sleep(0.1)  # Add a slight delay before clearing
                scoreboard.add_point(10)  # Add points for clearing the row
                # Clear the filled row
                for x in range(self.columns):
                    self.change_grid(0, x, y)
                # Shift all rows above it down by one row
                for row in range(y - 1, -1, -1):
                    for col in range(self.columns):
                        self.grid[row + 1][col] = self.grid[row][col]
                    # Clear the now empty row
                    for col in range(self.columns):
                        self.grid[row][col] = 0
                self.clear_row(scoreboard)  # Recursively check for more filled rows
        return
