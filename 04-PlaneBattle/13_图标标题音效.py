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
    size = None

    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()


class Map(Unit):
    def __init__(self, img_path, x, y):
        # super().__init__(img_path, x, y)
        self.img1 = pygame.image.load(img_path)
        self.img2 = pygame.image.load(img_path)
        self.x = x
        self.y = y

    def auto_move(self):
        self.y += 1
        if self.y > SCREEN_HEIGHT:
            self.y = 0

    def display(self):
        self.window.blit(self.img1, (self.x, self.y))
        self.window.blit(self.img2, (self.x, self.y - SCREEN_HEIGHT))


class Bullet(Unit):
    def auto_move(self):
        self.y -= 5

    def __del__(self):
        print("子弹销毁了 [%d,%d]" % (self.x, self.y))

    def is_hit_enemy(self, enemy):
        """
        判断和指定敌机是否碰撞
        :param enemy: 敌机
        """
        return pygame.Rect.colliderect(
            pygame.Rect(self.x, self.y, self.get_width(), self.get_height()),
            pygame.Rect(enemy.x, enemy.y, enemy.get_width(), enemy.get_height())
        )


class Plane(Unit):
    def move_left(self):
        self.x -= 5
        if self.x < -self.get_width() / 2:
            self.x = -self.get_width() / 2

    def move_right(self):
        self.x += 5
        if self.x > SCREEN_WIDTH - self.get_width() / 2:
            self.x = SCREEN_WIDTH - self.get_width() / 2

    def move_up(self):
        self.y -= 5
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += 5
        if self.y > SCREEN_HEIGHT - self.get_height():
            self.y = SCREEN_HEIGHT - self.get_height()


class HeroPlane(Plane):
    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.bullets = []
        self.is_hited = False
        self.anim_index = 0
        self.is_destroy = False

    def fire(self):
        """发射子弹"""
        bullet = Bullet("res/bullet_11.png", self.x + self.get_width() / 2 - 10, self.y - 31)
        self.bullets.append(bullet)

    def is_hit_enemy(self, enemy):
        """
        判断和指定敌机是否碰撞
        :param enemy: 敌机
        """
        return pygame.Rect.colliderect(
            pygame.Rect(enemy.x, enemy.y, enemy.get_width(), enemy.get_height()),
            pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        )

    def display(self, enemies):
        if self.is_destroy:
            print("我方挂啦!")
            self.is_destroy = False
            # 恢复飞机样式
            self.img, self.x, self.y = pygame.image.load("res/hero.png"), 196, SCREEN_HEIGHT - 200

        if self.is_hited:
            self.plane_down_anim()
        else:
            for enemy in enemies:
                if self.is_hit_enemy(enemy):
                    self.is_hited = True
                    enemy.is_hited = True
                    break

        super().display()

    def plane_down_anim(self):
        if self.anim_index >= 21:
            self.is_hited = False
            self.is_destroy = True
            self.anim_index = 0
            # 恢复飞机样式
            return

        self.img = pygame.image.load("res/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1

    def displayBullets(self, enemies):
        """显示当前飞机发出的子弹"""
        for i in range(len(self.bullets) - 1, -1, -1):
            bullet = self.bullets[i]
            if bullet.y >= -31:
                bullet.display()
                bullet.auto_move()

                for enemy in enemies:
                    if not enemy.is_hited and bullet.is_hit_enemy(enemy):
                        enemy.is_hited = True
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
        self.is_hited = False
        self.anim_index = 0
        self.is_destroy = False
        self.hit_sound = pygame.mixer.Sound("res/baozha.ogg")

    def plane_down_anim(self):
        if self.anim_index >= 21:
            self.is_hited = False
            self.is_destroy = True
            self.anim_index = 0
            # 恢复飞机样式
            return
        elif self.anim_index == 0:
            self.hit_sound.play()

        self.img = pygame.image.load("res/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1

    def display(self):
        if self.is_hited:
            self.plane_down_anim()
        super().display()

    def auto_move(self):
        self.y += 3
        if self.y >= SCREEN_HEIGHT or self.is_destroy:
            self.x, self.y = random.randint(0, SCREEN_WIDTH - 100), random.randint(-SCREEN_HEIGHT, -68)
            self.img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))
            self.is_destroy = False


score = 0


def main():
    pygame.init()
    pygame.display.set_caption("飞机大战 V1.0")

    pygame.display.set_icon(pygame.image.load("res/app.ico"))

    pygame.mixer.music.load("res/bg2.ogg")

    pygame.mixer.music.play(-1)
    # 游戏结束的音效（超级玛丽）
    # gameover_sound = pygame.mixer.Sound("res/gameover.wav")

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Unit.window = window

    map = Map("res/img_bg_level_%d.jpg" % random.randint(1, 5), 0, 0)

    font = pygame.font.Font("res/SIMHEI.TTF", 35)

    plane = HeroPlane("res/hero2.png", 196, SCREEN_HEIGHT - 200)
    enemies = []
    for _ in range(ENEMY_COUNT):
        enemies.append(EnemyPlane("res/img-plane_%d.png" % random.randint(1, 7), random.randint(0, SCREEN_WIDTH - 100),
                                  random.randint(-SCREEN_HEIGHT, -68)))

    clock = pygame.time.Clock()

    while True:
        handleEvent(plane)

        map.display()
        map.auto_move()

        plane.display(enemies)
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
