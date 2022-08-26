import pgzrun

HEIGHT = 500
WIDTH = 500

box1 = Rect((50, 50), (100,100))
box2 = Rect((300, 50), (100,100))
box3 = Rect((50, 350), (100,100))
box4 = Rect((350, 350), (100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box1, 'red')
    screen.draw.filled_rect(box2, 'yellow')
    screen.draw.filled_rect(box3, 'green')
    screen.draw.filled_rect(box4, 'blue')

def update():
    boxes_movement()

# custom function
def boxes_movement():
    box1.x += 2
    box2.y += 3
    box3.y += -3
    box4.x += -2

    if box1.x > WIDTH:
        box1.x = 0
    if box2.y > HEIGHT:
        box2.y = 0
    if box3.y < 0:
        box3.y = HEIGHT
    if box4.x < 0:
        box4.x = WIDTH

pgzrun.go()

