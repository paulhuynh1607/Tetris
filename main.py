import pygame
from pygame.locals import *  # Import constants for key events
from blocks import Blocks  # Import the Blocks class
from GameLoadout import Background  # Import the Background class
from scoreboard import Scoreboard


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((360, 800))  # Create a window of size 500x700
pygame.display.set_caption("Tetris")  # Set the window title
clock = pygame.time.Clock()  # Create a clock to manage the frame rate
background = Background()  # Create an instance of the Background class
scoreboard = Scoreboard()
block = Blocks(background, scoreboard)  # Create an instance of the Blocks class
running = True  # Game loop control variable
dt = 0  # Delta time for frame updates

# Variables to track key states for continuous movement
move_left = False
move_right = False

timer = 0

# Main game loop
while running:
    # Clear the screen before drawing the frame
    screen.fill("black")  # Fill the screen with black color
    background.draw_grid(screen)  # Draw the game grid
    block.draw()  # Draw the current block
    block.setup()  # Update block anchor positions and setup
    if timer >= 1:
        block.falling()
        timer = 0

    # Handle events (key presses, key releases, quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            running = False
        if event.type == KEYDOWN:  # Handle key presses
            if event.key == K_LEFT:  # Move block left
                block.left()
            elif event.key == K_RIGHT:  # Move block right
                block.right()
            elif event.key == K_UP:  # Rotate block
                block.rotate()
            elif event.key == K_DOWN:  # Move block down faster
                block.down()

    # Check for game over condition
    if block.check_game_end():
        print("Game Over")  # Print game over message to console
        running = False  # Exit the game loop

    scoreboard.check_score()
    screen.blit(scoreboard.text, scoreboard.textRect)

    # Update the display with new frame content
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds for dt
    timer += dt

# Quit pygame when the game loop ends
pygame.quit()
