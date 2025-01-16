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
        self.down_collide_blocks = []
        self.left_collide_blocks = []
        self.right_collide_blocks = []
        self.collide_left = False
        self.collide_right = False
        self.scoreboard = scoreboard
        self.background = background
        self.rotate_time = 0
        self.can_rotate = True
        self.rl = 0
        self.ll = 0
        self.dl = 0

    def setup(self):
        self.can_rotate = True
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
            self.check_collide()
        else:
            self.setup()
            for i in range(len(self.each_block)):
                self.background.change_grid(self.color, self.each_block[i][0], self.each_block[i][1])

    def falling(self):
        # Check for collision before moving down
        if self.anchor_blockY < 19 and not self.check_collide():
            for i in range(len(self.each_block)):
                self.background.change_grid(0, self.each_block[i][0], self.each_block[i][1])  # Clear current position
                self.each_block[i][1] += 1  # Move down
            self.draw()  # Draw the new position
            return
        else:
            self.background.clear_row(self.scoreboard)
            self.update()  # Update the block if it can't fall

    def down(self):
        # Check for collision before moving down
        if self.anchor_blockY < 19 and not self.check_collide():
            for i in range(len(self.each_block)):
                self.background.change_grid(0, self.each_block[i][0], self.each_block[i][1])  # Clear current position
                self.each_block[i][1] += 1  # Move down
            self.draw()  # Draw the new position
        else:
            self.background.clear_row(self.scoreboard)
            self.update()

    def right(self):
        self.check_collide()
        if self.anchor_block_R != 9 and self.isBlock:
            if not self.collide_right:
                for i in range(len(self.each_block)):
                    self.background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                    self.each_block[i][0] += 1
                    self.draw()
            else:
                self.collide_right = False
                return
        self.collide_right = False

    def left(self):
        self.check_collide()
        if self.anchor_block_L != 0 and self.isBlock:
            if not self.collide_left:
                for i in range(len(self.each_block)):
                    self.background.change_grid(0, self.each_block[i][0], self.each_block[i][1])
                    self.each_block[i][0] -= 1
                    self.draw()
            else:
                self.collide_left = False
                return
        self.collide_left = False

    def find_key_block(self):
        self.right_collide_blocks = []
        self.left_collide_blocks = []
        self.down_collide_blocks = []
        for block in self.each_block:
            x, y = block[0], block[1]
            if self.anchor_blockY != 19:
                if self.background.grid[y + 1][x] == 0:
                    self.down_collide_blocks.append([x, y])
            if self.anchor_block_L != 0:
                if self.background.grid[y][x - 1] == 0:
                    self.left_collide_blocks.append([x, y])
            if self.anchor_block_R != 9:
                if self.background.grid[y][x + 1] == 0:
                    self.right_collide_blocks.append([x, y])

    def check_collide(self):
        if not self.ll or not self.rl or not self.dl:
            self.rl = len(self.right_collide_blocks)
            self.ll = len(self.left_collide_blocks)
            self.dl = len(self.down_collide_blocks)
        self.find_key_block()

        if self.rl > len(self.right_collide_blocks):
            self.collide_right = True
        if self.ll > len(self.left_collide_blocks):
            self.collide_left = True
        if self.dl > len(self.down_collide_blocks):
            self.isColliding = True
            return True

        if self.anchor_block_L != 0:
            for i in range(len(self.left_collide_blocks)):
                x, y = self.left_collide_blocks[i][0], self.left_collide_blocks[i][1]
                if self.anchor_block_L != 0:
                    if self.background.grid[y][x - 1] != 0:
                        self.collide_left = True
        if self.anchor_block_R != 9:
            for i in range(len(self.right_collide_blocks)):
                x, y = self.right_collide_blocks[i][0], self.right_collide_blocks[i][1]
                if self.anchor_block_R != 9:
                    if self.background.grid[y][x + 1] != 0:
                        self.collide_right = True

        for m in range(len(self.down_collide_blocks)):
            x, y = self.down_collide_blocks[m][0], self.down_collide_blocks[m][1]
            if self.anchor_blockY != 19:
                if self.background.grid[y + 1][x] != 0:
                    self.isColliding = True
                    self.background.clear_row(self.scoreboard)
                    self.down_collide_blocks = []
                    return True
        return False

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

        if all(0 <= x < 10 and 1 <= y < 20 for x, y in new_block) and not self.check_collide():
            if len(new_block) != 0:
                for x, y in old_block:
                    self.background.change_grid(0, x, y)
                for x, y in new_block:
                    if self.background.grid[y][x] != 0:
                        print("stop")
                        self.each_block = old_block
                        for x1, y1 in old_block:
                            self.background.change_grid(self.color, x1, y1)
                        return

                self.each_block = new_block
                self.draw()
                self.find_key_block()
                self.rl = len(self.right_collide_blocks)
                self.ll = len(self.left_collide_blocks)
                self.dl = len(self.down_collide_blocks)
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
        self.can_rotate = False
        self.rl = 0
        self.ll = 0
        self.dl = 0
        self.right_collide_blocks = []
        self.left_collide_blocks = []
        self.down_collide_blocks = []
        self.color = random.randint(1, 9)
        self.random_block = random.randint(0, 6)
        self.isBlock = False
        self.down_collide_blocks = []

