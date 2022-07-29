from turtle import *
speed(0)
side = 6
size = 150
pensize(5)
for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(6):
        pencolor('blue')
        forward(75)
        pencolor('red')
        circle(25)
        pencolor('blue')
        left(360/6)
        write(i, font=('Arial', 14, 'normal'))
    left(360/side)

mainloop()
