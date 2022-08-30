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
    if not is_game_started and not is_game_over:
        show_intro_screen()
    elif is_game_started and not is_game_over: 
        show_game_screen()
    elif is_game_over:
        show_game_over_screen()

def show_intro_screen():
    screen.fill('yellow')
    screen.draw.text('My Game',center=(WIDTH//2, HEIGHT//2), color='red',fontsize=100)
    screen.draw.text('Press space to start', center=(WIDTH//2, HEIGHT//2+50),color='red')

def show_game_screen():
    screen.fill('white')
    screen.draw.text(f'SCORE: {score}', (20,20), color='red')
    p.draw()
    e.draw()
    c.draw()

def show_game_over_screen():
    screen.fill('red')
    screen.draw.text('GAME OVER',center=(WIDTH//2, HEIGHT//2), color='yellow',fontsize=100)
    screen.draw.text(f'score : {score}', center=(WIDTH//2, HEIGHT//2+50),color='yellow')

def update():
    global is_game_started
    if keyboard.SPACE and not is_game_started:
        is_game_started = True
    if is_game_started and not is_game_over:
        enemy_movement()
        player_controls()
        check_score()
    



def enemy_movement():
    global is_game_over
    if p.x > e.x:
        e.x += spd_e
    if p.y > e.y:
        e.y += spd_e
    if p.x < e.x:
        e.x -= spd_e
    if p.y < e.y:
        e.y -= spd_e
    if p.colliderect(e):
        p.image = 'splat'
        is_game_over = True

def check_score():
    global score
    if p.colliderect(c):
        score += 10
        c.pos = (randint(0, WIDTH), randint(0, HEIGHT) )
        sounds.s1.play()

def player_controls():
    if keyboard.UP and not p.top < 0:
        p.y += -spd_p
        p.angle = 0 
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += spd_p
        p.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        p.x += -spd_p
        p.angle = 10
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += spd_p
        p.angle = -10
    else:
        p.angle = 0


pgzrun.go()
