import turtle as t
from turtle import Screen

from colorama.ansi import clear_screen

screen  = Screen()
myturtle = t.Turtle()

def goup():
    myturtle.forward(10)
def turnleft():
    myturtle.setheading(myturtle.heading() + 10)
def turnright():
    myturtle.setheading(myturtle.heading() - 10)
def goback():
    myturtle.back(10)
def clear():
    myturtle.clear()
    myturtle.up()
    myturtle.home()
    myturtle.down()

screen.listen()
screen.onkey(goup,'w')
screen.onkey(turnleft,'a')
screen.onkey(turnright, 'd')
screen.onkey(goback,'s')
screen.onkey(clear,'c')


screen.mainloop()
