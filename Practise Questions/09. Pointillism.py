import turtle as t
import colorgram
import random
t.colormode(255)
#create turtle
myturtle = t.Turtle()
#get colors from image
colors = colorgram.extract('images.jpg', 10)
colorlist = []
for c in colors:
    tu = (c.rgb[0], c.rgb[1] , c.rgb[2])
    colorlist.append(tu)
myturtle.up()
myturtle.goto(-250,-250)
myturtle.dot(10,'black')
myturtle.speed(20)
myturtle.hideturtle()

for _ in range(11):
    for _ in range(11):
        selectedcolor = random.choice(colorlist)
        myturtle.dot(20,(selectedcolor[0],selectedcolor[1],selectedcolor[2]))
        myturtle.forward(50)
    pos = myturtle.pos()
    myturtle.goto(-250, pos[1] + 50)


screen = t.Screen()
screen.mainloop()


