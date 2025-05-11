from pygame import *

win = display.set_mode((1500,1000))

font.init()
ball_sc = image.load("ball.png")
platform1_sc = image.load("platform 1.png")
platform2_sc = image.load("platform 2.png")
font1 = font.Font(None,100)
font2 = font.Font(None,70)

count = 0
count_text = font2.render(f"Счёт: {count}",True,(29, 63, 87))
touch2 = 0
touch1 = 0

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
        global lose,lose_text,restart_text,count,count_text,touch1,touch2
        if self.rect.y <= 0:
            self.speed_y *= -1
        elif self.rect.y >= 870:
            self.speed_y *= -1
        
        if sprite.collide_rect(self,platform1):
            touch2 = 0
            if touch1 == 0:
                self.speed_x *= -1
                count += 1
                count_text = font2.render(f"Счёт: {count}",True,(29, 63, 87))
                touch1 += 1
        elif sprite.collide_rect(self,platform2):
            touch1 = 0
            if touch2 == 0:
                self.speed_x *= -1
                count += 1
                count_text = font2.render(f"Счёт: {count}",True,(29, 63, 87))
                touch2 += 1
        if self.rect.x <= 0:
            lose = 1
            lose_text = font1.render(f"Игрок {lose} проиграл",True,(0,0,0))
            restart_text = font1.render("Нажмите 'R' для перезапуска",True,(0,0,0))
        if  self.rect.x >= 1370:
            lose = 2
            lose_text = font1.render(f"Игрок {lose} проиграл",True,(255,0,0))
            restart_text = font1.render("Нажмите 'R' для перезапуска",True,(0,0,0))


        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        
        

ball = Ball(ball_sc,600,600)
platform1 = Platform(platform1_sc,100,500)
platform2 = Platform(platform2_sc,1200,500)

tick = time.Clock()
lose = None
mod = 0
while mod == 0:
    for e in event.get():
        if e.type == QUIT:
            mod = 1
        if lose == 1 or lose == 2:
            if e.type == KEYDOWN:
                if e.key == K_r:
                    ball = Ball(ball_sc,600,600)
                    platform1 = Platform(platform1_sc,100,500)
                    platform2 = Platform(platform2_sc,1200,500)
                    count = 0
                    count_text = font2.render(f"Счёт: {count}",True,(29, 63, 87))
                    lose = 0

    win.fill((100,100,100))


    platform1.move(K_w,K_s)
    platform2.move(K_UP,K_DOWN)
    ball.move()

    ball.draw()
    platform1.draw()
    platform2.draw()


    win.blit(count_text,(1250,40))
    if lose == 1 or lose == 2:
        win.blit(lose_text,(430,450))
        win.blit(restart_text,(270,900))


    tick.tick(60)
    display.update()