import pygame
from settings import *
import random


class Player:
    def __init__(self, display, x, y, width, height, image):
        self.display = display
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_velo = 5

        self.y_velo = 0
        self.jumping = False
        self.landed = True
        self.jump_height = 15

    def draw(self):
        self.display.blit(self.image, self.rect)

    def update(self, surface_list, plat_list):
        x_change = 0
        y_change = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: # and self.rect.right + x_change < WIDTH-BRICK_WIDTH:
            x_change = self.x_velo
        if keys[pygame.K_LEFT]: # and self.rect.x > BRICK_WIDTH:
            x_change = -1*self.x_velo
        if keys[pygame.K_SPACE] and not self.jumping and self.landed:
            self.jumping = True
            self.landed = False
            self.y_velo = -15
        if not keys[pygame.K_SPACE]:
            self.jumping = False
        
        # add gravity
        self.y_velo += GRAVITY
        if self.y_velo > 10:
            self.y_velo = 10        # set terminal velocity
            
        y_change += self.y_velo
        
        for surface in surface_list:
            if surface.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                x_change = 0
            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                if self.y_velo >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.landed = True
                    self.y_velo = 0
                elif self.y_velo < 0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.y_velo = 0

        for plat in plat_list:
            if plat.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                if self.y_velo >= 0:
                    y_change = plat.rect.top - self.rect.bottom
                    self.landed = True
                    self.y_velo = 0
                elif self.y_velo < 0:
                    y_change = plat.rect.bottom - self.rect.top
                    self.y_velo = 0

        self.rect.x += x_change
        self.rect.y += y_change

class Brick:
    def __init__(self, display, x, y, width, height, image):
        self.display = display
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.display.blit(self.img, self.rect)

class Barrier:
    def __init__(self, x, y, display):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH*.1, BRICK_HEIGHT)
    #     self.display = display

    # def draw(self):
    #     pygame.draw.rect(self.display, RED, self.rect)

class Enemy:
    def __init__(self, display, x, y):
        image = pygame.image.load('images/slime_normal.png')
        self.display = display
        self.img = pygame.transform.scale(image, (BRICK_WIDTH, .5*BRICK_HEIGHT))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xvelo = 1

    def draw(self):
        self.display.blit(self.img, self.rect)

    def update(self, b_list):

        for b in b_list:
            if b.rect.colliderect(self.rect):
                self.xvelo *= -1 

        self.rect.x += self.xvelo
        
class Plank():
    def __init__(self, x, y, display):
        img = pygame.image.load('images/plank.png')
        self.img = pygame.transform.scale(img, (2*BRICK_WIDTH, .5*BRICK_HEIGHT))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.display = display
        self.yvelo = random.choice([-1, 2])
        self.max = y - 3*BRICK_HEIGHT
        self.min = y + 3*BRICK_HEIGHT

    def draw(self):
        self.display.blit(self.img, self.rect)

    def update(self):
        self.rect.y += self.yvelo

        if self.rect.y <= self.max or self.rect.y >= self.min or \
            self.rect.y <= 2*BRICK_HEIGHT:
            self.yvelo *= -1
