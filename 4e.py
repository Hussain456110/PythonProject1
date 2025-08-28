import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Escape")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_SIZE = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - 70, PLAYER_SIZE, PLAYER_SIZE)
PLAYER_SPEED = 7

# Block (enemy) settings
BLOCK_SIZE = 50
blocks = []
BLOCK_SPEED = 5
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 800)  # spawn every 800ms

# Score
score = 0
font = pygame.font.Font(None, 50)

# Clock
clock = pygame.time.Clock()

def main():
    global score
    running = True

    while running:
        screen.fill(BLACK)

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SPAWN_EVENT:
                # Spawn a new falling block at random x
                x_pos = random.randint(0, WIDTH - BLOCK_SIZE)
                blocks.append(pygame.Rect(x_pos, 0, BLOCK_SIZE, BLOCK_SIZE))

        # --- Player Movement ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += PLAYER_SPEED

        # --- Update Blocks ---
        for block in blocks[:]:
            block.y += BLOCK_SPEED
            if block.y > HEIGHT:
                blocks.remove(block)  # remove if out of screen
                score += 1  # reward for dodging

            # Collision detection
            if player.colliderect(block):
                running = False

        # --- Draw ---
        pygame.draw.rect(screen, BLUE, player)  # player
        for block in blocks:
            pygame.draw.rect(screen, RED, block)  # blocks

        # Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    # Game over screen
    game_over_text = font.render("GAME OVER!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
