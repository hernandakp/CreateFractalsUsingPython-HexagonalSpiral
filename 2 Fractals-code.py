'Author: hernanda472@gmail.com'

import turtle
colors = ['red', 'purple', 'blue', 'green']
for x in range (90):
    turtle.pencolor(colors[x%4])
    turtle.width(x/20+1)
    turtle.forward(x)
    turtle.left(60)
