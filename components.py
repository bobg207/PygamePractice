import pygame
from settings import *


class Player:
    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.rect = pygame.Rect(x, y, width, height)
        # self.rect.x = x
        # self.rect.y = y
        self.color = color
        self.x_velo = 5

        self.y_velo = 0
        self.jumping = False
        self.jump_height = 15

    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)

    def update(self, surface_list):
        x_change = 0
        y_change = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.right + x_change < WIDTH-BRICK_WIDTH:
            x_change = self.x_velo
        if keys[pygame.K_LEFT] and self.rect.x > BRICK_WIDTH:
            x_change = -1*self.x_velo
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.y_velo = -15
        
        # add gravity
        self.y_velo += GRAVITY
        if self.y_velo > 10:
            self.y_velo = 10        # set terminal velocity
            
        y_change += self.y_velo
        
        for surface in surface_list:
            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                if self.y_velo >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.jumping = False
                    self.y_velo = 0
                elif self.y_velo < 0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.y_velo = 0

        self.rect.x += x_change
        self.rect.y += y_change

class Brick:
    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)