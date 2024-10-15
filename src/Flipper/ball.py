from global_variables import *
import pygame

class Ball:

    def __init__(self, size):
        self.window_size = size
        self.ball_color = WHITE
        self.ball_radius = self.window_size[0]/200
        self.x = 0
        self.y = 0
        self.moving = False
        self.direction = [2,2]
        self.acceleration = 5

    def apply_physics(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.ball_color, (self.x, self.y), self.ball_radius)
