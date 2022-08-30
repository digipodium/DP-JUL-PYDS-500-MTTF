import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 500

p = Actor('char1', pos= (WIDTH//2, HEIGHT//2))
e = Actor('char3', pos=(60,60))
c = Actor('gold_1')
c.x = randint(100, WIDTH-100) # c pos on x axis
c.y = randint(100, HEIGHT-100) # c pos on x axis

is_game_over = False
is_game_started = False

score = 0 
spd_p = 3
spd_e = 1

def draw():
    screen.fill('white')
    screen.draw.text(f'SCORE: {score}', (20,20))
    p.draw()
    e.draw()
    c.draw()

pgzrun.go()
