import pygame as pg

class Text:
    def __init__(self, text, text_color, pc_x, pc_y, font_size=32, font_family=None):
        self.text = str(text)
        self.text_color = text_color
        self.font_family = font_family
        self.font_size = font_size
        self.font = pg.font.Font("assets/Pixeltype.ttf", self.font_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.pc_x = pc_x
        self.pc_y = pc_y
        self.rect.topleft = pc_x, pc_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pc_x, self.pc_y