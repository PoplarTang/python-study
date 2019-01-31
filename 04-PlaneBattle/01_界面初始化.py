import pygame

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_image = pygame.image.load("res/img_bg_level_1.jpg")

    width = bg_image.get_width()
    height = bg_image.get_height()
    print(width, height)

    window.blit(bg_image, (0, 0))

    pygame.display.update()


if __name__ == '__main__':
    main()
