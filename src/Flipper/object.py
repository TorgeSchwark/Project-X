import pygame

class Object:

    def __init__(self, x, y, width, height):
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None

    def set_image(self, image):
        self.image = pygame.transform.scale(pygame.image.load(image), (self.rect.width, self.rect.height))
    
    def draw(self):
        pass