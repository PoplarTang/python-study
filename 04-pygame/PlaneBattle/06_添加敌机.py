import pygame

from pygame.locals import *
import sys
import time
import random

ENEMY_COUNT = 5
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
    def __del__(self):
        print("子弹销毁了" + str(self.x))


class Plane(Unit):
    def __init__(self, img_path, x, y, window):
        super().__init__(img_path, x, y, window)
        self.bullets = []

    def fire(self):
        """发射子弹"""
        bullet = Bullet("res/bullet_9.png", self.x + 60 - 10, self.y - 31, self.window)
        self.bullets.append(bullet)

    def displayBullets(self):
        """显示当前飞机发出的子弹"""
        for i in range(len(self.bullets) - 1, -1, -1):
            bullet = self.bullets[i]
            if bullet.y >= -31:
                bullet.display()
                bullet.move_up()
            else:
                self.bullets.pop(i)
                # del self.bullets[i]
                # self.bullets.remove(bullet)

class Enemy(Unit):
    def auto_move(self):
        self.y += 5
        if self.y >= SCREEN_HEIGHT:
            self.x, self.y = random.randint(0, SCREEN_WIDTH - 100), random.randint(-SCREEN_HEIGHT, -68)
            self.img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("res/img_bg_level_1.jpg")

    plane = Plane("res/hero2.png", 196, SCREEN_HEIGHT - 200, window)

    enemies = []
    for _ in range(ENEMY_COUNT):
        enemies.append(Enemy("res/img-plane_%d.png" % random.randint(1, 7), random.randint(0, SCREEN_WIDTH - 100), random.randint(-SCREEN_HEIGHT, -68), window))

    clock = pygame.time.Clock()

    while True:
        handleEvent(plane)

        window.blit(bg_image, (0, 0))
        plane.display()
        plane.displayBullets()

        for enemy in enemies:
            enemy.display()
            enemy.auto_move()

        pygame.display.update()

        clock.tick(100)
        # time.sleep(0.02)


def handleEvent(plane):
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
                plane.fire()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        plane.move_left()
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        plane.move_right()
    if pressed_keys[K_UP] or pressed_keys[K_w]:
        plane.move_up()
    elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
        plane.move_down()

        # if pressed_keys[K_SPACE]:
        #     plane.fire()


if __name__ == '__main__':
    main()
