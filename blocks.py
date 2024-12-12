import time

import pygame
import random

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


#
class Blocks:
    def __init__(self):
        self.random_block = random.randint(0, 6)
        self.each_block = []
        self.size = 28
        self.color = random.randint(1, 10)
        self.isBlock = False
        self.anchor_blockY = 0
        self.anchor_block_R = 0
        self.anchor_block_L = 0
        self.isFalling = False
        self.down_collide_blocks = []
        self.collide_left = False
        self.collide_right = False

    def setup(self):
        for x in self.each_block:
            if x[1] >= self.anchor_blockY:
                self.anchor_blockY = x[1]

        self.anchor_block_R = self.each_block[0][0]
        for block in self.each_block:
            if block[0] > self.anchor_block_R:
                self.anchor_block_R = block[0]

        self.anchor_block_L = self.each_block[0][0]
        for block in self.each_block:
            if block[0] < self.anchor_block_L:
                self.anchor_block_L = block[0]

    def draw(self, background):
        if not self.isBlock:
            shape = tetrominos[self.random_block]
            for y in range(len(shape)):
                for x in range(len(shape[y])):
                    if shape[y][x] != 0:
                        background.change_grid(self.color, x, y)
                        self.each_block.append([x, y])
            self.isBlock = True
            self.isFalling = True
        else:
            self.setup()
            for i in range(len(self.each_block)):
                background.change_grid(self.color, self.each_block[i][0], self.each_block[i][1])

    def falling(self, speed, background):
        time.sleep(speed)
        # Check for collision before moving down
        if self.anchor_blockY < 19 and not self.check_collide(background):
            for i in range(len(self.each_block)):
                background.change_grid(0, self.each_block[i][0], self.each_block[i][1])  # Clear current position
                self.each_block[i][1] += 1  # Move down
            self.draw(background)  # Draw the new position
        else:
            self.update()  # Update the block if it can't fall

    def right(self, background):
        time.sleep(0.1)
        if self.anchor_block_R != 9:
            if not self.collide_right:
                for i in range(len(self.each_block)):
                    background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                    self.each_block[i][0] += 1
                    self.draw(background)
        self.collide_right = False

    def left(self, background):
        time.sleep(0.1)
        if self.anchor_block_L != 0:
            if not self.collide_left:
                for i in range(len(self.each_block)):
                    background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                    self.each_block[i][0] -= 1
                    self.draw(background)
        self.collide_left = False

    def check_collide(self, background):
        for i in range(background.columns):
            self.down_collide_blocks.append([i, 0])
        for block in self.each_block:
            x, y = block[0], block[1]
            for m in range(len(self.down_collide_blocks)):
                if self.down_collide_blocks[m][1] <= y and self.down_collide_blocks[m][0] == x:
                    self.down_collide_blocks[m][1] = y
                    self.down_collide_blocks[m][0] = x

        for m in range(len(self.down_collide_blocks)):
            x, y = self.down_collide_blocks[m][0], self.down_collide_blocks[m][1]
            if background.grid[y + 1][x] != 0:
                return True
            if self.anchor_block_L != 0:
                if background.grid[y][self.anchor_block_L - 1] != 0:
                    self.collide_left = True
            if self.anchor_block_R != 9:
                if background.grid[y][self.anchor_block_R + 1] != 0:
                    self.collide_right = True
        return False

    def update(self):
        self.each_block = []
        self.anchor_blockY = 0
        self.color = random.randint(1, 10)
        self.random_block = random.randint(0, 6)
        self.isBlock = False
        self.down_collide_blocks = [[0, 0], [1, 0], [2, 0], [3, 0]]
