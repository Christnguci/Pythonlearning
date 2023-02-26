from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_left():
    #using heading function to colect the orientation 
    x=tim.heading()
    #setheading function to get orientation each clicking turn
    tim.setheading(x+10)

def move_right():
    x=tim.heading()
    tim.setheading(x-10)
def clear():
    tim.reset()

    
#su dung listen in turtle to create moving using arrows
#moving c
screen.listen() 
screen.onkey(key="w" ,fun=move_forward)
screen.onkey(key="s" ,fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear)


screen.exitonclick()   
#xin chao day la chao day 
#change git repo direction
#create a Turtles race using Turtle
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color")

Turtles=[]
for turtle in  range(5):
    turtle=Turtle()
    turtle.shape("turtle")
    Turtles.append(turtle)

colors=["red","green","blue","pink","black"]
default=100
for i in range(len(Turtles)):
    Turtles[i].color(colors[i])
    Turtles[i].penup()
    Turtles[i].goto(-230,default)
    Turtles[i].pendown()
    default-=50
if user_bet :
    is_race_on=True
import random
distance=0
while is_race_on:
    for i in range(len(Turtles)):
        random_step=random.randint(1,10)
        Turtles[i].forward(random_step)
        Turtles[i].clear()
    distance+=10
    if distance==1000:
        is_race_on=False

    
        
Max=float(0)
for i in range(len(Turtles)):
    pros=Turtles[i].pos()
    if pros[0] > Max :
        Max=pros[0]

for i in range(len(Turtles)):
    pros=Turtles[i].pos()
    if Max==pros[0]:
        if user_bet==Turtles[i].pencolor():
            print("You win !")
        else:
            print(f"You loose, the winning turtle is {Turtles[i].pencolor()}")

screen.exitonclick()

