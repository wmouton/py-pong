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
