import pygame


class Background:
    def __init__(self):
        self.columns = 10
        self.rows = 20
        self.size = 30
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colour = self.colours()

    def colours(self):
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
                cell_rect = pygame.Rect(column*self.size + 1, row*self.size + 1, self.size - 1, self.size - 1)
                pygame.draw.rect(screen, self.colour[cell_value], cell_rect)
