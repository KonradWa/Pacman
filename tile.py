import pygame as pg
from support import *


class BackGround(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.properties = None
        self.frames = import_folder("assets/bg")
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(0, 48))
        print("TEST")


class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.properties = None
        self.frames = import_folder(f"assets/{name}")
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

