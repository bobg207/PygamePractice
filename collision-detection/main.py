import pygame, sys
from components import Player, Brick
from settings import *

# General Game 
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

playing = True

brick_list = []
for row in range(len(LAYOUT)):
    y_pos = row*BRICK_HEIGHT
    for col in range(len(LAYOUT[0])):
        x_pos = col*BRICK_HEIGHT
        
        if LAYOUT[row][col] == '1':
            brick = Brick(display, x_pos, y_pos, BRICK_WIDTH, BRICK_HEIGHT, BLUE)
            brick_list.append(brick)

        elif LAYOUT[row][col] == 'p':
            player = Player(display, x_pos, y_pos, 40, 40, RED)
# Game Loop
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update(brick_list)

    display.fill(WHITE)

    for brick in brick_list:
        brick.draw()
    player.draw()

    pygame.display.update()
    clock.tick(FPS)