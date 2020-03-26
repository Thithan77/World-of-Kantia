import pygame
from math import *
from random import *
from tile import *
pygame.display.set_caption("World Of Kantia")
sol = pygame.image.load("assets/sprite_016.png").convert()
pierre = pygame.image.load("assets/sprite_007.png").convert()
vide = pygame.image.load("assets/sprite_186.png").convert()
arbre = pygame.image.load("assets/arbre.png").convert_alpha()
cailloux = pygame.image.load("assets/cailloux.png").convert_alpha()
perso = pygame.image.load("assets/perso.png").convert_alpha()

# Init tiles
Tile("sol",texture="sprite_016.png")
Tile("pierre",texture="sprite_007.png")
Tile("arbre",doPass=False,texture="arbre.png",dropItem=1)
Tile("cailloux",doPass=False,texture="cailloux.png",dropItem=2)
Tile("vide")

map = [0]*1000
surmap = [0]*1000
for i in range(999):
    map[i] = [0]*1000
    for j in range(999):
        map[i][j] = 0
chance = 30
for i in range(999):
    surmap[i] = [0]*1000
    for j in range(999):
        surmap[i][j] = 4
        if(i != 0):
            if(surmap[i-1][j] == 2):
                chance/=8
        if(j != 0):
            if(surmap[i][j-1] == 2):
                chance/=8
        if(floor(random()*chance) == 0):
                surmap[i][j] = 2
        chance = 30
        if(i != 0):
            if(surmap[i-1][j] == 3):
                chance/=8
        if(j != 0):
            if(surmap[i][j-1] == 3):
                chance/=8
        if(floor(random()*chance) == 0):
            surmap[i][j] = 3

        chance = 30
inv = [0]*10
surmap[1][1] = 2
