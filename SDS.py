GAP_WIDTH = 120
GAP_HEIGHT = 120

gap_x = {WIDTH - GAP_WIDTH} // 2
gap_y = {HEIGHT - GAP_HEIGHT} // 2

balls =[
    {"pos": WIDTH // 3, HEIGHT // 2], "vel":Balls_SPEED[0]},
    {"pos":2 * WIDTH // 2, HEIGHT //3], "vel":BALLS_SPEED[1]}

player_radius = 20
player_speed = 5

player1=[WIDTH // 3, HEIGHT - 60]
player2=[WIDTH // 2, 60]

score1 = 0
score2 = 0
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

running = True

for ball in balls:
    ball["pos"][0] += ball["vel"][0]
    ball["pos"][1] += ball["vel"][1]
     x , y = ball["pos"]
if(gap_x < x < gap_x + GAP_WIDTH and y - BALL_RADIUS <= BORDER) or (gap_x < x < gap_x + GAP_WIDTH and y + BALL_RADIUS>= HEIGHT - BORDER):
    running = False
if(gap_y < y < gap_y + GAP_HEIGHT and x + BALL_RADIUS <= BORDER or (gap_y <y < gap_y + GAP_HEIGHT and  x + BALL_RADIUS>= HEIGHT - BORDER):
   running = False
if x - BALL_RADIUS <=BORDER or x + BALL_RADIUS>= WIDTH - BORDER :
   ball["vel"][0] *=-1
if y - BALL_RADIUS <= BORDER or y + BALL_RADIUS > HEIGHT - BORDER:
   ball["vel"][1] *=-1

dx1 = x - player1[0]
dy1 = y - player1[0]
   if(dx1 * dx1 + dy1 * dy1 )** 0.5 <=BALL_RADIUS + PLAYER_RADIUS :
   ball["vel"][1] = -abs{ball]["vel"][1]
   score1 += 1
   dx2 = x - player2[0]
        dy2 = y - player2[1]
        if (dx2 * dx2 + dy2 * dy2) ** 0.5 <= BALL_RADIUS + PLAYER_RADIUS:
            ball["vel"][1] = abs(ball["vel"][1])  # push downward
            score2 += 1
screen.fill(BLACK)
pygame.draw.rect(screen, GREEN,(0, 0, (BORDER,gap_x)
pygame.draw.rect(screen,GREEN,(0, gap_x +gap_WIDTH, 0, WIDTH - (gap_x + GAP_WIDTH), BORDER))
               pygame.draw.rect(screen, GREEN, (gap_x + GAP_WIDTH, 0, WIDTH - (gap_x + GAP_WIDTH), BORDER))

    # Bottom border with gap
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - BORDER, gap_x, BORDER))
    pygame.draw.rect(screen, GREEN, (gap_x + GAP_WIDTH, HEIGHT - BORDER, WIDTH - (gap_x + GAP_WIDTH), BORDER))

    # Left border with gap
    pygame.draw.rect(screen, GREEN, (0, 0, BORDER, gap_y))
    pygame.draw.rect(screen, GREEN, (0, gap_y + GAP_HEIGHT, BORDER, HEIGHT - (gap_y + GAP_HEIGHT)))

    # Right border with gap
    pygame.draw.rect(screen, GREEN, (WIDTH - BORDER, 0, BORDER, gap_y))
    pygame.draw.rect(screen, GREEN, (WIDTH - BORDER, gap_y + GAP_HEIGHT, BORDER, HEIGHT - (gap_y + GAP_HEIGHT)))
