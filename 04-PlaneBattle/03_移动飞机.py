import pygame
from pygame.locals import *
import sys
import time
from collections import deque

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

time_latest = None
time_arr = deque([])

def calc_dps():
    """
    每秒多少帧 60dps
    1 / 最近10帧的平均间隔
    :return: 帧数
    """
    global time_latest
    global time_arr
    current = time.time()

    if not time_latest:
        time_latest = time.time()
    else:
        duration = current - time_latest
        time_arr.append(duration)
        time_latest = current
        if len(time_arr) > 10:
            time_arr.popleft()
            average = sum(time_arr) / len(time_arr)
            dps = round(1 / average)
            print(dps)

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("res/img_bg_level_1.jpg")
    hero = pygame.image.load("res/hero2.png")

    # 计算坐标
    hero_x = 196
    hero_y = 500

    clock = pygame.time.Clock()

    while True:

        calc_dps()
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
                    hero_x -= 5
                    print("left")
                elif event.key == K_RIGHT or event.key == K_d:
                    hero_x += 5
                    print("right")
                elif event.key == K_UP or event.key == K_w:
                    hero_y -= 5
                    print("up")
                elif event.key == K_DOWN or event.key == K_s:
                    hero_y += 5
                    print("down")
                elif event.key == K_SPACE:
                    print("shot")
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            hero_x -= 2
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            hero_x += 2

        if pressed_keys[K_UP] or pressed_keys[K_w]:
            hero_y -= 2
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            hero_y += 2

        clock.tick(300)

        window.blit(bg_image, (0, 0))
        window.blit(hero, (hero_x, hero_y))

        pygame.display.update()
        # time.sleep(0.01)

if __name__ == '__main__':
    main()
