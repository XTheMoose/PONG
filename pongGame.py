import turtle
import time


#WINDOW SETUP

wn = turtle.Screen()
wn.title("Pong Game - By Tyler Dakers - 2022")
wn.bgcolor("black")
wn.setup(width=800, height=600, startx=0, starty=0)
wn.tracer(0)


#FUNCTIONS

#movement functions
def a_UP():
    y = paddle_A.ycor()
    y += 40
    paddle_A.sety(y)
def a_DOWN():
    y = paddle_A.ycor()
    y -= 40
    paddle_A.sety(y)

def b_UP():
    y = paddle_B.ycor()
    y += 40
    paddle_B.sety(y)
def b_DOWN():
    y = paddle_B.ycor()
    y -= 40
    paddle_B.sety(y)

#pen functions

def score_UP():
    pen.clear()
    pen.goto(-350,260)
    pen.write("Player A: {}".format(score_a), align= "left", font=("Arial", 24, "normal"))
    pen.goto(350, 260)
    pen.write("Player B: {}".format(score_b), align= "right", font=("Arial", 24, "normal"))
    pen.goto(0,10)

def clearUP():   #clears screen and rewrites score
    pen.clear()
    score_UP()

def popup():
    pen.write("POINT {}".format(point), align= "center", font=("Arial", 60, "bold"))
    time.sleep(0.3)
    clearUP()

def countdown():
    pen.write("Ready?", align= "center", font=("Arial", 60, "bold"))
    time.sleep(1)
    clearUP()
    pen.write("Go", align= "center", font=("Arial", 60, "bold"))
    time.sleep(0.8)
    clearUP()

def exitMenu():
    pasuecount + 1


#ACTOR SETUP

#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup()
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.goto(-350, 0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dX = 0.1
ball.dY = 0.1

#PEN
score_a = 0
score_b = 0
pasuecount = 0
point = " "

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,30)
pen.write("Welcome to PONG", align= "center", font=("Arial", 60, "bold"))
pen.goto(0,0)
pen.write("Player 1: W-Up, S-Down    Player 2: I-Up, K-Down", align= "center", font=("Arial", 20, "normal"))
pen.goto(0,-40)
pen.write("Mash the key to move faster. Holding the key does nothing", align= "center", font=("Arial", 20, "normal"))
time.sleep(10)
pen.clear()
pen.goto(0,0)
countdown()


#STARTUP SEQUENCE

#KEYBINDINGS

key_aUP = "w"
key_aDOWN = "s"
key_bUP = "i"
key_bDOWN = "k"

wn.listen()
wn.onkey(a_UP, key_aUP)
wn.onkey(a_DOWN, key_aDOWN)
wn.onkey(b_UP, key_bUP)
wn.onkey(b_DOWN, key_bDOWN)

#MAIN GAME LOOP

while True:
    wn.update()

    #BALL MOVEMENT
    ball.setx(ball.xcor()+ball.dX)
    ball.sety(ball.ycor()+ball.dY)
    
    #COUNTDOWN
    if pasuecount == 1:
        pasuecount = 0

        pen.goto(0,10)
        popup()
        time.sleep(0.2)
        popup()
        time.sleep(0.2)
        popup()
        time.sleep(0.7)
        countdown()

    #BORDERS

    #ball collision
    #top and bottom
    
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dY *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dY *= -1

    #right and left
    if ball.xcor() > 400:
        score_a += 1
        score_UP()
        ball.goto(0,0)
        ball.dX *= -1
        pasuecount = 1
        point = "A"
        paddle_A.goto(-350, 0)
        paddle_B.goto(350, 0)
    if ball.xcor() < -400:
        score_b += 1
        pen.goto(-350,260)
        score_UP()
        ball.goto(0,0)
        ball.dX *= -1
        pasuecount = 1
        point = "B"
        paddle_A.goto(-350, 0)
        paddle_B.goto(350, 0)

    #paddle collision
    if paddle_A.ycor() > 210:
        paddle_A.sety(210)
    elif paddle_B.ycor() > 210:
        paddle_B.sety(210)
    elif paddle_A.ycor() < -250:
        paddle_A.sety(-250)
    elif paddle_B.ycor() < -250:
        paddle_B.sety(-250)


    #PADDLE+BALL COLLISION
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50:
        ball.setx(-340)
        ball.dX *= -1
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50:
        ball.setx(340)
        ball.dX *= -1

    #WIN
    if score_a == 10:
        pen.clear()
        pen.write("Winner Player A", align= "center", font=("Arial", 60, "bold"))
        time.sleep(5)
        break
    elif score_b == 10:
        pen.clear()
        pen.write("Winner Player B", align= "center", font=("Arial", 60, "bold"))
        time.sleep(5)
        break
