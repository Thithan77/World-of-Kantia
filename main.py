from config import *
import pygame;
from pygame.locals import *;
pygame.init()
pygame.key.set_repeat(10, 30)
fen = pygame.display.set_mode((width, height))
from init import *;
from perso import *
from math import *
from inv import *
Miguel = Perso(fen,perso)
lastTick = int(pygame.time.get_ticks())
tickCount = 0
destroyingTime = 0
destroying = False
destroyingPlace = (0,0)
font=pygame.font.Font(None, 24)
jaaj = 0
lastTickReal = pygame.time.get_ticks()
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
            else:
                yz = floor(y/32)
                xz = floor(x/32)
                texture = Tile.tiles[map[int(xz)][int(yz)]].texture
                #texture = Tile.tiles[0].texture
                fen.blit(texture,((j)*32-xc,(i)*32-yc))
            if(floor(x/32) <= 0 or floor(y/32) <= 0 or floor(x/32) <= 0 or floor(y/32) <= 0):
                fen.blit(vide,(j*32-xc,i*32-yc))
            else:
                texture = Tile.tiles[surmap[int(xz)-1][int(yz)-1]].texture
                fen.blit(texture,(j*32-xc,i*32-yc))
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
                #print(floor(destroyingPlace[0]/32),end="/")
                #print(floor(destroyingPlace[1]/32))
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                destroying = False
                destroyingTime = 0
    if(tickCount % 100 == 0):
        time = int(pygame.time.get_ticks())-lastTick
    if(destroying):
        destroyingTime+=(int(pygame.time.get_ticks())-lastTickReal)
        x = destroyingPlace[0] + (Miguel.pos["x"] - (width/2))
        y = destroyingPlace[1] + (Miguel.pos["y"] - (height/2))
        if(destroyingTime > 4000):
            xM = floor(Miguel.pos["x"]/32)
            yM = floor(Miguel.pos["y"]/32)
            xO = floor(x/32)
            yO = floor(y/32)
            d = sqrt((xO-xM)*(xO-xM)+(yO-yM)*(yO-yM))
            if(d < 4):
                if(Tile.tiles[surmap[floor(x/32)][floor(y/32)]].dropItem != "null"):
                    #inv[Tile.tiles[surmap[floor(x/32)][floor(y/32)]].dropItem]["n"] += 1
                    Inv.add(Item.items[Tile.tiles[surmap[floor(x/32)][floor(y/32)]].dropItem].nom,1)
                    surmap[floor(x/32)][floor(y/32)] = Tile.nameToNumber["vide"]
                    destroyingTime = 0

    if(time*0.001 != 0):
        if(tickCount % 100 == 0):
            FPS = floor(1/((time*0.001)/100));
        else:
            pass;
    else:
        FPS = 1
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
    Miguel.afficher()
    #pygame.draw.rect(fen,(0,0,150),((config.width-(10*32))/2,height-32,10*32,32))
    inventaire = pygame.Surface((48*10,48));
    for i in range(10):
        case = pygame.Surface((48,48))
        text = font.render(str(Inv.list[i]["n"]),1,(255,255,255))
        w,h = text.get_size()
        case.blit(text,(48-w,48-h))
        case.blit(Item.items[Item.nameToNumber[Inv.list[i]["type"]]].texture,(16,16))
        inventaire.blit(case,(i*48,0))
    w , h = inventaire.get_size()
    fen.blit(inventaire,(0,height-h))
    tickCount+=1
    lastTickReal = pygame.time.get_ticks()
    pygame.display.flip()
pygame.quit()
