import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768


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


if __name__ == '__main__':
    main()
