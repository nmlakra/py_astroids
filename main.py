import pygame
from player import Player
from constants import *


def main():
    # Initializing pygame 
    pygame.init()
    
    x_player_spwan_location = SCREEN_WIDTH / 2
    y_player_spwan_location = SCREEN_HEIGHT / 2
    player = Player(x_player_spwan_location, y_player_spwan_location)

    clock = pygame.time.Clock() 
    dt = 0
    # GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()
        # for event in pygame.event.get():
            # print(event)
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
