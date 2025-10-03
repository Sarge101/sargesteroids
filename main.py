import pygame
from constants import *
from player import Player

def main():
    print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
     
    running = True
    while running:
        screen.fill((0, 0, 0))
        for drawable in drawable_group:
            drawable.draw(screen)
        updatable_group.update(dt)
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()

if __name__ == "__main__":
    main()
