import pygame
from settings import SCREEN_WIDTH,HUDS_WIDTH,NET_WIDTH
from random import randrange,choice

class Net(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("net.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (randrange(HUDS_WIDTH,SCREEN_WIDTH - NET_WIDTH),0))
        self.direction = pygame.math.Vector2(1,0)
        self.speed = 9.2
        
    def net_movement(self):
        if self.rect.right >= SCREEN_WIDTH:
            self.direction.x = -1
        if self.rect.left <= HUDS_WIDTH:
            self.direction.x = 1

    def change_direction(self):
        self.direction.x = choice([1,-1])

    def change_direction1(self):
        self.direction.x = -1


        
    def update(self):
        self.net_movement()
        self.rect.x += self.direction.x * self.speed