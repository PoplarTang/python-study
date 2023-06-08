import pygame
from constants import *


class Food:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_BLUE, self.rect, border_radius=5)


class Snake:

    def __init__(self, head=(0, 0)):
        self.direction = locals.K_RIGHT
        self.can_cross_wall = True
        head_img = pygame.image.load('img/head-red.png')
        self.head_img = pygame.transform.scale(head_img, (BLOCK_SIZE, BLOCK_SIZE))

        self.body = [pygame.Rect(head[0] * BLOCK_SIZE, head[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)]
        for _ in range(2):
            self.grow()

    def cross_wall_enable(self, enable):
        self.can_cross_wall = enable

    def is_change_available(self, new_key):
        """
        判断是否可以改变方向
        :param new_key:
        :return:
        """
        if new_key not in direction_dict.keys():
            return False

        LR, UD = [locals.K_LEFT, locals.K_RIGHT], [locals.K_UP, locals.K_DOWN]
        # 如果当前和新的在同一个组里，则不更新
        if (new_key in LR and self.direction in LR) or (new_key in UD and self.direction in UD):
            return False
        return True

    def change_direction(self, new_key):
        self.direction = new_key

    def grow(self):
        # 将最后一个节点复制一份，添加到body中
        new_node = self.body[-1].copy()
        self.body.append(new_node)

    def move(self):
        # 初始化身体块
        new_node = self.body[0].copy()
        # 把新node根据方向移动一格
        new_change = direction_dict[self.direction]
        new_node.x += new_change[0] * BLOCK_SIZE
        new_node.y += new_change[1] * BLOCK_SIZE

        if self.can_cross_wall:
            # 如果超出界面，从另一侧出现
            self.cross_wall(new_node)

        self.body.insert(0, new_node)
        # 删除最后一个节点
        self.body.pop()

    def cross_wall(self, new_node):
        if new_node.x >= SCREEN_WIDTH:
            new_node.x -= SCREEN_WIDTH
        elif new_node.x < 0:
            new_node.x += SCREEN_WIDTH

        if new_node.y >= SCREEN_HEIGHT:
            new_node.y -= SCREEN_HEIGHT
        elif new_node.y < 0:
            new_node.y += SCREEN_HEIGHT  # 移除末尾

        # 打印头部坐标
        # print("Head: ", self.body[0].x, self.body[0].y)

    def draw(self, surface):
        for i, node in enumerate(self.body):
            # 将现有node收缩2像素绘制
            # draw_node = pygame.Rect(node.x + 2, node.y + 2, BLOCK_SIZE - 4, BLOCK_SIZE - 4)
            if i == 0:
                # pygame.draw.rect(surface, COLOR_RED, node, border_radius=3)
                new_img = pygame.transform.rotate(self.head_img, direction_angle_dict[self.direction])
                surface.blit(new_img, node)
            else:
                pygame.draw.rect(surface, COLOR_WHITE, node, border_radius=3)

    def body_list(self):
        snake_segments = [f"{segment.x},{segment.y}" for segment in self.body]
        return ";".join(snake_segments)
