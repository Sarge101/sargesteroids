import pygame
pygame.init()

from constants import *


def main():
    print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     
    running = True
    while running:
        # Clear the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()

if __name__ == "__main__":
    main()
