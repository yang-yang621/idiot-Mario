import sys
import pygame as pg
import data.control
from data.menu import Menu
from data import load_config, game

def main():
    prog = data.control.Control("main Capture")
    state_dict = {
        "main menu": Menu(),
        "game" : game.Game()
    }
    prog.setup(state_dict,"main menu")
    prog.run()


if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
