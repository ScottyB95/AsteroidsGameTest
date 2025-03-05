import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)  # Ensure proper initialization
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Placeholder method for drawing
        pass

    def update(self, dt):
        # Placeholder method for updating position
        pass
    
    def check_collision(self, other):
        # Used to check the distance between the centers is less than the sum of the radii
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
