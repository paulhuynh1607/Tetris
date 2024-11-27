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
left = False
right = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    background.draw_grid(screen)
    if left:
        block.left(-30)
    elif right:
        block.right(30)
    else:
        isBlock = block.falling(30)

    left = False
    right = False
    block.draw(screen)

    time.sleep(tempo)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
