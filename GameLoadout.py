import pygame


class Background:
    def __init__(self):
        self.blockY = 30
        self.blockX = 30
        self.rect = pygame.Rect(30, 30, self.blockX, self.blockY)

    def grid(self, x_coord, y_coord, screen):
        for x in range(1, x_coord):
            self.blockX = 30*x
            for y in range(1, y_coord):
                self.blockY = 30*y
                self.rect = pygame.Rect(30, 30, self.blockX, self.blockY)
                pygame.draw.rect(screen, "white", self.rect, 2)
