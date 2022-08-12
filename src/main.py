from turtle import Turtle, Screen
WINDOW_WIDTH = 730
WINDOW_HEIGHT = 495

screen = Screen()
screen.addshape("../img/blank_states_img.gif")
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.title("US States Game")
turtle = Turtle()
turtle.shape("../img/blank_states_img.gif")



screen.exitonclick()