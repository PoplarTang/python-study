import pygame

from pygame.locals import *
import sys
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

class Unit:
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def move_up(self):
        self.y -= 5
    def move_down(self):
        self.y += 5

class Bullet(Unit):
    pass

class Plane(Unit):
    def __init__(self, img_path, x, y, window):
        super().__init__(img_path, x, y, window)


def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("res/img_bg_level_1.jpg")

    plane = Plane("res/hero2.png", 196, 500, window)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # 鼠标点击右上角退出按钮
                print("quit")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("quit")
                    pygame.quit()
                    sys.exit()
                elif event.key == K_LEFT or event.key == K_a:
                    plane.move_left()
                elif event.key == K_RIGHT or event.key == K_d:
                    plane.move_right()
                elif event.key == K_UP or event.key == K_w:
                    plane.move_up()
                elif event.key == K_DOWN or event.key == K_s:
                    plane.move_down()
                elif event.key == K_SPACE:
                    print("shot")
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            plane.move_left()
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            plane.move_right()

        if pressed_keys[K_UP] or pressed_keys[K_w]:
            plane.move_up()
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            plane.move_down()

        clock.tick(300)

        window.blit(bg_image, (0, 0))
        plane.display()

        pygame.display.update()


if __name__ == '__main__':
    main()
