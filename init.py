import pygame
sol = pygame.image.load("assets/sprite_016.png").convert()
pierre = pygame.image.load("assets/sprite_007.png").convert()
vide = pygame.image.load("assets/sprite_186.png").convert()
map = [0]*100
for i in range(99):
    map[i] = "ssssssssssssssssssmmmmssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
print(len(map))
