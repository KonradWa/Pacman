import pygame as pg
from support import *
from level import Level
import sys

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((41, 49, 65))
    level.run()

    pg.display.update()
    clock.tick(30)
