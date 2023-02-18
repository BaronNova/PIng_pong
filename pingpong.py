from pygame import *
from random import randint

clock = time.Clock()
background = (100, 100, 100)
FPS = 60


windx = 700
windy = 500
FPS = 30
lost = 0
win = 0
overheat = 0
health = 3


window = display.set_mode((windx, windy))
window.fill(background)

bullets = sprite.Group()

playing = True
finsh = False


while playing:
    for e in event.get():
        if e.type == QUIT:
            playing = False
    display.update()
    clock.tick(FPS)

