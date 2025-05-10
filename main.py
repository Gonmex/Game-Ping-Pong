from pygame import *

win = display.set_mode((1500,1000))
win.fill((100,100,100))

tick = time.Clock()
mod = 0
while mod == 0:
    for e in event.get():
        if e.type == QUIT:
            mod = 1




    tick.tick(60)
    display.update()