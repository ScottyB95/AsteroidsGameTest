import pygame
from circleshape import CircleShape
from shots import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y, updatable, drawable):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # Initialize shoot_timer here
        self.updatable = updatable
        self.drawable = drawable
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity

        self.containers = (updatable, drawable)
        updatable.add(self)
        drawable.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)  # Draw a white triangle
        print(f"Drawing player at {self.position}")  # Debug print

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        direction = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_w]:
            self.move(-dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(dt)  # Move backward

        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer <= 0:  # Check if the cooldown period has passed
            # Use the front vertex of the player's triangle for shot start position
            front_vertex = self.triangle()[0]
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot = Shot(front_vertex.x, front_vertex.y, shot_velocity)
            self.updatable.add(shot)
            self.drawable.add(shot)  # Add to drawable group
            self.shoot_timer = 0.2  # Reset shoot timer (adjust cooldown period as needed)
            print(f"Shot fired at {front_vertex} with velocity {shot_velocity}")
