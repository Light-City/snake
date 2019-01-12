
# 定义蛇与食物的位置坐标
import random
import sys

import pygame
from pygame.locals import *
BLACK = (0, 0, 0)

# 设定蛇与食物坐标
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dupli(self):
        return Point(self.x,self.y)

# 开始结束类
class startOrEnd(object):
    def __init__(self,window,score,width):
        self.window = window
        self.score = score
        self.width = width
    def start_Game(self,window):
        font = pygame.font.Font('font-score.ttf', 40)
        tip = font.render("按任意键开始您的游戏之旅~~",True,(255, 105, 225))
        pygame.mixer.music.load('main.mp3')
        pygame.mixer.music.play(-1)
        window.fill((255,255,255))
        game_start = pygame.image.load('game_start.png')
        window.blit(game_start, (0,0))
        window.blit(tip, (200, 420))
        pygame.display.update()
        while True:  # 键盘监听事件
            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT:
                      self.game_Terminal()
                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        self.game_Terminal()
                    else:
                        pygame.mixer.music.stop()
                        return  # 结束此函数, 开始游戏


        font = pygame.font.Font('font-score.ttf', 30)
        tip = font.render('按Q或者ESC退出游戏, 按任意键重新开始游戏~', True, (255, 105, 225))
        scoreTotal = font.render('您本次总成绩为: %s分' % score, True, BLACK)
        game_over = pygame.image.load('game_over.png')
        window.blit(game_over, (0, 0))
        window.blit(tip, (50, 420))
        window.blit(scoreTotal, (250,0))
        pygame.display.update()

        while True:  # 键盘监听事件
            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT:
                    self.game_Terminal() # 终止程序
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_q:  # 终止程序
                        self.game_Terminal()  # 终止程序
                    else:
                        pygame.mixer.music.load('bm.mp3')
                        pygame.mixer.music.play(-1)
                        return  # 结束此函数, 重新开始游戏

    def game_Terminal(self):
        pygame.quit()
        sys.exit()

    # def music_Over(self):
    #     pygame.mixer.music.stop()

    def game_Over(self, window, score):
        pygame.mixer.music.stop()

        font = pygame.font.Font('font-score.ttf', 30)
        tip = font.render('按Q或者ESC退出游戏, 按任意键重新开始游戏~', True, (255, 105, 225))
        scoreTotal = font.render('您本次总成绩为: %s分' % score, True, BLACK)
        game_over = pygame.image.load('game_over.png')
        window.blit(game_over, (0, 0))
        window.blit(tip, (50, 420))
        window.blit(scoreTotal, (250, 0))
        pygame.display.update()

        while True:  # 键盘监听事件
            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT:
                    self.game_Terminal()  # 终止程序
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_q:  # 终止程序
                        self.game_Terminal()  # 终止程序
                    else:
                        pygame.mixer.music.load('bm.mp3')
                        pygame.mixer.music.play(-1)
                        return  # 结束此函数, 重新开始游戏

    # 显示成绩
    def show_score(self, window, score):
        font = pygame.font.Font('font-score.ttf', 30)
        scoreWindow = font.render('Score: %s' % score, True, BLACK)
        scoreRect = scoreWindow.get_rect()
        scoreRect.topright = (self.width - 20, 10)
        window.blit(scoreWindow, scoreRect)

# 食物类
class Food(object):
    def __init__(self,column,row):
        # 食物颜色
        food_color = (255, 255, 0)
        self.column = column
        self.row = row
        self.food_color = food_color
    # 生成食物
    def gen_food(self, snake_head, snake_list):
        # 食物跟蛇是否碰到了
        while True:
            pos = Point(random.randint(0, self.column - 1), random.randint(0, self.row - 1))

            is_collision = False
            if snake_head.x == pos.x and snake_head.y == pos.y:
                is_collision = True
            # 蛇身子
            for snake in snake_list:
                if snake.x == pos.x and snake.y == pos.y:
                    is_collision = True
                    break
            if not is_collision:
                break
        return pos

# 蛇类
class Snake(object):
    def __init__(self,column,row):
        self.column = column
        self.row = row


    # 蛇的属性
    def SnakeAttr(self):
        # 设置默认蛇头朝向
        direct = 'left'
        # 初始蛇长
        snake_list = [
        ]
        W, H, COL, ROW = Map().genMap()
        # 蛇初始位置
        snake_head = Point(int(ROW / 2), int(COL / 2))
        # 蛇头颜色
        snake_head_color = (0, 128, 128)
        # 蛇身颜色
        snake_body_color = (200, 200, 200)
        return direct,snake_list,snake_head,snake_head_color,snake_body_color

    # 蛇吃食物
    def eatFood(self):
        map = Map()
        W, H, COL, ROW = map.genMap()
        fd = Food(COL, ROW)
        direct, snake_list,snake_head, snake_head_color, snake_body_color = self.SnakeAttr()
        # 食物颜色
        food_color = fd.food_color
        # 背景颜色
        bg_color = map.bg_color
        # 设置默认蛇头朝向
        direct = direct
        # 初始蛇长
        snake_list = snake_list
        # 定义食物
        food = fd.gen_food(snake_head, snake_list)
        # window
        size = (W, H)
        pygame.init()
        window = pygame.display.set_mode(size)
        pygame.display.set_caption("光城的贪吃蛇")
        # 设置退出flag
        q = False
        # 游戏时间控制
        clock = pygame.time.Clock()
        score = 0
        start_end = startOrEnd(window, score, W)
        start_end.start_Game(window)
        pygame.mixer.music.load('bm.mp3')
        pygame.mixer.music.play(-1)
        while not q:
            # 处理事件,游戏退出
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    q = True
                elif event.type == pygame.KEYDOWN:
                    # print(event)
                    if event.key == 273 or event.key == 119:
                        if direct == 'left' or direct == 'right':
                            direct = 'up'
                    elif event.key == 274 or event.key == 115:
                        if direct == 'left' or direct == 'right':
                            direct = 'down'
                    elif event.key == 276 or event.key == 97:
                        if direct == 'up' or direct == 'down':
                            direct = 'left'
                    elif event.key == 275 or event.key == 100:
                        if direct == 'up' or direct == 'down':
                            direct = 'right'

            # 蛇吃食物
            eat = (snake_head.x == food.x and snake_head.y == food.y)
            if eat:
                food = fd.gen_food(snake_head, snake_list)
                pygame.display.update()
            # 处理蛇身
            # 头插入list前面中，最后一个删掉
            snake_list.insert(0, snake_head.dupli())

            if not eat:
                snake_list.pop()

            if direct == 'left':
                snake_head.x -= 1
            elif direct == 'right':
                snake_head.x += 1
            elif direct == 'up':
                snake_head.y -= 1
            elif direct == 'down':
                snake_head.y += 1

            # 检测，撞墙与撞自己
            is_dead = False
            if snake_head.x < 0 or snake_head.y < 0 or snake_head.x >= COL or snake_head.y >= ROW:
                is_dead = True

            for snake in snake_list:
                if snake_head.x == snake.x and snake_head.y == snake.y:
                    is_dead = True
                    break

            if is_dead:
                q = True

            # 渲染
            # 使用RGB颜色
            # pygame.draw.rect(window,(255,255,255),(0,0,W,H))
            window.fill(bg_color)

            # 绘制

            for snake_body in snake_list:
                rect(window, snake_body, snake_body_color)
            rect(window, snake_head, snake_head_color)
            rect(window, food, food_color)
            # 右上角显示分数
            start_end.show_score(window, len(snake_list))

            # flip在这里表示让出控制权，交给系统
            pygame.display.flip()
            # 设置帧频
            clock.tick(10)

            # 死亡处理
            if is_dead == True:
                start_end.game_Over(window, len(snake_list))
                is_dead = False
                q = False
                snake_head = Point(int(ROW / 2), int(COL / 2))
                snake_list.clear()


class Map(object):
    def __init__(self):
        # 背景色
        bg_color = (255, 255, 255)
        self.bg_color = bg_color
    def genMap(self):
        W = 800
        H = 471

        ROW, COL = 30, 40  # 每个格子宽度=800/80 每行高度=600/60
        return  W,H,COL,ROW



# 绘制
def rect(window, point, color):
    map = Map()
    width, height, column, row = map.genMap()
    cell_width = width / column
    cell_height = height / row
    x = point.x * cell_width
    y = point.y * cell_height
    pygame.draw.rect(window, color, (x, y, cell_width, cell_height))

W, H, COL, ROW = Map().genMap()
s = Snake(COL, ROW)
s.eatFood()