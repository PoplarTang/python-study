"""
贪吃蛇游戏
"""

import random
import time

import pygame
import sys
from constants import *
from models import Snake, Food
from socket_library.models import Msg, MsgType
from socket_library.socketio_client import *


class Game:

    def __init__(self, title="PyGame"):
        # 启动SocketIOClientThread
        self.client_thread = SocketIOClientThread(
            url='http://localhost:5000',
            message_callback=self.handle_message
        )
        self.client_thread.start()

        # 初始化 Pygame
        pygame.init()
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置游戏窗口的标题
        pygame.display.set_caption(title)
        # 设置图标
        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)

        # 加载飞机图片
        self.bg_image = pygame.image.load('img/bg.png')
        # 将图片缩放为指定大小
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # 显示时钟
        self.clock = pygame.time.Clock()

    def handle_message(self, type, data):
        print("收到消息:", type, data)
        if type == CALLBACK_CONNECTED:
            data = {
                "name": "转转小王子",
                "color": "blue",
            }
            msg = Msg(MsgType.CLIENT_INFO, data=data)
            self.client_thread.send_message(msg.to_dict())

    def gen_food_pos(self, snake):
        # 生成随机食物的函数
        # 无限循环，直到生成不与蛇身重叠的食物位置
        # 随机生成x和y的坐标
        # 判断生成的位置是否与蛇身重叠，若重叠则重新生成
        # 返回生成的x和y坐标
        while True:
            x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1)
            y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1)
            # 判断是否和蛇重叠
            if pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE) not in snake.body:
                break
        return x, y

    def start(self):
        game_over = False
        score = 0
        fps = 60

        # 蛇移动的时间间隔s
        move_period_base = 0.2
        move_period = move_period_base

        # 记录上一帧时间
        last_frame_time = time.time()

        snake = Snake((3, 3))
        food = Food(*self.gen_food_pos(snake))
        # 避免程序结束
        while True:
            # 处理事件 -------------------------------------------------
            new_direction = None
            event_list = pygame.event.get()
            for event in event_list:
                # 退出事件类型
                if event.type == locals.QUIT:
                    self.exit_game()
                elif event.type == locals.KEYDOWN:  # 键盘按下的事件
                    # 判断按下的是哪个键
                    if event.key == locals.K_ESCAPE:
                        self.exit_game()
                        return
                    elif game_over:
                        self.start()
                        return
                    elif snake.is_change_available(event.key):
                        new_direction = event.key

            if new_direction is not None:
                snake.change_direction(new_direction)

            # 进行游戏 -------------------------------------------------
            # 判断和最后一次刷新的时间间隔是否大于 move_period
            cur_time = time.time()
            if not game_over and (cur_time - last_frame_time > move_period):
                # 更新上一帧时间
                last_frame_time = cur_time
                # 判断游戏是否结束

                # 进行移动
                snake.move()

                # 发送消息, 通知服务器更新蛇的位置
                self.send_snake_position(snake)

                # 判断是否撞墙
                if snake.body[0].x < 0 or snake.body[0].x >= SCREEN_WIDTH or \
                        snake.body[0].y < 0 or snake.body[0].y >= SCREEN_HEIGHT:
                    game_over = True

                # 判断是否撞到身体
                for segment in snake.body[1:]:
                    if snake.body[0] == segment:
                        game_over = True

                # 判断是否吃到食物
                if snake.body[0] == food.rect:
                    snake.grow()
                    food = Food(*self.gen_food_pos(snake))
                    score = len(snake.body) - 3

                    fixed_score = min(score, 50)
                    # 根据score加快移动速度 score在[0, 100] 对应移动延时的比例为 [1.0, 0.6]
                    move_period = move_period_base * (1 - 0.4 * fixed_score / 50)

            # 绘制画面---------------------------------------------------
            self.screen.blit(self.bg_image, (0, 0))
            # self.screen.fill(COLOR_BLACK)
            # 绘制铺满屏幕的横竖网格线
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                pygame.draw.line(self.screen, COLOR_GRAY, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                pygame.draw.line(self.screen, COLOR_GRAY, (0, y), (SCREEN_WIDTH, y))

            # 绘制蛇身
            snake.draw(self.screen)
            # 绘制食物
            food.draw(self.screen)

            # 绘制游戏信息
            if not game_over:
                # 绘制得分
                self.show_text((10, 10), "得分：" + str(score), COLOR_RED, 18)
                # 绘制帧率
                self.show_text((SCREEN_WIDTH - 120, 10),
                               "fps：" + str(int(self.clock.get_fps())),
                               COLOR_RED, 18)
                # 绘制速度
                speed = 1 / move_period
                self.show_text((SCREEN_WIDTH - 120, 30),
                               "速度：" + str(round(speed, 1)) + "格/s",
                               COLOR_RED, 18)
            else:
                x, y = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4
                self.show_text((x, y), "游戏结束", COLOR_RED, 64)
                self.show_text((x, y + 64), "按ESC退出游戏", COLOR_RED, 18)
                self.show_text((x, y + 96), "按任意键重新开始", COLOR_RED, 18)
                self.show_text((x, y + 128), "得分：" + str(score), COLOR_RED, 18)

            # 刷新屏幕 ------------------------------------------------------------
            pygame.display.update()

            self.clock.tick(fps)  # 10帧/s  - 每次确保跑足 1/10 s 的时间
            # self.clock.tick(8 + min(score, 100))  # 10帧/s  - 每次确保跑足 1/10 s 的时间
            # print("fps: ", self.clock.get_fps())

    def show_text(self, pos, text, color, font_size=30):
        cur_font = pygame.font.SysFont("SimHei", font_size)  # 设置文字样式
        text_surface = cur_font.render(text, True, color)  # 设置文字内容
        self.screen.blit(text_surface, pos)  # 绘制文字

    @staticmethod
    def exit_game():
        # 退出界面
        pygame.display.quit()
        # sys退出
        sys.exit()

    def send_snake_position(self, snake: Snake):
        """
        发送蛇的位置给服务器
        :param snake:
        :return:
        """
        # 拼接蛇的位置
        snake_body_list = snake.body_list()

        # 构造Msg消息
        msg = Msg(code=MsgType.CLIENT_SNAKE_POSITION, data=snake_body_list)

        # print("msg:", msg)
        # 发送消息
        self.client_thread.send_message(msg.to_dict())


def main():
    game = Game("贪吃蛇游戏")
    game.start()


if __name__ == '__main__':
    main()
