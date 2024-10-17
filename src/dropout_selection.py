import pygame
from global_variables import *
from pygame.locals import*

class DropoutSelection:

    def __init__(self, text, x, y, width, height, color, hover_color, text_color, text_size, options, option_height=30, active=True):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text_size = text_size
        self.options = options
        self.option_height = option_height
        self.active = active

        self.button_font = pygame.font.SysFont('arial', self.text_size)
        self.text_surface = self.button_font.render(text, False, self.text_color)

        self.frame_image = None
        self.selected_option = None

        # Track of dropdown state
        self.dropdown_open = False
        self.option_rects = self.create_option_rects()

    def create_option_rects(self):
            option_rects = []
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height + i*self.option_height, self.rect.width, self.option_height)
                option_rects.append(option_rect)
            return option_rects
    
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

        # Render dropdown options
        if self.dropdown_open:
            for i, option_rect in enumerate(self.option_rects):
                option_text = self.options[i]
                option_surface = self.button_font.render(option_text, False, self.text_color)

                if option_rect.collidepoint(mouse_pos) and mouse_not_clipped:
                    pygame.draw.rect(screen, self.hover_color, option_rect)
                else:
                    pygame.draw.rect(screen, self.color, option_rect)
                
                # Render Text for option
                screen.blit(option_surface, option_rect)
        
        if self.frame_image != None:
            screen.blit(self.frame_image, (self.rect.x, self.rect.y))

    def set_frame_image(self, image):
        self.frame_image =  pygame.transform.scale(pygame.image.load(image), (self.rect.width, self.rect.height))

    def is_clicked_left(self):
        mouse_pos = pygame.mouse.get_pos()
        if not self.active:
            return
        elif self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: # Left click
                self.dropdown_open = not self.dropdown_open
        
        # Check if an option was selected
        elif self.dropdown_open:
            for i, option_rect in enumerate(self.option_rects):
                if option_rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        self.selected_option = self.options[i]
                        self.dropdown_open = False
                        break
                
    def get_selected_option(self):
        return self.selected_option