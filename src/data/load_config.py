import json
import pygame as pg
import os


def load_graphics(file_path,color_key = (255,0,255)):
    graphics = {}
    for pic in os.listdir(file_path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in [".png",".jpg","bmp"]:
            img = pg.image.load(os.path.join(file_path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(color_key)
            graphics[name] = img
    return graphics


def load_fonts(file_path):
    fonts = {}
    for f in os.listdir(file_path):
        name ,ext = os.path.splitext(f)
        if ext.lower() == ".ttf":
            fonts[name] = os.path.join(file_path,f)
    return fonts

f = open("./data/config.json", "r")
config = f.read()
config = json.loads(config)
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption("idiot-mario")
screen = pg.display.set_mode((config['SCREEN'][0]["HEIGHT"],config['SCREEN'][0]['WIDTH']))
screen_rect = screen.get_rect()

GRAPHICS = load_graphics(os.path.join("../resources","graphics"))
FONTS = load_fonts(os.path.join("../resources","fonts"))
