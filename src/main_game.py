import pygame
from global_variables import *
 
pygame.init()
 
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
pygame.display.set_caption('Project-X')
 
running = True
 
while running:
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False