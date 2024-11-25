import pygame


class Blocks:
    def __init__(self):
        self.blockY = 29
        self.blockX = 29
        self.rect = pygame.Rect(150, 30, self.blockX, self.blockY)

    def create(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)

    def falling(self, speed):
        if self.rect.y != 600:
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

