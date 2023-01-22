import pygame

class Button():
    def __init__(
       self,width,height,x_position,
       y_position,button_color,window,
       text,text_size,text_color,
       border=None,border_color=None
       ):

        super().__init__()
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.button_color = button_color
        self.window = window
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.border = border
        self.border_color = border_color

    def create_button(self):
        font_style = pygame.font.Font("Minecraft.ttf",self.text_size)
        font_surface = font_style.render(self.text,True,self.text_color)

        pygame.draw.rect(self.window,self.button_color,(
            self.x_position,self.y_position,self.width,self.height
        ))
        pygame.draw.rect(self.window,self.border_color,(
            self.x_position,self.y_position,self.width,self.height
        ),self.border)

        font_x = self.x_position + self.width//2
        font_y = self.y_position + self.height//2
        self.window.blit(font_surface,font_surface.get_rect(center= (font_x,font_y)))
    
        
    def check_collision(self,):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        
        if mouse_y >= self.y_position and mouse_y <= self.y_position + self.height:
            if mouse_x >= self.x_position and mouse_x <= self.x_position + self.width:
                return True
                


                

