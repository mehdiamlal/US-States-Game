from turtle import Turtle, Screen, penup
import pandas as pd
WINDOW_WIDTH = 730
WINDOW_HEIGHT = 495
STATES_DATA = pd.read_csv("../data/50_states.csv")

def show_name(name, coordinates):
    """Shows the name of the state at the given coordinates."""
    tt = Turtle()
    tt.hideturtle()
    tt.penup()
    tt.goto(coordinates)
    tt.write(name, True, align="center", font=("arial", 9, "normal"))

def create_states():
    """Creates a list of tuples in the following format: (state_name, x_coor, y_coor)."""
    state_names = STATES_DATA.state.tolist()
    x_coordinates = STATES_DATA.x.tolist()
    y_coordinates = STATES_DATA.y.tolist()
    coordinates = [] 

    for i in range(len(x_coordinates)):
        coordinates.append((state_names[i], x_coordinates[i], y_coordinates[i]))

    return coordinates
    

screen = Screen()
screen.addshape("../img/blank_states_img.gif")
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.title("US States Game")
turtle = Turtle()
turtle.shape("../img/blank_states_img.gif")

states = create_states()
show_name(states[0][0], states[0][1:])




screen.exitonclick()