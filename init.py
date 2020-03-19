import pygame
from math import *
from random import *
sol = pygame.image.load("assets/sprite_016.png").convert()
pierre = pygame.image.load("assets/sprite_007.png").convert()
vide = pygame.image.load("assets/sprite_186.png").convert()
arbre = pygame.image.load("assets/arbre.png").convert_alpha()
cailloux = pygame.image.load("assets/cailloux.png").convert_alpha()
map = [0]*1000
surmap = [0]*1000
for i in range(999):
    map[i] = "ssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
for i in range(999):
    surmap[i] = [0]*1000
    for j in range(999):
        surmap[i][j] = "v"
        if(floor(random()*30) == 0):
            surmap[i][j] = "a"
        elif(floor(random()*30) == 0):
            surmap[i][j] = "c"
inv = [0]*10
