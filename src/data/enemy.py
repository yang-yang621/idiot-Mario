import pygame as pg
from . import load_config

class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.set_up(x,y)

    
    def set_up(self,x,y):
        self.sheet = load_config.GRAPHICS["smb_enemies_sheet"]
        self.frames = []
        self.index = 0
        self.frames.append(
            self.get_image(0, 4, 16, 16))
        self.frames.append(
            self.get_image(30, 4, 16, 16))
        self.frames.append(
            self.get_image(61, 0, 16, 16))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))
        self.image = self.frames[1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,
                                   (int(rect.width*2.7),
                                    int(rect.height*2.7)))
        return image
