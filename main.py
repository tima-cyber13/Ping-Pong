from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, scale_x=65, scale_y=65):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (scale_x, scale_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
win = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("tennis-court.webp"), (win_width, win_height))

ball = GameSprite("tennis.png", 10, 10, 2, 200, 200)
racket1 = Player("i.webp", 50, 50, 3, 10, 100)
racket2 = Player("i.webp", 50, 50, 3, 690, 100)

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)
win1 = font.render('PLAYER 1 WIN!', True, (255, 215, 0))
win2 = font.render('PLAYER 2 WIN!', True, (255, 215, 0))

finish = False
game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    if finish == False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
