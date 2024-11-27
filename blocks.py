import pygame
from GameLoadout import Background
import random
background = Background()

tetrominos = [
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
        self.random_block = 0

    def draw(self):
        shape = tetrominos[self.random_block]
        background.grid[0][0] = 1
        for i in shape:
            for j in range(len(i)):
                pass

    def falling(self, speed):
        pass

    def left(self, speed):
        pass

    def right(self, speed):
        pass
