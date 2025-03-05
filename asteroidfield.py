import pygame
import random
from asteroid import Asteroid
from constants import ASTEROID_SPAWN_RATE, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS

class AsteroidField(pygame.sprite.Sprite):
    def __init__(self, updatable, drawable):
        super().__init__()
        self.updatable = updatable
        self.drawable = drawable
        self.asteroids = pygame.sprite.Group()  # Group to store the asteroids
        self.spawn_timer = 0  # Initialize spawn_timer to fix AttributeError

    def update(self, dt):
        self.spawn_timer += dt  # Accumulate time for spawning
        if self.spawn_timer >= ASTEROID_SPAWN_RATE:
            self.spawn_asteroid()  # Spawn a new asteroid
            self.spawn_timer = 0  # Reset spawn timer after spawning
        self.asteroids.update(dt)  # Update all asteroids

    def spawn_asteroid(self):
        # Randomly spawn from left or right
        x = random.choice([0, SCREEN_WIDTH])
        y = random.randint(0, SCREEN_HEIGHT)  # Random vertical position
        
        # Calculate a velocity vector pointing towards the center
        center = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        direction = (center - pygame.math.Vector2(x, y)).normalize() * random.randint(50, 150)
        
        # Create the new asteroid and add it to the groups
        new_asteroid = Asteroid(x, y, ASTEROID_MAX_RADIUS, direction, self.updatable, self.drawable)
        
        # Add asteroid to the updatable and drawable groups
        self.asteroids.add(new_asteroid)  # Keep track of all asteroids in the group
        self.updatable.add(new_asteroid)
        self.drawable.add(new_asteroid)
        
        print(f"New asteroid spawned at ({x}, {y}) with velocity {direction}")

    def get_asteroids(self):
        return self.asteroids  # Method to retrieve the list of asteroids
