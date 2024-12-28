import pygame

pygame.font.init()


class Scoreboard:
    def __init__(self):
        self.highscore = 180
        self.curr_score = 0
        self.color = (255, 255, 255)
        self.font = pygame.font.Font("freesansbold.ttf", size=20)
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)
        self.textRect = self.text.get_rect().center = (50, 50)

    def add_point(self, points):
        self.curr_score += points
        self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                     True, self.color)

    def check_score(self):
        if self.curr_score > self.highscore:
            self.highscore = self.curr_score
            self.text = self.font.render(f"Highscore: {self.highscore} Your Score: {self.curr_score}",
                                         True, self.color)
