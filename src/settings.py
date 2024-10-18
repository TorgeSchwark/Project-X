import pygame
from global_variables import *
from pygame.locals import*
from bar import * 

class Settings:

    def __init__(self,x,y,width,height,background_color,text_color,text_size,save_func,dismiss_func,active=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.text_color = text_color
        self.text_size = text_size
        self.active = active

        # Title height and bottom bar position
        title_height = self.text_size * 4 + 10  # title height + margin
        bottom_bar_y = height * 0.85

        # Calculate the available space between title and bottom bar
        available_height = bottom_bar_y - title_height
        bar_height = available_height * 0.9  # Use 90% of the available height for the bars
        bar_y = title_height + (available_height - bar_height) // 2  # Center the bars vertically

        # Left and right bars centered between title and bottom bar
        self.left_bar = Bar(0, bar_y, width // 2, bar_height, "V", (50, 50, 50), BAR_STYLE_ONE)
        self.right_bar = Bar(width // 2, bar_y, width // 2, bar_height, "V", (50, 50, 50), BAR_STYLE_ONE)

        # Bottom bar remains in the same position
        self.bottom_bar = Bar(width * 0.7, bottom_bar_y, 430, height * 0.1, "H", (50, 50, 50), BAR_STYLE_ONE)

        self.to_draw = [self.left_bar, self.right_bar, self.bottom_bar]

        # Settings label
        font_titel = pygame.font.SysFont('arial', self.text_size*4)
        self.font_text = pygame.font.SysFont('arial', self.text_size)
        self.titel_surface = font_titel.render("Settings", False, self.text_color)

        # Settings options

        # Save and dismiss button
        self.bottom_bar.add_button("bottom", "Save")
        self.bottom_bar.set_function(save_func, "bottom", 0)
        self.bottom_bar.add_button("bottom", "Dismiss")
        self.bottom_bar.set_function(dismiss_func, "bottom", 1)
        

    def draw(self,screen):
        if not self.active:
            return
        # Draw background
        pygame.draw.rect(screen, self.background_color, self.rect)
        # Draw titel
        screen.blit(self.titel_surface, (self.rect.x + self.rect.width//2 - self.titel_surface.get_width()//2, self.rect.y + 10))
        # Draw bars
        for bar in self.to_draw:
            bar.draw(screen)

    def is_clicked_left(self):
        if not self.active:
            return
        for bar in self.to_draw:
            bar.is_clicked_left()

    def deactivate(self):
        self.active = False
        for bar in self.to_draw:
            bar.deactivate()

    def activate(self):
        self.active = True
        for bar in self.to_draw:
            bar.activate()
        