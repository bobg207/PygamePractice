import pygame, sys
from components_imgs import Player, Brick, Enemy, Barrier, Plank
from settings import *

# General Game 
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

playing = True

block_img = pygame.image.load('images/block.png')
crate_img = pygame.image.load('images/crate.png')
ground_img = pygame.image.load('images/ground.png')
spikes_img = pygame.image.load('images/spikes.png')
player_img = pygame.image.load('images/player.png')

brick_list = []
enemy_list = []
barrier_list = []
platform_list = []
for row in range(len(LAYOUT)):
    y_pos = row*BRICK_HEIGHT
    for col in range(len(LAYOUT[0])):
        x_pos = col*BRICK_HEIGHT
        
        if LAYOUT[row][col] == '1':
            brick = Brick(display, x_pos, y_pos, BRICK_WIDTH, BRICK_HEIGHT, block_img)
            brick_list.append(brick)

        elif LAYOUT[row][col] == 'c':
            brick = Brick(display, x_pos, y_pos, BRICK_WIDTH, BRICK_HEIGHT, crate_img)
            brick_list.append(brick)

        elif LAYOUT[row][col] == 'g':
            brick = Brick(display, x_pos, y_pos, BRICK_WIDTH, BRICK_HEIGHT, ground_img)
            brick_list.append(brick)

        elif LAYOUT[row][col] == 's':
            brick = Brick(display, x_pos, y_pos+.5*BRICK_HEIGHT, BRICK_WIDTH, .5*BRICK_HEIGHT, spikes_img)
            brick_list.append(brick)

        elif LAYOUT[row][col] == 'e':
            enemy = Enemy(display, x_pos, y_pos+.5*BRICK_HEIGHT)
            enemy_list.append(enemy)

        elif LAYOUT[row][col] == 'v':
            barrier = Barrier(x_pos, y_pos+.5, display)
            barrier_list.append(barrier)

        elif LAYOUT[row][col] == '2':
            platform = Plank(x_pos, y_pos, display)
            platform_list.append(platform)

        elif LAYOUT[row][col] == 'p':
            player = Player(display, x_pos, y_pos, 40, 40, player_img)
# Game Loop
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update(brick_list, platform_list)

    for enemy in enemy_list:
        enemy.update(barrier_list)

    for plat in platform_list:
        plat.update()

    display.fill(SKY_BLUE)
    # for bar in barrier_list:
    #     bar.draw()

    for brick in brick_list:
        brick.draw()

    for enemy in enemy_list:
        enemy.draw()

    for plat in platform_list:
        plat.draw()

    player.draw()

    pygame.display.update()
    clock.tick(FPS)