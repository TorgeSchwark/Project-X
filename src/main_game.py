import pygame
from global_variables import *
from button import *
from bar import *
from frame_game import *

pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
pygame.display.set_caption('Project-X')
 
running = True

fonts = pygame.font.get_fonts()
# print(fonts)

#but = Button("test", 300, 400, 100, 100, (255,255,255), (0,0,0), (100,100,100), 40)
frame_game = FrameGame()

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
    # bar.draw(screen)
    #but.draw(screen)

    pygame.display.update()