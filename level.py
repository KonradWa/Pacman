import pygame as pg
from support import *
from tile import *
from Ghost import *
from pleyer import Player
from text import Text


class Level:
    def __init__(self):
        self.player_pos = None
        self.tile = None
        # Sprites
        self.wall = pg.sprite.Group()
        self.point = pg.sprite.Group()
        self.stop = pg.sprite.Group()
        self.power_up = pg.sprite.Group()
        self.ghost = pg.sprite.Group()
        self.C = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        self.bg = pg.sprite.Group()
        self.life = pg.sprite.Group()
        # Create level
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display_surface = pg.display.set_mode((self.screen_width, self.screen_height))
        self.setup_level(level_1)
        # BG
        tile = BackGround()
        self.bg.add(tile)
        # Game attribute
        self.power_up_active = False
        self.counter = 0
        self.game = 0
        self.game_timer = 0
        self.ghost_timer = 0
        self.points = 0
        # Text
        self.points_display = []
        txt = Text("SCORE:", "white", 0, 0, 20)
        self.points_display.append(txt)
        txt = Text(f"{self.points}", "white", 0, 26, 20)
        self.points_display.append(txt)
        txt = Text(f"Level:", "white", 335, 0, 20)
        self.points_display.append(txt)
        txt = Text(f"001", "white", 390, 26, 20)
        self.points_display.append(txt)

    # Generowanie mapy
    def setup_level(self, layout):
        self.tile = []
        self.ghost_pos = [0,1,2,3]

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != "-1" and col != "9":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile_type = tile_types[col]
                    if tile_type == "Pacman":
                        player_sprite = Player((x, y))
                        self.player_pos = (x,y)
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
                        tile = Clyde(x, y, (300,64), 2, 2, False, False, 0, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                        self.ghost_pos[0] = (x,y)
                    elif tile_type == "Pink":
                        tile = Pinky(x, y, (300,64), 2, 2, False, False, 1, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                        self.ghost_pos[1] = (x,y)
                    elif tile_type == "Blue":
                        tile = Inky(x, y, (300,64), 2, 2, False, False, 2, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                        self.ghost_pos[2] = (x,y)
                    elif tile_type == "Red":
                        tile = Blinky(x, y, (300,64), 2, 2, False, False, 3, self.stop)
                        self.ghost.add(tile)
                        self.tile.append(tile)
                        self.ghost_pos[3] = (208,272)
                    elif tile_type == "Stop":
                        tile = Tile(x, y, tile_type)
                        self.stop.add(tile)
                        self.tile.append(tile)

    # Kolizje gracza za ścianą
    def player_wall_collision(self):
        player = self.player.sprite
        # Zawracanie
        for s in self.stop.sprites():
            if player.direction == 0 and player.rect.colliderect(s.rect):
                player.rect.centerx -= 2
            elif player.direction == 1 and player.rect.colliderect(s.rect):
                player.rect.centerx += 2
            elif player.direction == 2 and player.rect.colliderect(s.rect):
                player.rect.centery += 2
            elif player.direction == 3 and player.rect.colliderect(s.rect):
                player.rect.centery -= 2
        # Skręcanie
        for z in zakrety:
            if player.direction == 0 and player.rect.topleft[0] == z[0]*16 and player.rect.topleft[1] == z[1]*16:
                player.last_direction = player.direction
                player.direction = player.next_direction
            elif player.direction == 1 and player.rect.topleft[0] == z[0]*16 and player.rect.topleft[1] == z[1]*16:
                player.last_direction = player.direction
                player.direction = player.next_direction
            elif player.direction == 2 and player.rect.topleft[0] == z[0]*16 and player.rect.topleft[1] == z[1]*16:
                player.last_direction = player.direction
                player.direction = player.next_direction
            elif player.direction == 3 and player.rect.topleft[0] == z[0]*16 and player.rect.topleft[1] == z[1]*16:
                player.last_direction = player.direction
                player.direction = player.next_direction
        # Kolizja ze ścianą
        if player.direction == 0 and player.next_direction == 1:
            player.direction = player.next_direction
        elif player.direction == 1 and player.next_direction == 0:
            player.direction = player.next_direction
        elif player.direction == 2 and player.next_direction == 3:
            player.direction = player.next_direction
        elif player.direction == 3 and player.next_direction == 2:
            player.direction = player.next_direction

    # Kolizje gracza z duchami
    def player_ghost_collision(self):
        player = self.player.sprite
        # Zjadanie duchów
        if self.power_up_active:
            for g in self.ghost.sprites():
                if player.rect.colliderect(g.rect):
                    self.points += 200
                    g.dead = True
                    g.import_character_assets()
                    g.target = (224, 288)
        # Bicie gracza
        else:
            for g in self.ghost.sprites():
                if not g.dead:
                    tmp = 0
                    if player.rect.colliderect(g.rect):
                        player.life -= 1
                        tmp += 1
                    if tmp > 0:
                        player.rect.topleft = self.player_pos
                        for g in self.ghost.sprites():
                            g.target = (300,64)
                            self.ghost_timer = 0
                            g.x_pos = self.ghost_pos[g.id][0]
                            g.y_pos = self.ghost_pos[g.id][1]
                            g.direction = 2

    # Zbieranie punktów
    def eat_points(self):
        for p in self.point.sprites():
            if self.player.sprite.rect.collidepoint(p.rect.centerx, p.rect.centery):
                p.kill()
                self.points += 10

    # Zbieranie power up'ów
    def eat_power_up(self):
            for p in self.power_up.sprites():
                if self.player.sprite.rect.collidepoint(p.rect.centerx, p.rect.centery):
                    p.kill()
                    self.points += 50
                    self.power_up_active = True
                    self.player.sprite.power_up = True
                    for g in self.ghost.sprites():
                        g.power_up = True
                        g.import_character_assets()

    # Licznik trwania power up'a
    def power_up_counter(self):
        if self.counter > 300:
            self.player.sprite.power_up = False
            for g in self.ghost.sprites():
                g.power_up = False
                g.import_character_assets()
            self.power_up_active = False
            self.counter = 0
        self.counter += 1

    # Tworzenie licznika żyć
    def life_bar(self):
        x = 0
        for _ in range(self.player.sprite.life):
            self.life.add(Tile(x,544,"pacman/0"))
            x += 16

    # Ustawianie calu duchów
    def set_target(self):
        if self.ghost_timer >40:
            for g in self.ghost.sprites():
                if g.dead:
                    g.target = (256, 288)
                else:
                    g.target = self.player.sprite.rect.topleft
        self.ghost_timer += 1

    # Play, pause, restart
    def set_game(self):
        keys = pg.key.get_pressed()
        if self.game_timer <= 0:
            if keys[pg.K_SPACE] and self.game == 0:
                self.game = 1
                self.game_timer = 5
            elif keys[pg.K_SPACE] and self.game == 1:
                self.game = 2
                self.game_timer = 5
            elif keys[pg.K_SPACE] and self.game == 2:
                self.game = 1
                self.game_timer = 5
            elif keys[pg.K_SPACE] and (self.game == 3 or self.game == 4):
                self.game = 1
                self.power_up.empty()
                self.ghost.empty()
                self.point.empty()
                self.player.empty()
                self.points = 0
                self.setup_level(level_1)
                self.game_timer = 5

        else:
            self.game_timer -=1

    # Sprawdzanie śmierci
    def check_dead(self):
        if self.player.sprite.life == 0:
            self.game = 3

    # Sprawdzanie wygranej
    def check_win(self):
        counter = 0
        for _ in self.point.sprites():
            counter += 1
        if counter == 0:
            self.game = 4

    def run(self):
        self.check_win()
        self.check_dead()
        self.set_game()
        # Ekran gry
        if self.game == 1:
            # Silnik gry
            self.set_target()
            self.player_wall_collision()
            self.player_ghost_collision()
            self.eat_points()
            self.eat_power_up()
            if self.power_up_active:
                self.power_up_counter()
            # Rysowanie gry
            self.bg.draw(self.display_surface)
            self.life_bar()
            self.life.draw(self.display_surface)
            self.life.empty()
            self.point.draw(self.display_surface)
            self.power_up.draw(self.display_surface)
            self.ghost.draw(self.display_surface)
            self.player.draw(self.display_surface)
            # Aktualizacja pozycji
            self.ghost.update()
            self.player.update()

            # Aktualizacja punktów
            counter = 0
            for p in self.points_display:
                if counter == 1:
                    p.text = f"{self.points}"
                    p.update()
                p.draw(self.display_surface)
                counter += 1
        else:
            # Rysowanie
            self.bg.draw(self.display_surface)
            self.life_bar()
            self.life.draw(self.display_surface)
            self.life.empty()
            self.point.draw(self.display_surface)
            self.power_up.draw(self.display_surface)
            self.ghost.draw(self.display_surface)
            self.player.draw(self.display_surface)
            counter = 0
            for p in self.points_display:
                if counter == 1:
                    p.text = f"{self.points}"
                    p.update()
                p.draw(self.display_surface)
                counter += 1
            # Ekran startowy
            if self.game == 0:
                txt = Text(f"START", "yellow", 178, 320, 20)
            # Ekran pauzy
            elif self.game == 2:
                txt = Text(f"Paused", "yellow", 165, 320, 20)
            # Ekran przegranej
            elif self.game == 3:
                txt = Text(f"DEAD", "yellow", 185, 320, 20)
            # Ekran wygranej
            elif self.game == 4:
                txt = Text(f"WIN", "yellow", 195, 320, 20)
            txt.draw(self.display_surface)

