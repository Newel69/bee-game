import random
import pgzrun

WIDTH = 600
HEIGHT = 500
score = 0
game_over = False

bee = Actor("bumblebee")
bee.pos = 300,250

flower = Actor("flower")

def move_flower():
    flower.x = random.randint(50,550)
    flower.y = random.randint(50,450)

def draw():
    screen.blit("backround",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+ str(score),(50,50),fontsize = 50, color = "red")
    if game_over:
        screen.fill("blue")
        screen.draw.text("Final score:"+ str(score),center = (200,50), fontsize = 50, color = "white")

def times_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 3
    if keyboard.right:
        bee.x = bee.x + 3
    if keyboard.up:
        bee.y = bee.y - 3
    if keyboard.down:
        bee.y = bee.y + 3
    if bee.colliderect(flower):
        move_flower()
        score = score + 1

move_flower()
clock.schedule(times_up,20.0)
pgzrun.go()