import pygame
from settings import *

class Huds():
    def __init__(self,screen):
        self.pixel_font = pygame.font.Font("Minecraft.ttf",35)
        self.time_text = self.pixel_font.render("Time: ",True,BACKGROUND_COLOR)
        self.time_text_surface =  self.time_text.get_rect(topleft = (30,30))

        self.score_text = self.pixel_font.render("Score: ",True,BACKGROUND_COLOR)
        self.score_text_surface = self.score_text.get_rect(topleft = (30,100))

        self.ball_image = pygame.image.load("ball2.png").convert_alpha()
        self.ball_image = pygame.transform.rotozoom(self.ball_image,0,0.3) 
        self.ball_image_rect = self.ball_image.get_rect(topleft = (30,170))

        self.number_of_balls_left = NUMBER_OF_BALLS
        self.ball_text = self.pixel_font.render(f"x {self.number_of_balls_left}",True,BACKGROUND_COLOR)
        self.ball_text_surface = self.ball_text.get_rect(topleft = (self.ball_image_rect.width + 40,175))

        self.screen = screen


    def render_initial_texts(self):
        pygame.draw.rect(self.screen,FOREGROUND_COLOR,(0,0,HUDS_WIDTH,HUDS_HEIGTH))
        self.screen.blit(self.time_text,self.time_text_surface)
        self.screen.blit(self.score_text,self.score_text_surface)
        self.screen.blit(self.ball_image,self.ball_image_rect)
        self.screen.blit(self.ball_text,self.ball_text_surface)
       


    def re_render_values(self):
        self.ball_text = self.pixel_font.render(f"x {self.number_of_balls_left}",True,BACKGROUND_COLOR)
        self.ball_text_surface = self.ball_text.get_rect(topleft = (self.ball_image_rect.width + 40,175))
        self.screen.blit(self.ball_text,self.ball_text_surface)



    def balls_left(self,ball_y_position):
        x = False if self.number_of_balls_left == 0 and ball_y_position <= 0 else True
        print(x)
        return False if self.number_of_balls_left == 0 and ball_y_position <= 0 else True


    def update(self):
        self.render_initial_texts()
        self.re_render_values()