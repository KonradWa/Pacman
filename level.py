import pygame as pg
from support import *
from tile import *
from Ghost import *
from pleyer import Player


class Level:
    def __init__(self):
        # Sprites
        self.tile = None
        self.wall = pg.sprite.Group()
        self.point = pg.sprite.Group()
        self.stop = pg.sprite.Group()
        self.power_up = pg.sprite.Group()
        self.ghost = pg.sprite.Group()
        self.C = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        self.bg = pg.sprite.Group()
        # Create level
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display_surface = pg.display.set_mode((self.screen_width, self.screen_height))
        self.setup_level(level_1)
        # BG
        tile = BackGround()
        self.bg.add(tile)

        self.points = 0

    def setup_level(self, layout):
        self.tile = []

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != "-1" and col != "9":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile_type = tile_types[col]
                    if tile_type == "Pacman":
                        player_sprite = Player((x, y))
                        self.player.add(player_sprite)
                        self.tile.append(player_sprite)
                    if tile_type == "Point":
                        tile = Tile(x, y, tile_type)
                        self.point.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Power_up":
                        tile = Tile(x, y, tile_type)
                        self.power_up.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Yellow":
                        tile = Clyde(x, y, (100, 100), 1, tile_type, 2, False, False, 0, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Pink":
                        tile = Pinky(x, y, (100, 100), 1, tile_type, 2, False, False, 1, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Blue":
                        tile = Inky(x, y, (100, 100), 1, tile_type, 2, False, False, 2, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Red":
                        tile = Blinky(x, y, (100, 100), 1, tile_type, 2, False, False, 3, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                    elif tile_type == "Stop":
                        tile = Tile(x, y, tile_type)
                        self.stop.add(tile)
                        self.tile.append(tile)

    def player_wall_collision(self):
        player = self.player.sprite
        for s in self.stop.sprites():
            if player.direction == 0 and player.rect.colliderect(s.rect):
                player.direction = player.last_direction
                player.rect.centerx -= 2
            elif player.direction == 1 and player.rect.colliderect(s.rect):
                player.direction = player.last_direction
                player.rect.centerx += 2

            elif player.direction == 2 and player.rect.colliderect(s.rect):
                player.direction = player.last_direction
                player.rect.centery += 2

            elif player.direction == 3 and player.rect.colliderect(s.rect):
                player.direction = player.last_direction
                player.rect.centery -= 2

    def eat_points(self):
        for p in self.point.sprites():
            if self.player.sprite.rect.collidepoint(p.rect.centerx,p.rect.centery):
                p.kill()
                self.points += 10
    def run(self):
        player_x = self.player.sprite.rect.centerx
        player_y = self.player.sprite.rect.centery
        target = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]
        for g in self.ghost.sprites():
            g.target = target[g.id]

        self.player_wall_collision()
        self.eat_points()

        self.bg.draw(self.display_surface)
        self.point.draw(self.display_surface)
        self.power_up.draw(self.display_surface)
        self.ghost.draw(self.display_surface)
        self.player.draw(self.display_surface)

        self.ghost.update()
        self.player.update()

