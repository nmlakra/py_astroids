import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import *
from time import sleep
import sys


def main():
    # Initializing pygame
    pygame.init()

    font = pygame.font.SysFont(pygame.font.get_default_font(), 50)

    # Creating Groups for sprite management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    ## Asteroids ##
    # Adding Asteroid class to the sprite groups
    Asteroid.containers = (asteroids, updatable, drawable)

    ## Asteroid Field ##
    AsteroidField.containers = updatable
    astro_field = AsteroidField()

    ## Player ##
    # Adding Player class to the sprite groups
    Player.containers = (updatable, drawable)
    x_player_spwan_location = SCREEN_WIDTH / 2
    y_player_spwan_location = SCREEN_HEIGHT / 2
    player = Player(x_player_spwan_location, y_player_spwan_location)

    ## Shot ##
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    # GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Event loop
    playing = True
    while playing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable_object in updatable:
            updatable_object.update(dt)

        screen.fill(BLACK)
        for drawable_object in drawable:
            drawable_object.draw(screen)
            
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    asteroid.split()
                    bullet.kill()
                    
            if asteroid.collision_check(player):
                text = font.render("GAME OVER", True, WHITE)
                screen.blit(text, (x_player_spwan_location, y_player_spwan_location))
                playing = False
                

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

    sleep(5)

if __name__ == "__main__":
    main()
