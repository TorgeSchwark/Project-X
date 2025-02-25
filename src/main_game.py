import pygame
from global_variables import *
from button import *
from bar import *
from frame_game import *

pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
    
initial_window_width = 1600
initial_window_height = 900

frame_game = FrameGame((initial_window_width, initial_window_height))

screen = pygame.display.set_mode((initial_window_width, initial_window_height))
 
pygame.display.set_caption('Project-X')
 
running = True

fonts = pygame.font.get_fonts()

while running:
    # seems like this function can only be called once every itteration. otherwise buggy
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
    # Set the frame rate
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)
    frame_game.manager(screen, events)


    pygame.display.update()