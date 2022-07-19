import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("res/img_bg_level_1.jpg")


    window.blit(bg_image, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT: # 鼠标点击右上角退出按钮
                print("quit")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("quit")
                    pygame.quit()
                    sys.exit()
                elif event.key == K_LEFT or event.key == K_a:
                    print("left")
                elif event.key == K_RIGHT or event.key == K_d:
                    print("right")
                elif event.key == K_UP or event.key == K_w:
                    print("up")
                elif event.key == K_DOWN or event.key == K_s:
                    print("down")
                elif event.key == K_SPACE:
                    print("shot")

        pygame.display.update()


if __name__ == '__main__':
    main()
