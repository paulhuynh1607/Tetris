import pygame
from pygame.locals import *
from blocks import Blocks
from GameLoadout import Background
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
block = Blocks()
background = Background()
running = True
dt = 0
tempo = 0.6
isFalling = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            isFalling = False
            if event.key == K_LEFT:
                block.left(background)
            if event.key == K_RIGHT:
                block.right(background)
        else:
            isFalling = True
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    background.draw_grid(screen)
    block.draw(background)
    if isFalling:
        block.falling(0.5, background)

    left = False
    right = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
