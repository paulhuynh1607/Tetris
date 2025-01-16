import json
import pygame

pygame.font.init()


class HighScoreManager:
    def __init__(self, file_name="highscores.txt"):
        # File to store user highscores
        self.file_name = file_name
        self.highscores = self.load_highscores()

    def load_highscores(self):
        """Load highscores from a file."""
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_highscores(self):
        """Save highscores to a file."""
        with open(self.file_name, "w") as file:
            json.dump(self.highscores, file, indent=4)

    def add_score(self, username, score):
        """Add or update a user's high score."""
        if username in self.highscores:
            # Update high score if the new score is higher
            if score > self.highscores[username]:
                self.highscores[username] = score
                print(f"{username}'s new high score: {score}")
        else:
            # Add a new user with their score
            self.highscores[username] = score
            print(f"New high score for {username}: {score}")

        # Save highscores to the file
        self.save_highscores()

    def get_highscore(self):
        """Retrieve a user's high score."""
        self.highscores = dict(sorted(self.highscores.items(), key=lambda x: x[1], reverse=True))
        self.save_highscores()
        highest_score_user = list(self.highscores.keys())[0]
        return self.highscores.get(highest_score_user, 0)

    def display_all_highscores(self):
        """Display all user highscores."""
        print("Highscores:")
        for username in self.highscores:
            print(f"{username}: {self.highscores[username]}")


class Scoreboard:
    def __init__(self):
        self.username = "Default_Name"
        self.highscore_manager = HighScoreManager()
        self.highscore = self.highscore_manager.get_highscore()
        self.curr_score = 0
        self.color = (255, 255, 255)
        self.font = pygame.font.Font("freesansbold.ttf", size=20)
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (175, 50)

    def show_leaderboard(self):
        yes_or_no = input("Would you like to see the leaderboard? (yes or no) ").lower()
        if yes_or_no == "yes":
            self.highscore_manager.display_all_highscores()


    def ask_username(self):
        self.username = input("Please enter your username: ")

    def add_point(self, points):
        self.curr_score += points
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)

    def check_score(self):
        if self.curr_score > self.highscore:
            self.highscore = self.curr_score
            self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                         True, self.color)
            self.highscore_manager.add_score(self.username, self.highscore)

    def render(self, screen):
        """Render the scoreboard on the screen."""
        screen.blit(self.text, self.textRect)
