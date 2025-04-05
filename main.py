
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers before creating Player
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    # Create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    asteroid_field = AsteroidField()


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000

        # Update and draw
        updatable.update(dt)
        shots.update(dt)

        # Collision check
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over")
                pygame.quit()
                return
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split(asteroids)
                    shot.kill()
            
        screen.fill("black")
        for d in drawable:
            d.draw(screen)  # if draw() needs screen
        for shot in shots:
            shot.draw(screen)
            
        pygame.display.flip()



        

if __name__ == "__main__":
    main()