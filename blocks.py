import pygame


class Blocks:
    def __init__(self):
        self.blockY = 29
        self.blockX = 29
        self.rect = pygame.Rect(150, 30, self.blockX, self.blockY)

    def create(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)
        print("New block create")

    def falling(self, speed):
        if self.rect.y != 600:
            self.rect.move_ip(0, speed)
        else:
            return False

    def left(self, speed):
        self.rect.move_ip(speed, 0)

    def right(self, speed):
        self.rect.move_ip(speed, 0)

