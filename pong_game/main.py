from turtle import Screen,Turtle
from paddle import Paddle 
from ball import Ball
import time
from scoreboard import Scoreboard
sc = Screen()
sc.bgcolor("black")
sc.setup(width = 800,height = 600)
sc.title("pong game")

sc.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkeypress(r_paddle.go_up,"Up")
sc.onkeypress(r_paddle.go_down,"Down")
sc.onkeypress(l_paddle.go_up,"w")
sc.onkeypress(l_paddle.go_down,"s")

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 : 
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

    WINNING_SCORE = 10

    if scoreboard.l_score == WINNING_SCORE:
        scoreboard.goto(0,0)
        scoreboard.write("LEFT PLAYER WINS!", align = "center",font=("courier",30,"normal"))
        game_is_on = False

    if scoreboard.r_score == WINNING_SCORE:
        scoreboard.goto(0,0)
        scoreboard.write("ROGHT PLAYER WINS!", align = "center",font=("courier",30,"normal"))
        game_is_on = False


sc.exitonclick()