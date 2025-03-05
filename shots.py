import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        shot_color = (255, 0, 0)  # Red color for the shot
        pygame.draw.circle(self.image, shot_color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.position)
        print(f"Shot initialized at {self.position} with velocity {self.velocity}")  # Debug print

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        print(f"Shot updated to {self.position}")  # Debug print

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        print(f"Drawing shot at {self.position}")  # Debug print
