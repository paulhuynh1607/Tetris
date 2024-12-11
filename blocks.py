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
        self.most_right = 0
        self.most_left = 0
        self.isFalling = False
        self.main_blocks = [[0, 0], [1, 0], [2, 0], [3, 0]]

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
            for i in range(len(self.each_block)):
                background.change_grid(self.color, self.each_block[i][0], self.each_block[i][1])

    def falling(self, speed, background):
        time.sleep(speed)
        for x in self.each_block:
            if x[1] >= self.anchor_blockY:
                self.anchor_blockY = x[1]

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
        self.most_right = self.each_block[0][0]
        for block in self.each_block:
            if block[0] > self.most_right:
                self.most_right = block[0]
        if self.most_right != 9:
            for i in range(len(self.each_block)):
                background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                self.each_block[i][0] += 1
                self.draw(background)

    def left(self, background):
        time.sleep(0.1)
        self.most_left = self.each_block[0][0]
        for block in self.each_block:
            if block[0] < self.most_left:
                self.most_left = block[0]
        if self.most_left != 0:
            for i in range(len(self.each_block)):
                background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                self.each_block[i][0] -= 1
                self.draw(background)

    def check_collide(self, background):

        for block in self.each_block:
            x, y = block[0], block[1]
            print(block)
            print(self.main_blocks)
            for m in range(len(self.main_blocks)):
                if self.main_blocks[m][1] <= y and self.main_blocks[m][0] == x:
                    self.main_blocks[m][1] = y
                    self.main_blocks[m][0] = x

        for m in self.main_blocks:
            x, y = m[0], m[1]
            if background.grid[y + 1][x] != 0:
                return True
            else:
                return False

    def update(self):
        self.each_block = []
        self.anchor_blockY = 0
        self.color = random.randint(1, 10)
        self.random_block = random.randint(0, 6)
        self.isBlock = False
        self.main_blocks = [[0, 0], [1, 0], [2, 0], [3, 0]]
