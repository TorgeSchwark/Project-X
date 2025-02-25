import pygame

def main():
    pygame.init()
    
    # Fenstergröße
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Fenster")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((30, 30, 30))  # Hintergrundfarbe setzen
        pygame.display.flip()  # Bildschirm aktualisieren
    
    pygame.quit()

if __name__ == "__main__":
    main()

