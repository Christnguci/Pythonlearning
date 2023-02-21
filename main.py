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