from . import control,load_config
import pygame as pg

class Menu(control.State):
    def __init__(self):
        super().__init__()
        self.persist = load_config.config["Menu"]
        self.game_info = load_config.config["Menu"]
        self.elements = self.setup_elements()
    

    def setup_elements(self):
        level_1 = pg.transform.scale(load_config.GRAPHICS['level_1'],(
            int(load_config.GRAPHICS['level_1'].get_rect().width * 2.5),
            int(load_config.GRAPHICS['level_1'].get_rect().height* 2.5)
            )
        )
        backgound = level_1
        viewport = load_config.screen.get_rect(bottom = load_config.screen_rect.bottom)
        (game_name_image ,game_name_rect) = self.get_image(1,60,176,88,(170,100),load_config.GRAPHICS['title_screen'])

        cursor = pg.sprite.Sprite()
        dest = (220,358)
        cursor.image,cursor.rect = self.get_image(24,160,8,8,dest,load_config.GRAPHICS['item_objects'])
        cursor.state = "Play Game"

        return [backgound, viewport, game_name_image,game_name_rect, cursor]

    
    def get_image(self, x, y, width, height, dest, sprite_sheet):
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet,(0, 0), (x, y, width, height))
        if sprite_sheet == load_config.GRAPHICS['title_screen']:
            image.set_colorkey((255,0,220))
            image = pg.transform.scale(
                image,
                (
                    (int(rect.width * 2.5),
                    int(rect.height * 2.5))
                )
            )
        else:
            image.set_colorkey((0, 0, 0))
            image = pg.transform.scale(
                image,
                (int(rect.width * 3),
                int(rect.height * 3))
            )
        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return image, rect

    
    def draw(self, surface):
        surface.blit(self.elements[0], self.elements[1], self.elements[1])
        surface.blit(self.elements[4].image, self.elements[4].rect)
        surface.blit(self.elements[2], self.elements[3])
        #self.overhead_info.draw(surface)


    def update(self,surface, keys, current_time):
        self.current_time = current_time
        self.game_info['current time'] = self.current_time
        #self.overhead_info.update(self.game_info)
        self.elements[4].rect.y = 358
        self.draw(surface)