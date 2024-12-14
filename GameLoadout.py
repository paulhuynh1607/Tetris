import pygame


class Background:
    def __init__(self):
        self.columns = 10
        self.rows = 20
        self.size = 30
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colour = self.colors()
        self.total_val = 0

    def change_grid(self, value, x, y):
        self.grid[y][x] = value

    def colors(self):
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

    def draw_grid(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.size + 30, row * self.size + 30, self.size - 1, self.size - 1)
                pygame.draw.rect(screen, self.colour[cell_value], cell_rect)

    def clear_row(self):
        # Iterate through the rows in reverse order to avoid index issues when removing rows
        for y in range(self.rows - 1, -1, -1):
            # Check if the current row is filled
            if all(self.grid[y][x] != 0 for x in range(self.columns)):
                # Clear the filled row
                for x in range(self.columns):
                    self.change_grid(0, x, y)
                # Shift all rows above down by one
                for row in range(y - 1, -1, -1):
                    for col in range(self.columns):
                        self.grid[row + 1][col] = self.grid[row][col]
                    # Clear the now empty row
                    for col in range(self.columns):
                        self.grid[row][col] = 0
                self.clear_row()
            else:
                return
