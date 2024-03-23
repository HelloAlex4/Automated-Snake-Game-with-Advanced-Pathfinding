import pygame
import random
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Frame rate
FPS = 100

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# Food settings
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True

# Score
score = 0

# Set speed of the game
clock = pygame.time.Clock()

# Game over function
def game_over():
    my_font = pygame.font.SysFont('ubuntu', 70)
    go_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    screen.fill(BLACK)
    screen.blit(go_surface, go_rect)
    pygame.display.flip()
    pygame.time.wait(500)
    pygame.quit()
    sys.exit()

def initializeMatrix():
    coordsystem = []

    for x in range(40):
        coordsystem.append([])
        for y in range(60):
            coordsystem[x].append(0)
    
    return(coordsystem)

initializeMatrix()

def initializePathMatrix():
    pathMatrix = initializeMatrix()

    xFood = food_pos[0] // 10
    yFood = food_pos[1] // 10

    for y in range(40):
        for x in range(60):
            xdistance = x - xFood
            ydistance = y - yFood

            distance = math.sqrt(xdistance ** 2 + ydistance ** 2)

            pathMatrix[y][x] = round(distance, 3)


    return(rewriteMatrix(pathMatrix))


def rewriteMatrix(coordsystem):
    x = food_pos[0] // 10
    y = food_pos[1] // 10
    coordsystem[y][x] = 0

    for a in snake_body:
        x = a[0] // 10
        y = a[1] // 10
        coordsystem[y][x] = 999

        if x > 0:
            coordsystem[y][x-1] += 17
        if x < 59:
            coordsystem[y][x+1] += 17

        if y > 0:
            coordsystem[y-1][x] += 17
        if y <39:
            coordsystem[y+1][x] += 17

        if(snake_body.index(a) > 2):
            if x > 1:
                coordsystem[y][x-2] += 10
            if x < 58:
                coordsystem[y][x+2] += 10

            if y > 1:
                coordsystem[y-2][x] += 10
            if y < 38:
                coordsystem[y+2][x] += 10

    return(coordsystem)

def calcdirection(matrix):
    global change_to

    x = snake_pos[0] // 10
    y = snake_pos[1] // 10

    print(x)
    print(y)

    distancelist = []

    if x > 0:
        distancelist.append(matrix[y][x - 1])
    else:
        distancelist.append(999)
    if x < 59:
        distancelist.append(matrix[y][x + 1])
    else:
        distancelist.append(999)


    if y > 0:
        distancelist.append(matrix[y - 1][x])
    else:
        distancelist.append(999)
    if y < 39:
        distancelist.append(matrix[y + 1][x])
    else:
        distancelist.append(999)
    
    direction = distancelist.index(min(distancelist))

    print(distancelist)

    if direction == 0:
        change_to = "LEFT"
        print("left")
    elif direction == 1:
        change_to = "RIGHT"
        print("right")
    elif direction == 2:
        change_to = "UP"
        print("up")
    elif direction == 3:
        change_to = "DOWN"
        print("DOWN")

# Main loop
while True:
    pathMatrix = initializePathMatrix()

    calcdirection(pathMatrix)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

            if event.key == pygame.K_a:
                FPS += 10
            if event.key == pygame.K_z:
                FPS -= 10

    # Validate direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                    random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True

    # Background and snake/food drawing
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.ellipse(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()
    clock.tick(FPS)
