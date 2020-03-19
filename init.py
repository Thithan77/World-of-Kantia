import pygame
from math import *
from random import *
pygame.display.set_caption("World Of Kantia")
sol = pygame.image.load("assets/sprite_016.png").convert()
pierre = pygame.image.load("assets/sprite_007.png").convert()
vide = pygame.image.load("assets/sprite_186.png").convert()
arbre = pygame.image.load("assets/arbre.png").convert_alpha()
cailloux = pygame.image.load("assets/cailloux.png").convert_alpha()
map = [0]*1000
surmap = [0]*1000
for i in range(999):
    map[i] = "ssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
chance = 30
for i in range(999):
    surmap[i] = [0]*1000
    for j in range(999):
        surmap[i][j] = "v"
        if(i != 0):
            if(surmap[i-1][j] == "a"):
                chance/=8
        if(j != 0):
            if(surmap[i][j-1] == "a"):
                chance/=8
        if(floor(random()*chance) == 0):
                surmap[i][j] = "a"
        chance = 30
        if(i != 0):
            if(surmap[i-1][j] == "c"):
                chance/=8
        if(j != 0):
            if(surmap[i][j-1] == "c"):
                chance/=8
        if(floor(random()*chance) == 0):
            surmap[i][j] = "c"
        chance = 30
inv = [0]*10
