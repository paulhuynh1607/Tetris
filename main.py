import pygame
from pygame.locals import *
from blocks import Blocks
from GameLoadout import Background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
block = Blocks()
background = Background()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                block.left(background)
            elif event.key == K_RIGHT:
                block.right(background)
            elif event.key == K_UP:
                block.rotate(background)
            elif event.key == K_DOWN:
                block.down(background)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    background.draw_grid(screen)
    block.draw(background)
    block.setup()

    if block.anchor_blockY >= 16:
        block.falling(0.3, background)
    else:
        block.falling(0.5, background)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()
