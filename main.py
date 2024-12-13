import pygame
from constants import *

BLACK = (0, 0, 0)

def main():
    # Initializing pygame 
    pygame.init()

    # GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        pygame.display.flip()
        # for event in pygame.event.get():
            # print(event)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()
