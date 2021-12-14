import turtle as t

player_A_score = 0
player_B_score = 0

window = t.Screen()
window.title("Pong Game - by WMouton | l33th")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# create left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# create right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# create ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2

# create pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))
