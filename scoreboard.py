import json
import pygame

pygame.font.init()


class HighScoreManager:
    def __init__(self, file_name="highscores.txt"):
        # Initialize with the file name to store highscores (default is "highscores.txt")
        self.file_name = file_name
        self.highscores = self.load_highscores()  # Load existing highscores from file

    def load_highscores(self):
        # Load highscores from a file.
        try:
            with open(self.file_name, "r") as file:
                # If file exists, load highscores as a dictionary
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is not found or is empty/corrupted, return an empty dictionary
            return {}

    def save_highscores(self):
        # Save highscores to a file.
        with open(self.file_name, "w") as file:
            # Write highscores to file in a readable JSON format
            json.dump(self.highscores, file, indent=4)

    def add_score(self, username, score):
        # Add or update a user's high score.
        if username in self.highscores:
            # Update high score if the new score is higher than the current high score
            if score > self.highscores[username]:
                self.highscores[username] = score
                print(f"{username}'s new high score: {score}")
        else:
            # Add a new user and their score if the username is not in the highscores
            self.highscores[username] = score
            print(f"New high score for {username}: {score}")

        # Save updated highscores to the file
        self.save_highscores()

    def get_highscore(self):
        # Retrieve the highest score from all users.
        # Sort highscores in descending order and get the highest score
        self.highscores = dict(sorted(self.highscores.items(), key=lambda x: x[1], reverse=True))
        self.save_highscores()
        highest_score_user = list(self.highscores.keys())[0]  # Get the user with the highest score
        return self.highscores.get(highest_score_user, 0)  # Return highest score (default 0 if no scores)

    def display_all_highscores(self):
        # Display all user highscores.
        print("Highscores:")
        # Iterate through all highscores and print them
        for username in self.highscores:
            print(f"{username}: {self.highscores[username]}")


class Scoreboard:
    def __init__(self):
        # Initialize the scoreboard with default values
        self.username = "Default_Name"  # Default username
        self.highscore_manager = HighScoreManager()  # Create an instance of HighScoreManager to manage highscores
        self.highscore = self.highscore_manager.get_highscore()  # Load the highest score
        self.curr_score = 0  # Current score starts at 0
        self.color = (255, 255, 255)  # White color for text
        self.font = pygame.font.Font("freesansbold.ttf", size=20)  # Set font for text rendering
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)  # Render the initial scoreboard text
        self.textRect = self.text.get_rect()  # Get the rectangle of the rendered text
        self.textRect.center = (175, 50)  # Set the text's position on the screen

    def show_leaderboard(self):
        # Ask the user if they want to see the leaderboard and display it if yes.
        yes_or_no = input("Would you like to see the leaderboard? (yes or no) ").lower()
        if yes_or_no == "yes":
            self.highscore_manager.display_all_highscores()  # Display all highscores

    def ask_username(self):
        # Ask the user to input their username.
        self.username = input("Please enter your username: ")

    def add_point(self, points):
        # Add points to the current score and update the scoreboard text.
        self.curr_score += points
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)

    def check_score(self):
        # Check if the current score is higher than the highscore and update it if necessary.
        if self.curr_score > self.highscore:
            self.highscore = self.curr_score
            self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                         True, self.color)
            # Update highscore and save it using HighScoreManager
            self.highscore_manager.add_score(self.username, self.highscore)

    def render(self, screen):
        # Render the current scoreboard on the Pygame screen.
        screen.blit(self.text, self.textRect)  # Draw the scoreboard text on the screen
