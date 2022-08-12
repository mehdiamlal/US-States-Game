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
    
def check_state(str, lst):
    """Checks if the str string is a valid state."""
    formatted_str = str.title().strip()
    for i in lst:
        if i[0] == formatted_str:
            return i
    return []

screen = Screen()
screen.addshape("../img/blank_states_img.gif")
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.title("US States Game")
turtle = Turtle()
turtle.shape("../img/blank_states_img.gif")

states_list = create_states()

game_is_on = True
while game_is_on:
    answer = screen.textinput(title="US States Game", prompt="Enter the name of a state.")
    state = check_state(answer, states_list)
    if len(state) > 0:
        show_name(state[0], state[1:])
        states_list.remove(state)
    
    if len(states_list) == 0:
        game_is_on = False





screen.exitonclick()