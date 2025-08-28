import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login and Loading Page")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Login variables
username = ""
password = ""
stage = "username"   # stages: username → password → ready → loading → game
login_success = False

clock = pygame.time.Clock()


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
                    login_success = True

    if stage in ["username", "password", "ready"]:
        draw_login()
    elif stage == "game":
        screen.fill(WHITE)
        success_text = font.render(f"Welcome {username}! Game Loaded", True, BLUE)
        screen.blit(success_text, (80, 150))
        pygame.display.flip()

    clock.tick(30)
