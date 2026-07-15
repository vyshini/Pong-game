from turtle import Turtle,Screen
import pandas as pd
import time
screen = Screen()
screen.title("India states game")
screen.setup(width=800, height=600)
image = "India-state.gif"

screen.addshape(image)
map_image = Turtle()
map_image.shape(image)

data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

width = screen.window_width()
height = screen.window_height()
timer_turtle =  Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.color("red")
timer_turtle.goto(width/2 - 20 , height/2 - 40)

time_left = 180
game_over = False

def countdown():
    global time_left,game_over

    if game_over :
        return
    timer_turtle.clear()
    timer_turtle.write(f"Time Left :{time_left}",align = "right",font = ("Arial",14,"bold"))
    if time_left >=0:
        time_left -= 1
        screen.ontimer(countdown,1000)
    else:
        game_over = True

countdown()
user_quit = False
while len(guessed_states) < 29 :
    answer_state = screen.textinput(title =f"{len(guessed_states)}/29 states correct",prompt= "Name the states in India")

    if answer_state is None:
        confirm = screen.textinput(title="Quit Game?",prompt="Do you want to quit the game? (yes/no)")
                                   
        if confirm and confirm.lower() == "yes":
            user_quit = True
            game_over = True
            break
        else:
            continue
        
    
   

    answer_state = answer_state.strip().title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0,240)

if user_quit:
    result_turtle.write(f"You quit the game.\nYou guessed {len(guessed_states)} / 29 states.",align="center",font=("Arial", 16, "bold"))
    
elif len(guessed_states) == 29:
    result_turtle.write("congragulations! you guessed all 29 states",align = "center",font = ("Arial",16,"bold"))
else:
    result_turtle.write(f"time's up ! you guessed {len(guessed_states)} out of 29 states",align = "center",font = ("Arial",16,"bold")) 

screen.exitonclick()






