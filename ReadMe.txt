# Build a Tetris Game
The program require at least python 3 to work, preferably the newest version of python 3
THe program have the minimum requirement of an external library call pygame
pygame can be downloaded on the computer using the instruction on this website https://www.pygame.org/news

When you run the program there will be a window popping off, that window will be where you play the tetris game
But at the start you will have to enter your username in the python command line
After hitting enter to confirm your username then switch to the window pop up earlier, and now you can play the game

How to play Tetris

The Game consist of a constantly falling block coming from the sky
Inside a 10x20 grid, where you will be able to move the block inside
On top of the grid there will 2 main numbers which is your current score and the highest score in the game

If the block reaches the ground or fall onto another block there will be a new block coming from the sky
You the player will have to move or rotate the block so that if all pixel on a horizontal line is filled with blocks
Then the game will clear the horizontal row and gives you 10 points
If you get a new highscore in the python console will say that you are getting a new highscore
The more point you gain, the faster the blocks will move down

To move the blocks in the game, you will need to press the up, down, left, right keys on your keyboard
The up key will rotate the falling block if the new rotation is not outside the grid or other blocks
The down key will move the falling block down faster if it doesn't touch another block or the grid
The left key will move the falling block to the left if it doesn't touch another block or the grid
The right key will move the falling block to the right if it doesn't touch another block or the grid

The game will go on forever until the user finally loses the game
by stacking blocks ontop of one another reaching where the blocks come from

When the game stop
the program will store the user highscore into the highscore.txt file
It will then ask the player if they would like to see the leaderboard, to see who have the highest highscore
and where they
Then the program will ask the user if they want to play the game again
if the user wants to play the game again
    the program will reset the user's score and rerun the program
Else
    The game will stop

If you are starting a new game and uses the same username as before
if you get a new highscore then it will be store under the same username as well inside highscore.txt file

Try to gain as many points as you can and have fun!
