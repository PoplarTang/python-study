import pygame, sys, random

SCREEN, dirction_node = 600, {pygame.K_LEFT: ['left', -25],
                              pygame.K_RIGHT: ['right', 25],
                              pygame.K_UP: ['top', -25],
                              pygame.K_DOWN: ['top', 25]}  # 屏幕尺寸，移动的定义


class Snake:  # 蛇类
    def __init__(self):  # 初始化各种需要的属性 [开始时默认向右/身体块x5]
        self.dirction = pygame.K_RIGHT
        self.body = []
        for _ in range(5):
            self.add_node()

    def add_node(self):
        left_top = (self.body[0].left, self.body[0].top) if self.body else (0, 0)
        node = pygame.Rect((left_top) + (25, 25))  # 随时增加蛇块
        head_dirction, head_forward = dirction_node[self.dirction]
        value = getattr(node, head_dirction) + head_forward
        setattr(node, head_dirction, value)

        if node.x >= SCREEN:
            node.x -= SCREEN
        elif node.x < 0:
            node.x += SCREEN

        if node.y >= SCREEN:
            node.y -= SCREEN
        elif node.y < 0:
            node.y += SCREEN

        self.body.insert(0, node)

    def is_dead(self):
        body_h = self.body[0]
        if body_h.x not in range(SCREEN) or body_h.y not in range(SCREEN) or body_h in self.body[1:]:  # 撞墙、撞自己则死亡
            return True

    def move(self):
        self.add_node()
        self.body.pop()

    def change_direction(self, curkey):  # 改变方向 但是左右、上下不能被逆向改变
        LR, UD = [pygame.K_LEFT, pygame.K_RIGHT], [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if not ((curkey in LR) and (self.dirction in LR) or (curkey in UD) and (self.dirction in UD)):
                self.dirction = curkey


class Food:  # 食物类
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)

    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allpos = [pos for pos in range(75, SCREEN - 75, 25)]  # 生成的食物距离墙在75 ~ SCREEN-55 之间
            self.rect.left, self.rect.top = random.choice(allpos), random.choice(allpos)


def show_text(screen, pos, text, color, font_size=30):
    cur_font = pygame.font.SysFont("SimHei", font_size)  # 设置文字样式
    text_fmt = cur_font.render(text, True, color)  # 设置文字内容
    screen.blit(text_fmt, pos)  # 绘制文字


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN, SCREEN))
    pygame.display.set_caption('贪吃蛇')
    snake, food, clock, scores, isdead = Snake(), Food(), pygame.time.Clock(), 0, False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)
                if event.key == pygame.K_SPACE and isdead:  # 死后按space重新
                    return main()
        screen.fill((255, 255, 255))
        if not isdead:  # 画蛇身 / 每一步+1分
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen, (144, 238, 144), rect)
        isdead = snake.is_dead()  # 显示死亡文字
        if isdead:
            show_text(screen, (150, 200), '翻车了！', (227, 29, 18), 80)
            show_text(screen, (50, 320), '按空格键重试...', (0, 0, 22))
        if food.rect == snake.body[0]:  # 当食物rect与蛇头重合,吃掉 -> Snake增加一个Node
            scores += 1  # 食物处理 / 吃到+1分
            food.remove()
            snake.add_node()
        food.set()  # 食物投递
        pygame.draw.rect(screen, (233, 150, 122), food.rect)
        speed = 10 + scores * 3.5 if scores else 10  # 蛇移动速度
        show_text(screen, (20, 550), '关卡:' + str(scores) + '   速度:' + str(speed) + 'KM/h', (0, 0, 205))  # 显示得分和速度
        pygame.display.update()
        clock.tick(speed)


main()
