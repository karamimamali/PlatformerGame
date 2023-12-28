from os import listdir
from os.path import isfile ,join
import pygame 
from constants import *



def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, width, height, direction=False):
    path = join("assets", dir1)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []

        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_R"] = sprites
            all_sprites[image.replace(".png", "") + "_L"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_BG(name):
    image = pygame.image.load(join('assets','BG',name))
    _, _, width, height = image.get_rect()

    cordinates = []

    for i in range(wn_width//width+1):
        for j in range(wn_height//height+1):
            pos = (i*width, j*height)
            cordinates.append(pos)
    return cordinates, image


def get_block(width, height, x, y):
    path = join("assets", "BG", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    rect = pygame.Rect(x, y, width, height)
    surface.blit(image, (0, 0), rect)
    
    return pygame.transform.scale2x(surface)
    # return surface



