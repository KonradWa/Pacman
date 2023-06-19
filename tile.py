import pygame as pg
from support import *

# Object tła
class BackGround(pg.sprite.Sprite):
    def __init__(self, lvl):
        super().__init__()
        self.properties = None
        self.image = pg.image.load("assets/bg/bg"+str(lvl)+".png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 48))

# Objeck
class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.properties = None
        self.frames = import_folder(f"assets/{name}")
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

