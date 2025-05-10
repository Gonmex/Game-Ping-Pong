from pygame import *

win = display.set_mode((1500,1000))
win.fill((100,100,100))

ball_sc = image.load("ball.png")
platform1_sc = image.load("platform 1.png")
platform2_sc = image.load("platform 2.png")

class Sprite():
    def __init__(self,image_p,x,y):
        self.image_p = image_p
        self.rect = image_p.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        win.blit(self.image_p, (self.rect.x, self.rect.y))

ball = Sprite(ball_sc,600,600)
platform1 = Sprite(platform1_sc,100,500)
platform2 = Sprite(platform2_sc,1200,500)

tick = time.Clock()
mod = 0
while mod == 0:
    for e in event.get():
        if e.type == QUIT:
            mod = 1


    ball.draw()
    platform1.draw()
    platform2.draw()

    tick.tick(60)
    display.update()