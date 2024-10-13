import pygame
from global_variables import *
from button import *
from bar import *

pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
pygame.display.set_caption('Project-X')
 
running = True

fonts = pygame.font.get_fonts()
print(fonts)

#but = Button("test", 300, 400, 100, 100, (255,255,255), (0,0,0), (100,100,100), 40)
bar = Bar(100,100, 200, 600, True, True, "V", (100,0,90))
bar.add_button("top", "Hello, World!")
bar.add_button("scrollable", "fick")
bar.add_button("scrollable", "dich!")
bar.add_button("scrollable", "dich!")
bar.add_button("bottom", "dich!")
while running:
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            bar.scrolling(-event.y*30)
    
    # Set the frame rate
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)
    bar.draw(screen)
    #but.draw(screen)

    pygame.display.update()