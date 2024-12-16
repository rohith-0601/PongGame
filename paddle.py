from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
    #paddle settings
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(x, y)

    # user controls for paddle
    def move_up(self):
        if self.ycor() <= 290:
            y = self.ycor()
            self.goto(self.xcor(),y+50)

    def move_down(self):
        if self.ycor() > -290:
            y = self.ycor()
            self.goto(self.xcor(),y-50)







