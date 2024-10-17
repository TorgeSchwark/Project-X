import pygame
from global_variables import *
from pygame.locals import*

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, text_color, text_size, active=True):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text_size = text_size

        self.function = None
        self.active = active

        self.button_font = pygame.font.SysFont('arial', self.text_size)
        self.text_surface = self.button_font.render(text, False, self.text_color)
        # screen.blit(text_surface, (0,0))
        self.frame_image = None

    def draw(self, screen, mouse_not_clipped=True):
        mouse_pos = pygame.mouse.get_pos()
        # Render button
        if not self.active:
            return
        elif self.rect.collidepoint(mouse_pos) and mouse_not_clipped:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Render Text
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

        if self.frame_image != None:
            screen.blit(self.frame_image, (self.rect.x, self.rect.y)) 

    

    def set_frame_image(self, image):
        self.frame_image =  pygame.transform.scale(pygame.image.load(image), (self.rect.width, self.rect.height))

    def set_function(self, function):
        self.function = function

    def is_clicked_left(self):
        mouse_pos = pygame.mouse.get_pos()
        if not self.active:
            return
        elif self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: # Left click
                print("here")
                if self.function != None:
                    print("here as well")
                    self.function()