# After a long break, I decided to kick back and try my hand in Python.
# Code is a bit janky and has its problems here and there
# TODO:Add an actual interface. And for the love of God, something unique.
# 11/19/2021, ÖmEren

import turtle


wind = turtle.Screen()
wind.title("PNOG")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

paddle = turtle.Turtle()
paddle.shape("square")
paddle.speed(0)
paddle.color("green")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-350, 0)

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.speed(0)
paddle1.color("green")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(350, 0)

ball = turtle.Turtle()
ball.shape("square")
ball.speed(0)
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

bscore = 0
ascore = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(ascore, bscore), align="center", font={"Courier", 24, "normal"})


def moveaup():
    y = paddle.ycor()
    y += 40
    if y <= 300:
        paddle.sety(y)

def moveadow():
    y = paddle.ycor()
    y -= 40
    if y >= -300:
        paddle.sety(y)

def movebup():
    y = paddle1.ycor()
    y += 40
    if y <= 300:
        paddle1.sety(y)

def movebdow():
    y = paddle1.ycor()
    y -= 40
    if y >= -300:
        paddle1.sety(y)

wind.listen()
wind.onkeypress(moveaup, "w")
wind.onkeypress(movebup, "Up")
wind.onkeypress(moveadow, "s")
wind.onkeypress(movebdow, "Down")

while True:
    wind.update()

    if ball.xcor() >= 400:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        ascore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(ascore, bscore), align="center", font={"Courier", 24, "normal"})
    if ball.xcor() <= -400:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        bscore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(ascore, bscore), align="center", font={"Courier", 24, "normal"})

    if ball.ycor() >= 300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor() <= -300:
        ball.sety(-300)
        ball.dy *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle1.ycor()+40) and (ball.ycor() > paddle1.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() > -350 and ball.xcor() < -340 and (ball.ycor() < paddle.ycor()+40) and (ball.ycor() > paddle.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
