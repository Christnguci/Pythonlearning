from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()


def move_forward():
    tim.forward(10)
    
#su dung listen in turtle to create moving using arrows
screen.listen() 
screen.onkey(key="space" ,fun=move_forward )


screen.exitonclick()   
#xin chao day la chao day 
#change git repo direction