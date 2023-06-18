import pygame as pg
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = None
        self.import_character_assets()
        self.frame_index = 0
        self.animations_speed = 0.2
        self.image = self.animations[0][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.power_up = False
        self.speed = 2

        self.direction = 0
        self.last_direction = 0

    def import_character_assets(self):
        self.animations = {0: [], 1: [], 2: [], 3: []}
        character_path = "assets/pacman/"
        for animation in self.animations.keys():
            full_path = character_path + str(animation)
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
            self.last_direction = self.direction
            self.direction = 0

        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.last_direction = self.direction
            self.direction = 1

        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.last_direction = self.direction
            self.direction = 2

        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.last_direction = self.direction
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.rect.centerx += self.speed
        elif self.direction == 1:
            self.rect.centerx -= self.speed
        elif self.direction == 2:
            self.rect.centery -= self.speed
        elif self.direction == 3:
            self.rect.centery += self.speed

    def update(self):
        self.get_input()
        self.animate()
        self.move()
