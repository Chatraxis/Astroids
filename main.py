import pygame
from constants import *
from player import *
from astroid import *
from asteroidfield import *



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    number = 1
    
    time = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    astroids =  pygame.sprite.Group()
    
    AsteroidField.containers = (updateable)
    Asteroid.containers = (drawable, updateable, astroids)
    Player.containers = (drawable, updateable)
    P1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AF = AsteroidField()


    while number != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        updateable.update(dt)
        for astr in astroids:
            if P1.collision(astr):
                print("Game Over!")
                raise SystemExit

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = time.tick(60)/1000
        
if __name__ == "__main__":
    main()
