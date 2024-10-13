import pygame
from global_variables import *

class Button:
    def __inirext__(self, text, x, y, width, height, color, hover_color, text_color):
        
        
        self.text = text
        self.x = x
        self.y = y 
        self.width = width * WINDOW_WIDTH
        self.height = height * WINDOW_HEIGHT