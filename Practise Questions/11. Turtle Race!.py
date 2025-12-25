import random
from turtle import Screen
import turtle as t

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'pink', 'black', 'green', 'blue']
listofturtles = []
x = -230
y = 150
for i in range(5):
    tut = t.Turtle(shape='turtle')
    tut.color(colors[i])
    tut.up()
    tut.goto(x,y- (50*(i)))
    listofturtles.append(tut)

name = screen.textinput("yo what's good?", "whats your name? ")
print('Hello', name, 'Race started!')
race_ongoing = True
winner_index = 0
while name !=None and race_ongoing:
    for tut in listofturtles:
        if tut.xcor() >= 220:
            race_ongoing = False
            winner_index += listofturtles.index(tut)
            break
        tut.forward(random.randint(1,10))

print(f'{colors[winner_index]} turtle won')


screen.mainloop()
