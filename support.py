import os
import pygame as pg
from csv import reader, writer

screen_width = 28 * 16
screen_height = 35 * 16
tile_size = 16
pacman_start_pos = (432, 244)


def import_folder(path):
    surface_list = []
    for _, __, image_files in os.walk(path):
        for image in image_files:
            if image == "desktop.ini":
                pass
            else:
                full_path = path + "/" + image
                image_surface = pg.image.load(full_path).convert_alpha()
                surface_list.append(image_surface)

    return surface_list


def import_csv_save(path):
    terrain_map = []
    with open(path) as maps:
        level = reader(maps, delimiter=",")
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


tile_types = {
    "0": ("Pacman"),
    "1": ("Yellow"),
    "2": ("Pink"),
    "3": ("Red"),
    "4": ("Blue"),
    "5": ("Power_up"),
    "6": ("Point"),
    "8": ("Stop")
}

level_1 = import_csv_save("level/map1.csv")

x = import_csv_save("level/zakret.csv")
zakrety = []
for row_index, row in enumerate(x):
    for col_index, col in enumerate(row):
        if col == "1":
            zakrety.append((col_index,row_index))
print(zakrety)

