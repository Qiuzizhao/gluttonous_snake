import pygame.font


class Settings:
    '''存储《贪吃蛇》游戏中所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''

        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (255, 255, 255)

        #行列数设置
        self.ROW = self.screen_height/20
        self.COL = self.screen_width/20

        #帧频设置
        self.fps = 30  #可用于改变蛇移动速度

        #食物设置
        self.food_color = (255, 255, 0)  #食物颜色，默认黄
        self.food_number = 3  #食物数量

        #蛇设置
        self.snake_body_color = (200, 200, 200)  #蛇身颜色，默认淡灰
        self.snake_head_color = (0, 128,128)  #蛇头颜色，默认浅蓝
        self.snake_init_length = 3  #蛇身的初始长度
        self.snake_init_pos = (int(self.ROW / 2), int(self.COL / 2))  #蛇头的初始位置
        self.snake_init_direction = 'left'  #初始运动方向，默认为左

        #按钮设置
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)

        #得分板设置
        self.scoreboard_text_color = (30, 30, 30)
        self.scoreboard_font = pygame.font.SysFont(None, 48)
