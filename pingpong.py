from pygame import *
from random import randint

clock = time.Clock()
background = (100, 100, 100)
FPS = 60

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

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
point1 = 0
point2 = 0


while playing:
    for e in event.get():
        if e.type == QUIT:
            playing = False

    if not finsh:
        score = font1.render(f'{point1}', True, (255, 255, 255))
        score2 = font1.render(f'{point2}', True, (255, 255, 255))
        window.fill(background)
        player.update_l()
        player2.update_r()

        balls.rect.y += speedy
        balls.rect.x += speedx
        if balls.rect.y > windy - 50 or balls.rect.y < 0:
            speedy *= -1
        if sprite.collide_rect(player2, balls) or sprite.collide_rect(player, balls):
            speedx *= -1
        
        if balls.rect.x >= windx:
            point1 +=1
            balls.rect.x = windx/2
            balls.rect.y = windy/2


        if balls.rect.x <= 0:
            point2 +=1
            balls.rect.x = windx/2
            balls.rect.y = windy/2


        window.blit(score, (350, 0))
        window.blit(score2, (370, 0))
        balls.reset()
        balls.reset()
        player.reset()
        player2.reset()
        player.update()
        player2.update()
    display.update()
    clock.tick(FPS)
