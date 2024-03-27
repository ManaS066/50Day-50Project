import turtle
import pandas as pd

screen = turtle.Screen()
tim = turtle.Turtle()
screen.title("US State game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# used to get the location of every state . ,but we have the data already.

# def get_mouseclick(x,y):
#     print(x,y)
# #fetch the cordinarte of the screen where the user clicked
# turtle.onscreenclick(get_mouseclick)
# # used to conntinue after click on sccreen
# turtle.mainloop()
guess_state = []

state_data = pd.read_csv("50_states.csv")
all_state = state_data.state.to_list()
while len(guess_state) < 50:
    ans_text = screen.textinput(title=f"{len(guess_state)}/50 state", prompt="Type the state name !").title()
    guess_state.append(ans_text)
    if ans_text == "Exit":
        missing_state = [state for state in all_state if state not  in guess_state]
        # for state in all_state:
        #     if state not in guess_state:
        #         missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing_state.txt")
        print(missing_state)
        break
    if ans_text in all_state:
        tim.hideturtle()
        tim.penup()
        statedata = state_data[state_data.state == ans_text]
        tim.goto(int(statedata.x.iloc[0]), int(statedata.y.iloc[0]))
        tim.write(f"{ans_text} ", align="center", font=("Arial", 8, "normal"))
