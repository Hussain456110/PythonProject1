import pygame
import sys
import time

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login & Loading Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Simple login simulation
username = "Hussain"
password = "1234"
active_box = "username"
input_active = True
clock = pygame.time.Clock()

def draw_login():
    screen.fill(WHITE)
    user_text = font.render(f"Username: {username}", True, BLACK)
    pass_text = font.render(f"Password: {'*' * len(password)}", True, BLACK)
    hint_text = font.render("Press ENTER to login", True, BLUE)
    screen.blit(user_text, (100, 100))
    screen.blit(pass_text, (100, 150))
    screen.blit(hint_text, (100, 250))

def draw_loading():
    screen.fill(WHITE)
    loading_text = font.render("Loading...", True, BLUE)
    screen.blit(loading_text, (250, 180))
    pygame.display.flip()
    time.sleep(2)  # simulate loading time

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_TAB:
                active_box = "password" if active_box == "username" else "username"
            elif event.key == pygame.K_RETURN:
                draw_loading()
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                if active_box == "username":
                    username = username[:-1]
                else:
                    password = password[:-1]
            else:
                if active_box == "username":
                    username += event.unicode
                else:
                    password += event.unicode

    if input_active:
        draw_login()
    else:
        screen.fill(WHITE)
        success_text = font.render(f"Welcome {username}!", True, BLUE)
        screen.blit(success_text, (200, 200))

    pygame.display.flip()
    clock.tick(30)

