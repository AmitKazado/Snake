import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
SCOREBOARD_POSITION = (0, 270)
GAMEOVER_POSITION = (0, 50)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.highest_score = 0
        with open("highest_score.txt") as file:
            self.highest_score = int(file.read())
        self.create_scoreboard()
        self.update_scoreboard()

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.current_score} Highest Score: {self.highest_score}", False, ALIGNMENT, FONT)

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()

    def game_over(self):
        self.goto(GAMEOVER_POSITION)
        self.color("red")
        self.write(f"Game Over", False, ALIGNMENT, FONT)
        # self.clear()

    def reset(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
            with open("highest_score.txt", mode="w+") as file:
                file.write(f"{self.highest_score}")

        self.current_score = 0
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.update_scoreboard()
