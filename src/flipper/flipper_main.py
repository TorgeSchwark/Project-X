import pygame

class Flipper:

  def __init__(self):
    self.window_size = [0,0]

  def activate_game(self, windwo_size):
    self.window_size = (self.window_size[0]/16*7,self.window_size[1])
    pygame.display.set_mode(self.window_size)

  def draw(self, screen):
    pass

  def manage_inputs(self, events):
    pass