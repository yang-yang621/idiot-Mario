import control,load_config

class Menu(control.State):
    def __init__(self):
        control.State.__init__(self)
        self.persist = load_config.config["Menu"]
        self.game_info = load_config.config["Menu"]
        self.next = 
        self.setup_background()
    

    def setup_background(self):
        pass

    
    def setup_mario(self):
        pass


    def setup_cursor(self):
        pass
