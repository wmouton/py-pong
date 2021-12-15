import turtle as t

player_A_score = 0
player_B_score = 0

window = t.Screen()
window.title("Pong Game - by WMouton | l33th")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# create left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# create right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# create ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ball_x_direction = 0.2
ball_y_direction = 0.2

# create pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))


# moving the left paddle
def left_paddle_up():
    y = left_paddle.ycor()
    y = y + 90
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y = y - 90
    left_paddle.sety(y)


# moving the right paddle
def right_paddle_up():
    y = right_paddle.ycor()
    y = y + 90
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y = y - 90
    right_paddle.sety(y)


# assign keys to play
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball_x_direction)
    ball.sety(ball.ycor() + ball_y_direction)

    # set up border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y_direction = ball_y_direction * -1
    if ball.ycor() > -290:
        ball.sety(-290)
        ball_y_direction = ball_y_direction * -1
