import sys
import pygame as pg
from data.control import Control


def main():
    prog = Control("main Capture")
    state_dict = {
        "main menu"
    }
    prog.run()


if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
