import pygame
from flipper.objects import *

class Flipper:

  def __init__(self):
    self.window_size = [0,0]

    self.balls = [Ball((200,300), 30)]
    self.objects = [Polygon([(100,200),(200,200),(200,300),(100,300)])]

  def activate_game(self, window_size):
    self.window_size = (window_size[0]/16*7,window_size[1])
    pygame.display.set_mode(self.window_size)

  def draw(self, screen):

    self.apply_physics()

    for object in self.objects:
      object.draw(screen)

    for ball in self.balls:
      ball.draw(screen)

  def apply_physics(self):
    for ball in self.balls:
      ball.apply_physics()

  def manage_inputs(self, events):
    pass  
