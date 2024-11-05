# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clockObj = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    playerObj = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidFieldObj = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u_item in updateable:
            u_item.update(dt)

        for rock in asteroids:
            if rock.check_collision(playerObj):
                print("Game over!")
                raise SystemExit
            for bullet in shots:
                if bullet.check_collision(rock):
                    bullet.kill()
                    rock.split()
            
        screen.fill("black")

        for d_item in drawable:
            d_item.draw(screen)

        pygame.display.flip()
        dt = clockObj.tick(60) / 1000.0

    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()