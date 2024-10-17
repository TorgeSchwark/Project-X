import pygame
from global_variables import *
from pygame.locals import*

class Settings:

    def __init__(self,x,y,width,height,background_color,text_color,text_size,active=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.text_color = text_color
        self.text_size = text_size
        self.active = active

        self.left_bar = None
        self.right_bar = None
        self.bottom_bar = None

        self.to_draw = []

        # Settings label
        font_titel = pygame.font.SysFont('arial', self.text_size*4)
        self.font_text = pygame.font.SysFont('arial', self.text_size)
        self.titel_surface = font_titel.render("Settings", False, self.text_color)

    def draw(self,screen):
        if not self.active:
            return
        # Draw background
        pygame.draw.rect(screen, self.background_color, self.rect)
        # Draw titel
        screen.blit(self.titel_surface, (self.rect.x + self.rect.width//2 - self.titel_surface.get_width()//2, self.rect.y + 10))

    def is_clicked_left(self):
        pass

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True
        