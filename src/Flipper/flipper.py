from Flipper.ball import *

class Flipper:

    def __init__(self, size):
        self.window_size = size
        self.score = 0
        self.highscore = 0
        
        self.ball = Ball(size)

        self.player_left_stick_coords = [(self.window_size[0]*0.2,self.window_size[1]*0.8), (self.window_size[0]*0.2,self.window_size[1]*0.85), (self.window_size[0]*0.3,self.window_size[1]*0.9), (self.window_size[0]*0.3,self.window_size[1]*0.89)]


    def manage_inputs(self, events):
        pass

    def applie_physics(self):
        self.ball.apply_physics()
        
    def draw(self, screen):
        self.ball.draw(screen)
        pygame.draw.polygon(screen, (0, 255, 0), self.player_left_stick_coords)