import pygame as pg
from . import control,load_config
from . import mario,enemy,item

class Game(control.State):
    def __init__(self):
        super().__init__()

    
    def startup(self, current_time, persist):
        self.game_info = load_config.config['Menu']
        self.game_info['CURRENT_TIME'] = current_time
        self.game_info['MARIO_DEAD'] = False
        self.setup()

    
    def setup(self):
        self.background = load_config.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,(int(self.background_rect.width*2.7),int(self.background_rect.height*2.7)))
        self.background_rect = self.background.get_rect()
        self.level = pg.Surface((self.background_rect.width,self.background_rect.height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = load_config.screen.get_rect(bottom = self.level_rect.bottom)
        self.viewport.x = self.game_info['CAMERA_START_X']
        
        self.set_element()


    def set_element(self):
        self.mario = mario.Mario()
        self.mario.rect.x = self.viewport.x + 500
        self.mario.rect.bottom = self.game_info["GROUND"]
        ground_1 = item.Item(0,load_config.config['GROUND'], 2953, 60)
        enemy0 = enemy.Enemy(self.viewport.x + 200,self.game_info["GROUND"])
        enemy1 = enemy.Enemy(self.viewport.x + 600,self.game_info["GROUND"])
        self.enemies = pg.sprite.Group(enemy0,enemy1)
        self.all_element = pg.sprite.Group(self.mario,self.enemies)
    

    def draw_all(self,surface):
        self.level.blit(self.background, self.viewport, self.viewport)
        self.all_element.draw(self.level)
        #self.mario.draw(self.level)
        surface.blit(self.level, (0,0), self.viewport)


    def update(self,surface,keys,current_time):
        self.mario.update(keys, self.game_info)
        self.mario.rect.x += self.mario.x_vel
        if pg.sprite.spritecollideany(self.mario,self.enemies):
            self.mario.dead = True
            self.mario.kill()
        self.mario.rect.y += self.mario.y_vel
        if pg.sprite.spritecollideany(self.mario,self.enemies):
            pass
        self.draw_all(surface)