from pygame import locals

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 10

COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (150, 150, 150, 100)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

direction_dict = {
    locals.K_LEFT: (-1, 0),
    locals.K_RIGHT: (1, 0),
    locals.K_UP: (0, -1),
    locals.K_DOWN: (0, 1)
}

direction_angle_dict = {
    locals.K_LEFT: 270,
    locals.K_RIGHT: 90,
    locals.K_UP: 180,
    locals.K_DOWN: 0
}
