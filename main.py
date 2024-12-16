from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# screen settings
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PING PONG GAME")
screen.tracer(0)
score = Scoreboard(screen)

r_paddle = Paddle(370,0)
l_paddle = Paddle(x =-370,y =0)
ball = Ball()

# keyboard user controls
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


is_on = True
while is_on:
    time.sleep(0.07)
    screen.update()
    ball.ball_move()

    #collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddle
    if (ball.distance(r_paddle) <50 and ball.xcor() >340) or (ball.distance(l_paddle) < 50 and ball.xcor() < - 340):
        ball.bounce_x()

    # r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_l()

    #l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_r()


    if score.r_score == 10 or score.l_score == 10:
        is_on = False
        score.game_over()

screen.exitonclick()
