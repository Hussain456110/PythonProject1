import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Ball settings
BALL_RADIUS = 25
BALL_SPEEDS = [(2, 2), (3, 3), (4, 4)]  # different speeds for 3 balls

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
PADDLE_SPEED = 10

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Balls Game")

# Clock
clock = pygame.time.Clock()

# Multiple balls and their speeds/velocities
balls = [
    {"pos": [WIDTH // 2, HEIGHT // 3], "vel": list(BALL_SPEEDS[0])},
    {"pos": [WIDTH // 3, HEIGHT // 2], "vel": list(BALL_SPEEDS[1])},
    {"pos": [2 * WIDTH // 3, HEIGHT // 2], "vel": list(BALL_SPEEDS[2])},
]

# Paddle positions at bottom
paddle1 = [100, HEIGHT - 30]  # left paddle
paddle2 = [400, HEIGHT - 30]  # right paddle

# Score
score = 0
font = pygame.font.Font(None, 50)


def main():
    global balls, paddle1, paddle2, score
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Move paddle1 with arrow keys
        if keys[pygame.K_LEFT] and paddle1[0] > 0:
            paddle1[0] -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle1[0] < WIDTH - PADDLE_WIDTH:
            paddle1[0] += PADDLE_SPEED

        # Move paddle2 with U (left) and D (right)
        if keys[pygame.K_u] and paddle2[0] > 0:
            paddle2[0] -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle2[0] < WIDTH - PADDLE_WIDTH:
            paddle2[0] += PADDLE_SPEED

        # Update balls
        for ball in balls:
            ball["pos"][0] += ball["vel"][0]
            ball["pos"][1] += ball["vel"][1]

            # Bounce off walls
            if ball["pos"][0] - BALL_RADIUS <= 0 or ball["pos"][0] + BALL_RADIUS >= WIDTH:
                ball["vel"][0] = -ball["vel"][0]
            if ball["pos"][1] - BALL_RADIUS <= 0:
                ball["vel"][1] = -ball["vel"][1]

            # Ball falls below screen (Game Over)
            if ball["pos"][1] + BALL_RADIUS >= HEIGHT:
                print(f"Game Over! Final Score: {score}")
                running = False

            # Collision with paddle1
            if (
                paddle1[1] < ball["pos"][1] + BALL_RADIUS < paddle1[1] + PADDLE_HEIGHT
                and paddle1[0] < ball["pos"][0] < paddle1[0] + PADDLE_WIDTH
            ):
                ball["vel"][1] = -ball["vel"][1]
                score += 1


            # Collision with paddle2
            if (
                paddle2[1] < ball["pos"][1] + BALL_RADIUS < paddle2[1] + PADDLE_HEIGHT
                and paddle2[0] < ball["pos"][0] < paddle2[0] + PADDLE_WIDTH
            ):
                ball["vel"][1] = -ball["vel"][1]
                score += 1

        # Draw everything
        screen.fill(BLACK)

        # Draw balls
        for ball in balls:
            pygame.draw.circle(screen, RED, (int(ball["pos"][0]), int(ball["pos"][1])), BALL_RADIUS)

        # Draw paddles
        pygame.draw.rect(screen, BLUE, (*paddle1, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, BLUE, (*paddle2, PADDLE_WIDTH, PADDLE_HEIGHT))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (50, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
