# This allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
      
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #FPS
    clock = pygame.time.Clock()

    #Initialize delta time variable
    dt = 0

    

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # Clear screen with black
        screen.fill("black")
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)
        # Update display
        pygame.display.flip()

        

if __name__ == "__main__":
    main()