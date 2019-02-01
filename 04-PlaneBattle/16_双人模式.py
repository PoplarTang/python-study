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
    def __init__(self, img_path, host, **kwargs):
        self.img = pygame.image.load(img_path)
        self.x = host.x + kwargs["offset"]
        self.y = host.y - self.get_height()
        self.host = host

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
        self.score = 0

    def fire(self):
        if self.is_destroy:
            return
        """发射子弹"""
        bullet1 = Bullet("res/bullet_12.png", self, offset=0)
        bullet = Bullet("res/bullet_11.png", self, offset=self.get_width() / 2 - 10)
        bullet2 = Bullet("res/bullet_12.png", self, offset=self.get_width() - 20)
        self.bullets.append(bullet)
        self.bullets.append(bullet1)
        self.bullets.append(bullet2)

    def is_hit_enemy(self, enemy):
        if self.is_destroy:
            return False
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
            return
            # self.is_destroy = False
            # 恢复飞机样式
            # self.img, self.x, self.y = pygame.image.load("res/hero.png"), 196, SCREEN_HEIGHT - 200

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
                        bullet.host.score += 10
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


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("飞机大战 V1.0")

        pygame.display.set_icon(pygame.image.load("res/app.ico"))

        pygame.mixer.music.load("res/bg2.ogg")

        pygame.mixer.music.play(-1)
        # 游戏结束的音效（超级玛丽）
        self.gameover_sound = pygame.mixer.Sound("res/gameover.wav")

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        Unit.window = self.window

        self.map = Map("res/img_bg_level_%d.jpg" % random.randint(1, 5), 0, 0)

        self.font = pygame.font.Font("res/SIMHEI.TTF", 26)

        self.plane_player_1 = HeroPlane("res/hero.png", 156, SCREEN_HEIGHT - 200)
        self.plane_player_2 = HeroPlane("res/hero2.png", 236, SCREEN_HEIGHT - 200)
        self.enemies = []
        for _ in range(ENEMY_COUNT):
            self.enemies.append(EnemyPlane("res/img-plane_%d.png" % random.randint(1, 7),
                                           random.randint(0, SCREEN_WIDTH - 100),
                                           random.randint(-SCREEN_HEIGHT, -68)))

        self.clock = pygame.time.Clock()

    def draw_text(self, content, size, x, y):
        # font_obj = pygame.font.SysFont("simhei", size)
        font_obj = pygame.font.Font("res/SIMHEI.TTF", size)
        text = font_obj.render(content, 1, (255, 255, 255))
        self.window.blit(text, (x, y))

    def start(self):
        while True:
            # 处理游戏进行事件
            handleEvent(self.plane_player_1, self.plane_player_2)

            # 处理游戏进行渲染
            self.map.display()
            self.map.auto_move()

            self.plane_player_1.display(self.enemies)
            self.plane_player_1.displayBullets(self.enemies)

            self.plane_player_2.display(self.enemies)
            self.plane_player_2.displayBullets(self.enemies)

            for enemy in self.enemies:
                enemy.display()
                enemy.auto_move()

            self.window.blit(self.font.render("player1得分: %d" % self.plane_player_1.score, 1, (255, 255, 255)), (20, 20))
            self.window.blit(self.font.render("player2得分: %d" % self.plane_player_2.score, 1, (255, 255, 255)), (50, 20))

            pygame.display.update()

            self.clock.tick(100)

            # time.sleep(0.02)
            if self.plane_player_1.is_destroy and self.plane_player_2.is_destroy:
                break

        # 游戏凉凉, 让用户决定重新开始还是退出
        self.showInputOrder()

    def showInputOrder(self):

        pygame.mixer.music.stop()

        self.gameover_sound.play()

        self.map.display()
        self.draw_text("飞机大战", 40, SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 3)
        self.draw_text("按Enter开始游戏，Esc退出游戏.", 28, SCREEN_WIDTH / 3 - 140, SCREEN_HEIGHT / 2)
        pygame.display.update()
        self.handleOrderEvent()

        self.gameover_sound.stop()

    def handleOrderEvent(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                        pygame.quit()
                        return
                    if event.key == K_RETURN:
                        self.waiting_order = False
                        global score
                        score = 0
                        return


def main():
    while True:
        game = Game()
        game.start()


def handleEvent(player1, player2):
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

            if event.key == K_a:
                player1.move_left()
            elif event.key == K_d:
                player1.move_right()
            elif event.key == K_w:
                player1.move_up()
            elif event.key == K_s:
                player1.move_down()
            elif event.key == K_SPACE:
                player1.fire()

            if event.key == K_LEFT:
                player2.move_left()
            elif event.key == K_RIGHT:
                player2.move_right()
            elif event.key == K_UP:
                player2.move_up()
            elif event.key == K_DOWN:
                player2.move_down()
            elif event.key == K_KP_PLUS or event.key == K_KP_ENTER:
                player2.fire()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a]:
        player1.move_left()
    elif pressed_keys[K_d]:
        player1.move_right()
    if pressed_keys[K_w]:
        player1.move_up()
    elif pressed_keys[K_s]:
        player1.move_down()

    if pressed_keys[K_LEFT] :
        player2.move_left()
    elif pressed_keys[K_RIGHT] :
        player2.move_right()
    if pressed_keys[K_UP] :
        player2.move_up()
    elif pressed_keys[K_DOWN] :
        player2.move_down()

        # if pressed_keys[K_SPACE]:
        #     plane.fire()


if __name__ == '__main__':
    main()
