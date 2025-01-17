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
    def __init__(self, background, scoreboard):
        self.isColliding = False
        self.random_block = random.randint(0, 6)
        self.each_block = []
        self.size = 28
        self.color = random.randint(1, 9)
        self.isBlock = False
        self.anchor_blockY = 0
        self.anchor_block_R = 0
        self.anchor_block_L = 0
        self.scoreboard = scoreboard
        self.background = background


    def setup(self):
        self.anchor_block_R = self.each_block[0][0]
        self.anchor_block_L = self.each_block[0][0]
        for block in self.each_block:
            if block[0] > self.anchor_block_R:
                self.anchor_block_R = block[0]
            if block[1] >= self.anchor_blockY:
                self.anchor_blockY = block[1]
            if block[0] < self.anchor_block_L:
                self.anchor_block_L = block[0]

    def draw(self):
        self.isColliding = False
        if not self.isBlock:
            self.isColliding = False
            self.each_block = []
            self.anchor_blockY = 0
            shape = tetrominos[self.random_block]
            for y in range(len(shape)):
                for x in range(len(shape[y])):
                    if shape[y][x] != 0:
                        self.background.change_grid(self.color, x + 4, y)
                        self.each_block.append([x + 4, y])
            self.isBlock = True
        else:
            self.setup()
            for i in range(len(self.each_block)):
                self.background.change_grid(self.color, self.each_block[i][0], self.each_block[i][1])

    def down(self):
        new_block = []
        old_block = self.each_block.copy()
        # Check for collision before moving down
        if self.anchor_blockY < 19:
            for x, y in self.each_block:
                new_block.append([x, y+1])
            for x, y in old_block:
                self.background.change_grid(0, x, y)
            for x, y in new_block:
                if self.background.grid[y][x] != 0:
                    self.each_block = old_block
                    self.draw()
                    self.background.clear_row(self.scoreboard)
                    self.update()
                    self.isColliding = True
                    return
            self.each_block = new_block
            self.draw()  # Draw the new position
        else:
            self.background.clear_row(self.scoreboard)
            self.update()
            return

    def right(self):
        new_block = []
        old_block = self.each_block.copy()
        # Check for collision before moving down
        if self.anchor_block_R != 9:
            for x, y in self.each_block:
                new_block.append([x+1, y])
            for x, y in old_block:
                self.background.change_grid(0, x, y)
            for x, y in new_block:
                if self.background.grid[y][x] != 0:
                    self.each_block = old_block
                    self.draw()
                    return
            self.each_block = new_block
            self.draw()  # Draw the new position
        else:
            return

    def left(self):
        new_block = []
        old_block = self.each_block.copy()
        # Check for collision before moving down
        if self.anchor_block_L != 0:
            for x, y in self.each_block:
                new_block.append([x - 1, y])
            for x, y in old_block:
                self.background.change_grid(0, x, y)
            for x, y in new_block:
                if self.background.grid[y][x] != 0:
                    self.each_block = old_block
                    self.draw()
                    return
            self.each_block = new_block
            self.draw()  # Draw the new position
        else:
            return

    def rotate(self):
        old_block = self.each_block.copy()
        new_block = []
        if self.random_block == 1:
            return
        if self.anchor_blockY < 19 and self.anchor_blockY != 0:
            center_x = sum(x for x, y in self.each_block) // len(self.each_block)
            center_y = sum(y for x, y in self.each_block) // len(self.each_block)
            for x, y in self.each_block:
                new_x = center_x + (y - center_y)
                new_y = center_y - (x - center_x)
                new_block.append([new_x, new_y])

        if all(0 <= x < 10 and 1 <= y < 20 for x, y in new_block):
            if len(new_block) != 0:
                for x, y in old_block:
                    self.background.change_grid(0, x, y)
                for x, y in new_block:
                    if self.background.grid[y][x] != 0:
                        self.each_block = old_block
                        self.draw()
                        return

                self.each_block = new_block
                self.draw()
                if self.random_block == 6 or 5 or 2:
                    self.down()
        else:
            self.each_block = old_block

    def check_game_end(self):
        if self.anchor_blockY <= 2 and self.isColliding:
            return True
        else:
            self.isColliding = False
            return False

    def update(self):
        self.color = random.randint(1, 9)
        self.random_block = random.randint(0, 6)
        self.isBlock = False

