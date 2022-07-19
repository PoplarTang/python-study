import pygame

from pygame.locals import *
import sys
import time
import random

ENEMY_COUNT = 5
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768


class Unit:
    window = None

    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

class Map(Unit):
    pass

class Bullet(Unit):

    def auto_move(self):
        self.y -= 5
    def __del__(self):
        print("子弹销毁了 [%d,%d]" % (self.x, self.y))

    def is_hit_enemy(self, enemy):
        return pygame.Rect.colliderect(
            pygame.Rect(self.x, self.y, 20, 31),
            pygame.Rect(enemy.x, enemy.y, 100, 68)
        )

class Plane(Unit):
    def move_left(self):
        self.x -= 5
        if self.x < -60:
            self.x = -60

    def move_right(self):
        self.x += 5
        if self.x > SCREEN_WIDTH - 60:
            self.x = SCREEN_WIDTH - 60

    def move_up(self):
        self.y -= 5
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += 5
        if self.y > SCREEN_HEIGHT - 78:
            self.y = SCREEN_HEIGHT - 78

class HeroPlane(Plane):
    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.bullets = []

    def fire(self):
        """发射子弹"""
        bullet = Bullet("res/bullet_9.png", self.x + 60 - 10, self.y - 31)
        self.bullets.append(bullet)

    def displayBullets(self, enemies):
        """显示当前飞机发出的子弹"""
        for i in range(len(self.bullets) - 1, -1, -1):
            bullet = self.bullets[i]
            if bullet.y >= -31:
                bullet.display()
                bullet.auto_move()

                for enemy in enemies:
                    if bullet.is_hit_enemy(enemy):
                        enemy.isDestory = True
                        global score
                        score += 10
                        self.bullets.pop(i)
                        break
            else:
                self.bullets.pop(i)
                # del self.bullets[i]
                # self.bullets.remove(bullet)

class EnemyPlane(Plane):


    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.isDestory = False

    def auto_move(self):
        self.y += 5
        if self.y >= SCREEN_HEIGHT or self.isDestory:
            self.x, self.y = random.randint(0, SCREEN_WIDTH - 100), random.randint(-SCREEN_HEIGHT, -68)
            self.img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))
            self.isDestory = False

score = 0
def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Unit.window = window
    map = Map("res/img_bg_level_1.jpg", 0, 0)

    font = pygame.font.Font("res/SIMHEI.TTF", 35)

    plane = HeroPlane("res/hero2.png", 196, SCREEN_HEIGHT - 200)
    enemies = []
    for _ in range(ENEMY_COUNT):
        enemies.append(EnemyPlane("res/img-plane_%d.png" % random.randint(1, 7), random.randint(0, SCREEN_WIDTH - 100), random.randint(-SCREEN_HEIGHT, -68)))

    clock = pygame.time.Clock()

    while True:
        handleEvent(plane)

        map.display()
        plane.display()
        plane.displayBullets(enemies)

        for enemy in enemies:
            enemy.display()
            enemy.auto_move()

        text_obj = font.render("得分: %d" % score, 1, (255, 255, 255))
        window.blit(text_obj, (20, 20))

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
