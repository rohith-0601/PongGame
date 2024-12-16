from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_l(self):
        self.l_score += 1
        self.update_score()

    def update_r(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.screen.title(f"{self.l_score} PING PONG GAME {self.r_score}")

    def game_over(self):
        if self.l_score == 10:
            self.write("Left player won",align = "center",font = ('Arial', 24, 'normal'))
        elif self.r_score == 10:
            self.write("Right player won", align="center", font=('Arial', 24, 'normal'))
        time.sleep(1)

