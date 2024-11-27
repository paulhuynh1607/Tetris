import pygame

SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],  # T-shape
    [[1, 1],
     [1, 1]],  # Square
    [[1, 1, 1, 1]],  # Line
    [[1, 1, 0],
     [0, 1, 1]],  # Z-shape
    [[0, 1, 1],
     [1, 1, 0]],  # S-shape
    [[1, 0, 0],
     [1, 1, 1]],  # L-shape
    [[0, 0, 1],
     [1, 1, 1]]  # J-shape
]


class Blocks:
    def __init__(self):
        self.blockY = 29
        self.blockX = 29
        self.rect = pygame.Rect(150, 30, self.blockX, self.blockY)

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)

    def falling(self, speed):
        if self.rect.y != 570:
            self.rect.move_ip(0, speed)
        else:
            self.rect.x = 150
            self.rect.y = 30

    def left(self, speed):
        if self.rect.x != 30:
            self.rect.move_ip(speed, 0)

    def right(self, speed):
        if self.rect.x != 270:
            self.rect.move_ip(speed, 0)
