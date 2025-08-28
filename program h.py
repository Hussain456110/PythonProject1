import pygame
import sys
import time

pygame.init()

# ----------------------------
# Global Screen
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login and Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# ----------------------------
# Login Variables
username = ""
password = ""
stage = "username"   # username → password → ready → loading → game

# ----------------------------
# Ball Game Variables
BALL_RADIUS = 30
BALL_SPEEDS = [[4, 4], [-4, 4]]
BORDER = 40
GAP_WIDTH = 120
GAP_HEIGHT = 120

gap_x = (WIDTH - GAP_WIDTH) // 2
gap_y = (HEIGHT - GAP_HEIGHT) // 2

balls = [
    {"pos": [WIDTH // 3, HEIGHT // 3], "vel": BALL_SPEEDS[0][:]},
    {"pos": [2 * WIDTH // 3, HEIGHT // 2], "vel": BALL_SPEEDS[1][:]}
]

PLAYER_RADIUS = 30
PLAYER_SPEED = 6

player1 = [WIDTH // 2, HEIGHT - 60]   # bottom (blue)
player2 = [WIDTH // 2, 60]            # top (yellow)

score1 = 0
score2 = 0
game_running = True

# ----------------------------
# Functions

def draw_login():
    screen.fill(WHITE)
    user_text = font.render(f"Username: {username}", True, BLACK)
    passw_text = font.render(f"Password: {'*' * len(password)}", True, BLACK)

    if stage == "username":
        hint_text = font.render("Enter Username & press ENTER", True, BLUE)
        pygame.draw.rect(screen, BLUE, (90, 95, 320, 40), 2)
    elif stage == "password":
        hint_text = font.render("Enter Password & press ENTER", True, BLUE)
        pygame.draw.rect(screen, BLUE, (90, 145, 320, 40), 2)
    elif stage == "ready":
        hint_text = font.render("Press ENTER to login", True, BLUE)
    else:
        hint_text = None

    screen.blit(user_text, (100, 100))
    screen.blit(passw_text, (100, 150))
    if hint_text:
        screen.blit(hint_text, (100, 190))
    pygame.display.flip()


def draw_loading():
    screen.fill(WHITE)
    loading_text = font.render("Loading...", True, BLUE)
    screen.blit(loading_text, (180, 130))
    pygame.display.flip()
    time.sleep(2)


def run_game():
    global score1, score2, game_running
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player 1 (bottom, arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player1[0] - PLAYER_RADIUS > BORDER:
            player1[0] -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player1[0] + PLAYER_RADIUS < WIDTH - BORDER:
            player1[0] += PLAYER_SPEED

        # Player 2 (top, A/D keys)
        if keys[pygame.K_a] and player2[0] - PLAYER_RADIUS > BORDER:
            player2[0] -= PLAYER_SPEED
        if keys[pygame.K_d] and player2[0] + PLAYER_RADIUS < WIDTH - BORDER:
            player2[0] += PLAYER_SPEED

        # Update balls
        for ball in balls:
            ball["pos"][0] += ball["vel"][0]
            ball["pos"][1] += ball["vel"][1]

            x, y = ball["pos"]

            # Check gaps: if ball enters any gap → game over
            if (gap_x < x < gap_x + GAP_WIDTH and y - BALL_RADIUS <= BORDER) or (gap_x < x < gap_x + GAP_WIDTH and y + BALL_RADIUS >= HEIGHT - BORDER):
                game_running = False
            if (gap_y < y < gap_y + GAP_HEIGHT and x - BALL_RADIUS <= BORDER) or (gap_y < y < gap_y + GAP_HEIGHT and x + BALL_RADIUS >= WIDTH - BORDER):
                game_running = False

            # Bounce on walls if not gap
            if x - BALL_RADIUS <= BORDER or x + BALL_RADIUS >= WIDTH - BORDER:
                ball["vel"][0] *= -1
            if y - BALL_RADIUS <= BORDER or y + BALL_RADIUS >= HEIGHT - BORDER:
                ball["vel"][1] *= -1

            # Collision with Player 1
            dx1 = x - player1[0]
            dy1 = y - player1[1]
            if (dx1 * dx1 + dy1 * dy1) ** 0.5 <= BALL_RADIUS + PLAYER_RADIUS:
                ball["vel"][1] = -abs(ball["vel"][1])
                score1 += 1

            # Collision with Player 2
            dx2 = x - player2[0]
            dy2 = y - player2[1]
            if (dx2 * dx2 + dy2 * dy2) ** 0.5 <= BALL_RADIUS + PLAYER_RADIUS:
                ball["vel"][1] = abs(ball["vel"][1])
                score2 += 1

        # Drawing
        screen.fill(BLACK)

        # Borders with gaps
        pygame.draw.rect(screen, GREEN, (0, 0, gap_x, BORDER))
        pygame.draw.rect(screen, GREEN, (gap_x + GAP_WIDTH, 0, WIDTH - (gap_x + GAP_WIDTH), BORDER))
        pygame.draw.rect(screen, GREEN, (0, HEIGHT - BORDER, gap_x, BORDER))
        pygame.draw.rect(screen, GREEN, (gap_x + GAP_WIDTH, HEIGHT - BORDER, WIDTH - (gap_x + GAP_WIDTH), BORDER))
        pygame.draw.rect(screen, GREEN, (0, 0, BORDER, gap_y))
        pygame.draw.rect(screen, GREEN, (0, gap_y + GAP_HEIGHT, BORDER, HEIGHT - (gap_y + GAP_HEIGHT)))
        pygame.draw.rect(screen, GREEN, (WIDTH - BORDER, 0, BORDER, gap_y))
        pygame.draw.rect(screen, GREEN, (WIDTH - BORDER, gap_y + GAP_HEIGHT, BORDER, HEIGHT - (gap_y + GAP_HEIGHT)))

        # Balls
        for ball in balls:
            pygame.draw.circle(screen, RED, (int(ball["pos"][0]), int(ball["pos"][1])), BALL_RADIUS)

        # Players
        pygame.draw.circle(screen, BLUE, (int(player1[0]), int(player1[1])), PLAYER_RADIUS)   # bottom
        pygame.draw.circle(screen, YELLOW, (int(player2[0]), int(player2[1])), PLAYER_RADIUS)  # top

        # Scores
        score_text1 = font.render(f"P1 Score: {score1}", True, WHITE)
        score_text2 = font.render(f"P2 Score: {score2}", True, WHITE)
        screen.blit(score_text1, (10, 10))
        screen.blit(score_text2, (WIDTH - 180, 10))

        pygame.display.flip()
        clock.tick(60)


# ----------------------------
# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if stage == "username":
                if event.key == pygame.K_RETURN and username != "":
                    stage = "password"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

            elif stage == "password":
                if event.key == pygame.K_RETURN and password != "":
                    stage = "ready"
                elif event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

            elif stage == "ready":
                if event.key == pygame.K_RETURN:
                    draw_loading()
                    stage = "game"

    if stage in ["username", "password", "ready"]:
        draw_login()
    elif stage == "game":
        run_game()
        pygame.quit()
        sys.exit()

    clock.tick(30)
