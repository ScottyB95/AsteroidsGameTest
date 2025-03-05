import pygame
import random
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity, updatable, drawable):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
        self.position = pygame.math.Vector2(self.x, self.y)
        self.updatable = updatable
        self.drawable = drawable

        # Create the asteroid surface
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        asteroid_color = (200, 200, 200)  # Light gray color for asteroid
        pygame.draw.circle(self.image, asteroid_color, (self.radius, self.radius), self.radius)
        
        # Create the rectangle for positioning and collision
        self.rect = self.image.get_rect(center=self.position)
        
        # Add the asteroid to the updatable and drawable groups
        self.updatable.add(self)
        self.drawable.add(self)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        # Draw the asteroid to the screen
        screen.blit(self.image, self.rect)
        print(f"Drawing asteroid at {self.position}")  # Debug print

    def split(self, asteroid_field):
        if self.radius > ASTEROID_MIN_RADIUS * 2:  # Large asteroid splits into medium
            new_radius = self.radius // 2
            for _ in range(2):
                new_velocity = self.velocity.rotate(random.randint(-45, 45))
                new_asteroid = Asteroid(self.rect.centerx, self.rect.centery, new_radius, new_velocity, self.updatable, self.drawable)
                asteroid_field.asteroids.add(new_asteroid)
                self.updatable.add(new_asteroid)
                self.drawable.add(new_asteroid)
        elif self.radius > ASTEROID_MIN_RADIUS:  # Medium asteroid splits into small
            new_radius = ASTEROID_MIN_RADIUS
            for _ in range(2):
                new_velocity = self.velocity.rotate(random.randint(-45, 45))
                new_asteroid = Asteroid(self.rect.centerx, self.rect.centery, new_radius, new_velocity, self.updatable, self.drawable)
                asteroid_field.asteroids.add(new_asteroid)
                self.updatable.add(new_asteroid)
                self.drawable.add(new_asteroid)
        self.kill()  # Destroy the current asteroid
