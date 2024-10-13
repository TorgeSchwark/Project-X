import pygame
from global_variables import *

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, text_color, text_size):
        self.text = text
        self.button_rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text_size = text_size

        self.button_font = pygame.font.SysFont('Comic Sans MS', self.text_size)
        self.text_surface = self.button_font.render(text, False, self.text_color)
        # screen.blit(text_surface, (0,0))

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        # Render button
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.button_rect)
        else:
            pygame.draw.rect(screen, self.color, self.button_re_colorct)


