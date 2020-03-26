import pygame
class Tile:
    tiles = []
    n = 0
    nameToNumber = {}
    def __init__(self,nom,**opt):
        self.nom = nom
        self.num = Tile.n
        Tile.n+=1
        Tile.tiles.append(self)
        Tile.nameToNumber[nom] = self.num
        if("doPass" in opt):
            if(opt["doPass"] == True):
                self.doPass = True
        else:
            self.doPass = False

        if("doBreak" in opt):
            if(opt["doBreak"] == True):
                self.doBreak = True
            else:
                self.doBreak = False
        else:
            self.doBreak = False
        if("texture" in opt):
            self.texture = pygame.image.load("assets/"+opt["texture"]).convert_alpha()
        else:
            self.texture = pygame.Surface((32,32)).convert_alpha()
            self.texture.fill((0,0,0,0))
        if("dropItem" in opt):
            self.dropItem = opt["dropItem"]
        else:
            self.dropItem = "null"
