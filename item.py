import pygame
class Item:
    items = []
    n = 0
    nameToNumber = {}
    def __init__(self,nom,**opt):
        self.nom = nom
        self.num = Item.n
        Item.n+=1
        Item.items.append(self)
        Item.nameToNumber[nom] = self.num
        if("texture" in opt):
            self.texture = pygame.image.load("assets/"+opt["texture"]).convert_alpha()
        else:
            self.texture = pygame.Surface((16,16)).convert_alpha()
            self.texture.fill((0,0,0,0))
