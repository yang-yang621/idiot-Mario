import pygame as pg
from . import load_config


class Mario(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = load_config.GRAPHICS['mario_bros']
        self.facing = "right"
        self.dead = False
        self.walk_timer = 0
        self.x_vel = 0
        self.y_vel = 0
        self.load_image()
        self.frame_index = 0
        self.image = self.right_frames[0]
        self.rect = self.image.get_rect()
    

    def load_image(self):
        self.right_frames = []
        self.left_frames = []
        self.right_frames.append(self.get_image(178,32,12,16))
        self.right_frames.append(self.get_image(80,32,15,16))
        self.right_frames.append(self.get_image(96,32,16, 16))
        self.right_frames.append(self.get_image(112,32,16,16))
        self.right_frames.append(self.get_image(144,32,16,16))
        self.right_frames.append(self.get_image(130,32,14,16))
        self.right_frames.append(self.get_image(160,32,15,16))
        for f in self.right_frames:
            self.left_frames.append(pg.transform.flip(f,True,False))


    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,
                                   (int(rect.width*2.7),
                                    int(rect.height*2.7)))
        return image

    
    def update(self, key,info):
        self.current_time = info['CURRENT_TIME']
        self.move(key)


    def move(self, key):
        if key[pg.K_RIGHT]:
            self.walk(direction=True)
        elif key[pg.K_LEFT]:
            self.walk(direction=False)
        elif key[pg.K_UP]:
            self.jump(key)
        else:
            self.x_vel = 0

    
    def walk(self,direction):
        if direction:
            frames = self.right_frames
            self.x_vel = 5
        else:
            frames = self.left_frames
            self.x_vel = -5
        
        if self.frame_index == 0:
            self.frame_index += 1
            self.walk_timer = self.current_time
        else:
            if(self.current_time - self.walk_timer) < 100:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.walk_timer = self.current_time
        self.image = frames[self.frame_index]


    def jump(self, key):
        self.frame_index = 4