from pygame import *
from random import randint

clock = time.Clock()
background = (100, 100, 100)
FPS = 60


windx = 700
windy = 500

window = display.set_mode((windx, windy))
window.fill(background)

playing = True
finsh = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

player = Player('platform.png', windx-60, windy/2, 10)
player2 = Player('platform.png', windx-690, windy/2, 10)
balls = Player('ball.png', windx/2, windy/2, 10)

speedx = 5
speedy = 5

while playing:
    for e in event.get():
        if e.type == QUIT:
            playing = False

    if not finsh:
        window.fill(background)
        player.update_l()
        player2.update_r()

        '''crash = sprite.spritecollide(player, monsters, True)
        for i in crash:
            health -= 1'''
        

        balls.rect.y += speedy
        balls.rect.x += speedx
        if balls.rect.y > windy - 50 or balls.rect.y < 0:
            speedy *= -1
        if sprite.collide_rect(player2, balls) or sprite.collide_rect(player, balls):
            speedy *= -1
            speedx *= -1

        balls.reset()
        balls.reset()
        player.reset()
        player2.reset()
        player.update()
        player2.update()
    display.update()
    clock.tick(FPS)
