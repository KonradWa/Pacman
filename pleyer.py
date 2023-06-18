import pygame as pg
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = None
        self.import_character_assets()
        self.frame_index = 0
        self.animations_speed = 0.2
        self.image = self.animations["RIGHT"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2

        self.direction = "RIGHT"

    def import_character_assets(self):
        self.animations = {"RIGHT": [], "LEFT": [], "UP": [], "DOWN": []}
        character_path = "assets/pacman/"
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.direction]
        self.frame_index += self.animations_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = "RIGHT"

        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = "LEFT"

        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = "UP"

        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = "DOWN"

    def move(self):
        if self.direction == "RIGHT":
            self.rect.centerx += self.speed
        elif self.direction == "LEFT":
            self.rect.centerx -= self.speed
        elif self.direction == "UP":
            self.rect.centery -= self.speed
        elif self.direction == "DOWN":
            self.rect.centery += self.speed

    def update(self):
        self.get_input()
        self.animate()
        self.move()
