import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball settings
BALL_RADIUS = 15
BALL_SPEED = [4, 4]

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_SPEED = 8

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


# Ball position and movement
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = BALL_SPEED.copy()

# Paddle position
paddle_pos = [WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50]

# Score
score = 0

# Font for displaying the score
font = pygame.font.Font(None, 36)

# Main game loop
def main():
    global ball_pos, ball_vel, paddle_pos, score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddle with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
            paddle_pos[0] -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - PADDLE_WIDTH:
            paddle_pos[0] += PADDLE_SPEED

        # Update ball position
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Ball collision with walls
        if ball_pos[0] - BALL_RADIUS < 0 or ball_pos[0] + BALL_RADIUS > WIDTH:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] - BALL_RADIUS < 0:
            ball_vel[1] = -ball_vel[1]

        # Ball collision with paddle
        if (
            paddle_pos[1] < ball_pos[1] + BALL_RADIUS < paddle_pos[1] + PADDLE_HEIGHT
            and paddle_pos[0] < ball_pos[0] < paddle_pos[0] + PADDLE_WIDTH
        ):
            ball_vel[1] = -ball_vel[1]
            score += 1

        # Ball falls below the paddle
        if ball_pos[1] - BALL_RADIUS > HEIGHT:
            print(f"Game Over! Your score: {score}")
            running = False

        # Clear screen
        screen.fill(BLACK)

        # Draw ball
        pygame.draw.circle(screen, RED, ball_pos, BALL_RADIUS)

        # Draw paddle
        pygame.draw.rect(screen, BLUE, (*paddle_pos, PADDLE_WIDTH, PADDLE_HEIGHT))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
