from circleshape import  *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.rect.center, self.radius, width=2)

    def split(self, asteroids):
        # Kill this asteroid because it's being destroyed
        self.kill()

        # If the asteroid is already too small, don't split it further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees for the split
        random_angle = random.uniform(20, 50)

        # Create two new velocities, rotated by random_angle and -random_angle
        velocity1 = self.velocity.rotate(random_angle)  # Rotate by random_angle
        velocity2 = self.velocity.rotate(-random_angle)  # Rotate by -random_angle

        # Compute new radius by subtracting ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two smaller asteroids with the new velocity and position
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    # Set the velocities and scale them up by 1.2 for added speed
        new_asteroid1.velocity = velocity1 * 1.2
        new_asteroid2.velocity = velocity2 * 1.2

    # Add the new asteroids to the asteroid group
        asteroids.add(new_asteroid1)
        asteroids.add(new_asteroid2)
