'Author: hernanda472@gmail.com'

import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow']
for x in range (180):
    turtle.pencolor(colors[x%5])
    turtle.width(x/50+5)
    turtle.forward(x)
    turtle.left(60)
