from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x,y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.rect.center, self.radius, width=2)