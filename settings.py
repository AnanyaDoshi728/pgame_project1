from os import environ

#screen position
SCREEN_POSITION_X = 50
SCREEN_POSITION_Y = 70

#screen dimensions
SCREEN_WIDTH = 1324
SCREEN_HEIGHT = 670

#screen appears at specified position each time
environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SCREEN_POSITION_X,SCREEN_POSITION_Y)

#ball net area dimensions
BALL_NET_AREA = 1024
BALL_NET_HEIGHT = SCREEN_HEIGHT

#huds dimensions
HUDS_WIDTH = SCREEN_WIDTH - BALL_NET_AREA
HUDS_HEIGTH = SCREEN_HEIGHT

#frame rate
FPS = 60

#colors
BACKGROUND_COLOR = "#10368f"
FOREGROUND_COLOR = "#ff8e42"

#ball dimensions
BALL_WIDTH = 43
BALL_HEIGHT = 43

#net dimension
NET_WIDTH = 144
NET_HEIGHT = 46

#number of balls
NUMBER_OF_BALLS = 60
