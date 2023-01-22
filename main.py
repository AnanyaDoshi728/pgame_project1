import pygame
from settings import *
from sys import exit
from net import Net 
from huds import Huds
from button import Button

#pyinstaller --onefile -w 'filename.py'

#ball group
class Ball(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,0.3)
        self.rect = self.image.get_rect(midbottom = position)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = pygame.math.Vector2(7,30)
        self.released = False
        self.dead = False
        
    def ball_movement(self):
        if self.rect.bottom == SCREEN_HEIGHT:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
            else:
                self.direction.x = 0

    def release(self):
        if self.released:
            if self.rect.bottom <= 0 or self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.kill()
                self.released = False
                ball_x_position = self.rect.x if self.rect.left > 0 or self.rect.right < SCREEN_WIDTH else SCREEN_WIDTH // 2
                global ball
                ball_group.remove(ball)
                ball = Ball(position = (ball_x_position,SCREEN_HEIGHT))
                ball_group.add(ball)

            else:
                self.rect.y -= 1 * self.speed.y

                if self.rect.top <= 0 and self.rect.bottom <= NET_HEIGHT:
                    if self.rect.left >= net_group.sprite.rect.left and self.rect.right <= net_group.sprite.rect.right:
                        global score
                        score += 1
                        print("score")
                        self.kill()
                        self.released = False
                        # global ball
                        ball_group.remove(ball)
                        ball = Ball(position = (SCREEN_WIDTH // 2,SCREEN_HEIGHT) )
                        ball_group.add(ball)
                        

    def handle_collision_with_boundries(self):
        if self.rect.left <= HUDS_WIDTH:
            self.rect.left = HUDS_WIDTH
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def update(self):
        self.ball_movement()
        self.rect.x += self.direction.x * self.speed.x
        self.handle_collision_with_boundries()
        self.release()


def display_time():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    time_value = pixel_font.render(f"{current_time}/180",True,BACKGROUND_COLOR)
    time_value_surface = time_value.get_rect(topleft = (150,30))
    screen.blit(time_value,time_value_surface)
    return current_time


def draw_score_text(x_position = 160,y_position = 100,color = BACKGROUND_COLOR,text = ""):
    global score
    score_number = pixel_font.render(f"{text}{score}",True,color)
    score_number_surface = score_number.get_rect(topleft = (x_position,y_position))
    screen.blit(score_number,score_number_surface)
    return score


#initialize pygame
pygame.init()
clock = pygame.time.Clock()


#window setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shooter x Shooter")
ball_image = pygame.image.load("ball.png").convert_alpha()
pygame.display.set_icon(ball_image)

#
game_active = False
start_time = 0
time_since_game_active = 0
global score
score = 0

#net
net_group = pygame.sprite.GroupSingle()
net = Net()
net_group.add(net)

#ball
ball_group = pygame.sprite.GroupSingle()
ball = Ball(position = (SCREEN_WIDTH // 2,SCREEN_HEIGHT))
ball_group.add(ball)

#huds
huds = Huds(screen = screen)

#timer to change net x position randomly
net_direction_timer = pygame.USEREVENT + 1
pygame.time.set_timer(net_direction_timer,2000)

net_direction_timer1 = pygame.USEREVENT + 2
pygame.time.set_timer(net_direction_timer1,6000)


#play button
play_button = Button(
            450,130,(SCREEN_WIDTH - 450) // 2,(SCREEN_HEIGHT - 130) // 2,
            BACKGROUND_COLOR,screen,"PLAY",50,
            FOREGROUND_COLOR,5,FOREGROUND_COLOR
            )
#font
pixel_font = pygame.font.Font("Minecraft.ttf",35)

#main loop
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           ball.released = True
           huds.number_of_balls_left -= 1

        if event.type == net_direction_timer:
           net.change_direction()

        if event.type == net_direction_timer1:
            net.change_direction1()


    if game_active:
        game_active_time = pygame.time.get_ticks() // 1000
        # game_active = huds.balls_left(ball.rect.y)

        if time_since_game_active > 180:
            game_active = False

        if huds.number_of_balls_left == -1:
            game_active = False

        screen.fill(BACKGROUND_COLOR)

        #draw and update
        net_group.draw(screen)
        ball_group.draw(screen)
        
        net_group.update()
        ball_group.update()

        #huds
        huds.update()
        draw_score_text()

        time_since_game_active = display_time()


    else:
        start_time = pygame.time.get_ticks() // 1000
        screen.fill(BACKGROUND_COLOR)

        #draw play button 
        play_button.create_button()

        if draw_score_text() > 0:
            draw_score_text(
                x_position = play_button.x_position + play_button.width // 2 - 70,
                y_position = SCREEN_HEIGHT - 150,
                color = FOREGROUND_COLOR,
                text = "Score: "
            )

        #check collision for play button only if mouse button is down
        if event.type == pygame.MOUSEBUTTONDOWN:
           if play_button.check_collision():
                game_active = True 
                huds.number_of_balls_left = NUMBER_OF_BALLS

    
    pygame.display.update()
    clock.tick(FPS)