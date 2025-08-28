import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Ball settings
BALL_RADIUS = 20

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED = 6

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi Ball Game")

# Clock
clock = pygame.time.Clock()

# Define balls
ball1 = {"pos": [WIDTH // 2, HEIGHT // 2], "speed": [3, 3], "color": RED}
ball2 = {"pos": [WIDTH // 3, HEIGHT // 3], "speed": [4, 3], "color": YELLOW}
ball3 = {"pos": [WIDTH // 4, HEIGHT // 4], "speed": [5, 2], "color": ORANGE}
balls = [ball1, ball2, ball3]

# Define paddles
paddle_bottom = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_top = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, 15, PADDLE_WIDTH, PADDLE_HEIGHT)

def move_balls():
    for ball in balls:
        # Move ball
        ball["pos"][0] += ball["speed"][0]
        ball["pos"][1] += ball["speed"][1]

        # Bounce on walls
        if ball["pos"][0] - BALL_RADIUS <= 0 or ball["pos"][0] + BALL_RADIUS >= WIDTH:
            ball["speed"][0] *= -1
        if ball["pos"][1] - BALL_RADIUS <= 0 or ball["pos"][1] + BALL_RADIUS >= HEIGHT:
            ball["speed"][1] *= -1

        # Bounce on paddles
        if paddle_bottom.collidepoint(ball["pos"][0], ball["pos"][1] + BALL_RADIUS):
            ball["speed"][1] *= -1
        if paddle_top.collidepoint(ball["pos"][0], ball["pos"][1] - BALL_RADIUS):
            ball["speed"][1] *= -1

def main():
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key press handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_bottom.left > 0:
            paddle_bottom.move_ip(-PADDLE_SPEED, 0)
        if keys[pygame.K_RIGHT] and paddle_bottom.right < WIDTH:
            paddle_bottom.move_ip(PADDLE_SPEED, 0)
        if keys[pygame.K_a] and paddle_top.left > 0:
            paddle_top.move_ip(-PADDLE_SPEED, 0)
        if keys[pygame.K_d] and paddle_top.right < WIDTH:
            paddle_top.move_ip(PADDLE_SPEED, 0)

        # Move balls
        move_balls()

        # Draw paddles (make sure they show before balls)
        pygame.draw.rect(screen, BLUE, paddle_bottom)  # bottom paddle
        pygame.draw.rect(screen, GREEN, paddle_top)    # top paddle

        # Draw balls
        for ball in balls:
            pygame.draw.circle(screen, ball["color"], ball["pos"], BALL_RADIUS)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()
