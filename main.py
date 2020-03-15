from config import *
import pygame;
from pygame.locals import *;
pygame.init()
pygame.key.set_repeat(10, 30)
fen = pygame.display.set_mode((width, height))
from init import *;
from perso import *
from math import *
Miguel = Perso(fen)
lastTick = int(pygame.time.get_ticks())
font=pygame.font.Font(None, 24)
while cont:
    xmin = Miguel.pos["x"] - (width/2)
    xmax = Miguel.pos["x"] + (width/2)
    ymin = Miguel.pos["y"] - (height/2)
    ymax = Miguel.pos["y"] + (height/2)
    x = xmin
    y = ymin
    for i in range(26):
        yc = y%32
        for j in range(26):
            xc = x%32
            if(floor(xc)%10 == 1):
                fen.blit(pierre,(j*32-xc,i*32-yc))
            else:
                fen.blit(sol,(j*32-xc,i*32-yc))
            x+=32
        x = xmin
    # print(xmin,"",xmax)
    for event in pygame.event.get():
        if event.type == QUIT:
            cont = False;
        elif event.type == KEYDOWN:
            if event.key == K_w:
                Miguel.pos["x"] += 10
            elif event.key == K_s:
                Miguel.pos["y"] += 10
            elif event.key == K_f:
                print("xmin:"+str(xmin))
                print("xmax:"+str(xmax))
    time = int(pygame.time.get_ticks())-lastTick
    FPS = floor(1/(time*0.001));
    text = font.render("FPS:"+str(FPS),1,(255,255,255))
    fen.blit(text,(0,0))
    text = font.render("PosX:"+str(Miguel.pos["x"]),1,(255,255,255))
    fen.blit(text,(0,32))
    text = font.render("PosY:"+str(Miguel.pos["y"]),1,(255,255,255))
    fen.blit(text,(0,64))
    lastTick = int(pygame.time.get_ticks())
    Miguel.afficher()
    pygame.display.flip()
pygame.quit()
