
import turtle
import winsound

# window setup

win = turtle.Screen()
win.title("Pong by @janhninini")
win.bgpic("bg.gif")
win.setup(width = 800, height = 600)
win.tracer(0)

# score
score_A = 0
score_B = 0

# paddle A
paddie = turtle.Turtle()
paddie.speed(0)
paddie.shape("square")
paddie.color("white")
paddie.shapesize(stretch_wid=5, stretch_len=1)
paddie.penup()
paddie.goto(-350,0)

# paddle B
baddie = turtle.Turtle()
baddie.speed(0)
baddie.shape("square")
baddie.color("white")
baddie.shapesize(stretch_wid=5, stretch_len=1)
baddie.penup()
baddie.goto(350,0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = -0.3

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 24, "bold"))


# functions
def paddie_up():
    y = paddie.ycor()
    y += 30
    if y <= 290:
        paddie.sety(y)

def paddie_down():
    y = paddie.ycor()
    y -= 30
    if y >= -290:
        paddie.sety(y)

def baddie_up():
    y = baddie.ycor()
    y += 30
    if y <= 290:
        baddie.sety(y)

def baddie_down():
    y = baddie.ycor()
    y -= 30
    if y >= -290:
        baddie.sety(y)


# keyboard bindings
win.listen()
win.onkeypress(paddie_up,"w")
win.onkeypress(paddie_down,"s")
win.onkeypress(baddie_up,"Up")
win.onkeypress(baddie_down,"Down")

# main game loop

while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()  < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write(f"Player A: {score_A}  Player B: {score_B}", align= "center", font=("Courier", 24, "bold"))
        winsound.PlaySound("Squish.wav", winsound.SND_ASYNC)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write(f"Player A: {score_A}  Player B: {score_B}", align= "center", font=("Courier", 24, "bold"))
        winsound.PlaySound("Squish.wav", winsound.SND_ASYNC)
       

    # paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < baddie.ycor() + 40 and ball.ycor() > baddie.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddie.ycor() + 40 and ball.ycor() > paddie.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
