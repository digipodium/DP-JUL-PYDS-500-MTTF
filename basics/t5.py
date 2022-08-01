from turtle import *

start = 300
goto(-150,-150)
while start > 0:
    forward(start)
    left(360/6)
    start -= 10
    
    write(start, font=('Arial', 8, 'normal'))

mainloop()