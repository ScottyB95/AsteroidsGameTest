import pygame
from player import Player
from asteroid import Asteroid
from shots import Shot
from asteroidfield import AsteroidField
from circleshape import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroids')

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y, updatable, drawable)
updatable.add(player)
drawable.add(player)

asteroid_field = AsteroidField(updatable, drawable)
updatable.add(asteroid_field)

score = 0  # Initialize score
lives = 3  # Initialize lives

font = pygame.font.Font(None, 36)  # Initialize font for displaying score and lives

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # Delta time in seconds

    if not game_over:
        updatable.update(dt)  # Update all updatable sprites
        screen.fill((0, 0, 0))  # Clear the screen

        for drawable_object in drawable:
            drawable_object.draw(screen)  # Draw all drawable sprites

        # Check for collisions between player and asteroids
        for asteroid in asteroid_field.get_asteroids():
            if player.check_collision(asteroid):
                print("Game over!")
                lives -= 1
                if lives <= 0:
                    game_over = True
                break

        # Check for collisions between bullets and asteroids
        for asteroid in asteroid_field.get_asteroids():
            for bullet in updatable:
                if isinstance(bullet, Shot) and bullet.check_collision(asteroid):
                    asteroid.split(asteroid_field)  # Pass asteroid_field instance
                    bullet.kill()
                    score += 10  # Increase score when an asteroid is destroyed
                    break

        # Display score and lives
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))
    else:
        game_over_text = font.render('Game Over! Press ESC to exit.', True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()  # Update the display

pygame.quit()
