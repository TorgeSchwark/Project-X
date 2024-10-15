import pygame

class Player:
    
    def __init__(self):
        self.atack_speedms = 500
        self.last_atack_time = pygame.time.get_ticks()
        
        self.points_per_atack = 10