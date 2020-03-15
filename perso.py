import pygame;
import config;
class Perso(object):
    def __init__(self,fen):
        self.pos = {};
        self.pos["x"] = config.width/2+20;
        self.pos["y"] = config.height/2+20;
        self.fen = fen
    def afficher(self):
        pygame.draw.rect(self.fen,(255,0,150),(config.width/2,config.height/2,20,20))
