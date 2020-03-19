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
destroyingTime = 0
destroying = False
destroyingPlace = (0,0)
font=pygame.font.Font(None, 24)
while cont:
    xmin = Miguel.pos["x"] - (width/2) +32
    xmax = Miguel.pos["x"] + (width/2) +32
    ymin = Miguel.pos["y"] - (height/2) +32
    ymax = Miguel.pos["y"] + (height/2) +32
    x = xmin
    y = ymin
    for i in range(26):
        yc = y%32
        for j in range(26):
            xc = x%32
            if(floor(x/32) <= 0 or floor(y/32) <= 0):
                fen.blit(vide,(j*32-xc,i*32-yc))
            elif(map[floor(y/32)][floor(x/32)] == "s"):
                fen.blit(sol,(j*32-xc,i*32-yc))
            else:
                fen.blit(pierre,(j*32-xc,i*32-yc))
            if(floor(x/32) <= 0 or floor(y/32) <= 0):
                fen.blit(vide,(j*32-xc,i*32-yc))
            elif(surmap[floor(y/32)-1][floor(x/32)-1] == "a"):
                fen.blit(arbre,((j)*32-xc,(i)*32-yc))
            elif(surmap[floor(y/32)-1][floor(x/32)-1] == "c"):
                fen.blit(cailloux,((j)*32-xc,(i)*32-yc))
            x+=32
        x = xmin
        y+=32
    for event in pygame.event.get():
        if event.type == QUIT:
            cont = False;
        elif event.type == KEYDOWN:
            if event.key == K_w:
                Miguel.pos["y"] -= 10
            elif event.key == K_s:
                Miguel.pos["y"] += 10
            elif event.key == K_a:
                Miguel.pos["x"] -= 10
            elif event.key == K_d:
                Miguel.pos["x"] += 10
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                destroying = True
                destroyingPlace = (event.pos[0],event.pos[1])
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                destroying = False
                destroyingTime = 0
    time = int(pygame.time.get_ticks())-lastTick
    if(destroying):
        destroyingTime+=(int(pygame.time.get_ticks())-lastTick)
        x = destroyingPlace[0] + (Miguel.pos["x"] - (width/2))
        y = destroyingPlace[1] + (Miguel.pos["y"] - (height/2))
        if(surmap[floor(y/32)][floor(x/32)] == "a" and destroyingTime > 4000):
            xM = floor(Miguel.pos["x"]/32)
            yM = floor(Miguel.pos["y"]/32)
            xO = floor(x/32)
            yO = floor(y/32)
            d = sqrt((xO-xM)*(xO-xM)+(yO-yM)*(yO-yM))
            if(d < 4):
                surmap[floor(y/32)][floor(x/32)] = "v"
                inv[0]+=1;
        elif(surmap[floor(y/32)][floor(x/32)] == "c" and destroyingTime > 4000):
            xM = floor(Miguel.pos["x"]/32)
            yM = floor(Miguel.pos["y"]/32)
            xO = floor(x/32)
            yO = floor(y/32)
            d = sqrt((xO-xM)*(xO-xM)+(yO-yM)*(yO-yM))
            if(d < 4):
                surmap[floor(y/32)][floor(x/32)] = "v"
                inv[1]+=1;
    FPS = floor(1/(time*0.001));
    text = font.render("GAMEPLAY EXPERIMENTAL:",1,(255,255,255))
    fen.blit(text,(0,0))
    text = font.render("FPS:"+str(FPS),1,(255,255,255))
    fen.blit(text,(0,32))
    text = font.render("PosX:"+str(floor(Miguel.pos["x"]/32)),1,(255,255,255))
    fen.blit(text,(0,64))
    text = font.render("PosY:"+str(floor(Miguel.pos["y"]/32)),1,(255,255,255))
    fen.blit(text,(0,96))
    text = font.render("DestroyingTime:"+str(destroyingTime),1,(255,255,255))
    fen.blit(text,(0,96+32))
    lastTick = int(pygame.time.get_ticks())
    Miguel.afficher()
    pygame.draw.rect(fen,(0,0,150),((config.width-(10*32))/2,height-32,10*32,32))
    for i in range(10):
        text = font.render(str(inv[i]),1,(255,255,255))
        fen.blit(text,((config.width-(10*32))/2+(i*32),height-32))
    pygame.display.flip()
pygame.quit()
