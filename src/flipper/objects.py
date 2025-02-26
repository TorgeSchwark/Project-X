import pygame

class Ball:

  def __init__(self, center, radius):
    self.center = center
    self.direction = [2,1]
    self.color = (255, 0, 0)
    self.radius = radius

  def apply_physics(self):
    self.center = [self.center[0]+self.direction[0], self.center[1]+self.direction[1]]

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, self.center, self.radius, 3)

class Polygon:

  def __init__(self, vertices):
    self.vertices = vertices
    self.color = (0, 255, 0)

  def apply_physics(self):
    pass

  def draw(self, screen):
    pygame.draw.polygon(screen, self.color, self.vertices, 0)