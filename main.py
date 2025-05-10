from pygame import *

win = display.set_mode((1500,1000))

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

class Platform(Sprite):
    def move(self,m_up,m_down):
        key_pressed = key.get_pressed()
        if key_pressed[m_up] and self.rect.y > 7:
                self.rect.y -= 7
        if key_pressed[m_down] and self.rect.y < 750:
                self.rect.y += 7

class Ball(Sprite):
    def __init__(self, image_p, x, y):
        super().__init__(image_p, x, y)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        if self.rect.y <= 0:
            self.speed_y *= -1
        elif self.rect.y >= 870:
            self.speed_y *= -1
        
        if sprite.collide_rect(self,platform1):
            self.speed_x *= -1
        elif sprite.collide_rect(self,platform2):
            self.speed_x *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        

ball = Ball(ball_sc,600,600)
platform1 = Platform(platform1_sc,100,500)
platform2 = Platform(platform2_sc,1200,500)

tick = time.Clock()
mod = 0
while mod == 0:
    for e in event.get():
        if e.type == QUIT:
            mod = 1
    win.fill((100,100,100))


    platform1.move(K_w,K_s)
    platform2.move(K_UP,K_DOWN)
    ball.move()

    ball.draw()
    platform1.draw()
    platform2.draw()



    tick.tick(60)
    display.update()