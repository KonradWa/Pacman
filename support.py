import os
import pygame as pg
from csv import reader, writer

screen_width = 28 * 16
screen_height = 35 * 16
tile_size = 16
pacman_start_pos = (432, 244)
sound_volume = 0.1
start_target = [(200, 128), (400, 64), (300, 128), (200, 64)]
current_level = 1


# Pobieranie zdjęć
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

# Pobieranie csv
def import_csv_save(path):
    terrain_map = []
    with open(path) as maps:
        level = reader(maps, delimiter=",")
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

# Rodzaje obiektów
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
level_2 = import_csv_save("level/map2.csv")

# Odczyt zakrętów
x = import_csv_save("level/zakret1.csv")
zakrety1 = []
for row_index, row in enumerate(x):
    for col_index, col in enumerate(row):
        if col == "1":
            zakrety1.append((col_index,row_index))
x = import_csv_save("level/zakret2.csv")
zakrety2 = []
for row_index, row in enumerate(x):
    for col_index, col in enumerate(row):
        if col == "1":
            zakrety2.append((col_index,row_index))

zakrety = {
    1:zakrety1,
    2:zakrety2
}

mapa = {
    1:level_1,
    2:level_2
}


