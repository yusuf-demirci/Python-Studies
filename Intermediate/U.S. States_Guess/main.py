import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()
correct_answers = 0
correct_answer_list = []

while correct_answers != 50:
    answer = screen.textinput(title=f"{correct_answers}/50 States Correct",
                              prompt="What's the name of next state?").title()
    data = pandas.read_csv("50_states.csv")

    if answer == "Exit":
        break
    if answer in list(data.state):
        answer_list = data[data.state == answer]
        x_cor = int(answer_list.x)
        y_cor = int(answer_list.y)
        t.goto(x_cor, y_cor)
        t.write(answer)

        correct_answer_list.append(answer)
        correct_answers += 1

unknown_states = [state for state in data.state if state not in correct_answer_list]

output = pandas.DataFrame(unknown_states)
output.to_csv("Missing States.csv")
