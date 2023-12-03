import os
import pygame as pg


class Control(object):
    def __init__(self,caption):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.caption = caption
        self.fps = 60
        self.finish = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None


    def setup(self, state_dict,start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]


    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.finish = True
        elif self.state.finish:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    
    def flip_state(self):
        pass


    def loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.finish = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)

    
    def run(self):
        while not self.finish:
            self.loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)


class State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.finish = False
        self.quit = False
        self.next = None
        self.previous = None
        self.presist = {}

    def get_event(self, event):
        pass

    def startup(self,current_time,presistant):
        self.start_time = current_time
        self.presist = presistant

    def cleanup(self):
        self.done = False
        return self.presist

    def update(self, surface, keys, current_time):
        pass