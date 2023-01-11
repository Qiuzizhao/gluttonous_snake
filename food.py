import pygame
from pygame.sprite import Sprite

import random

from cell import Cell


class Food(Sprite):
    '''表示单个食物的类'''

    def __init__(self, gs_game):
        '''初始化食物并设置其起始位置'''
        super().__init__()
        self.screen = gs_game.screen
        self.settings = gs_game.settings
        
        self.granary = gs_game.granary

        #随机生成食物所在的行列
        #判断食物是否生成在蛇上
        while True:

            self.row = random.randint(1, self.settings.ROW - 2)
            self.col = random.randint(1, self.settings.COL - 2)

            is_collision = False
            #判断是否在蛇头
            if self.row == gs_game.snake.head.row and self.col == gs_game.snake.head.col:
                is_collision = True

            #判断是否在蛇身
            for snake_body_cell in gs_game.snake.body:
                if self.row == snake_body_cell.row and self.col == snake_body_cell.col:
                    is_collision = True
                    break
                
            #判断是当前位置是否已经存在食物
            for exist_food in self.granary:
                if self.row == exist_food.row and self.col == exist_food.col:
                    is_collision = True
                    break

            if not is_collision:
                break

        #生成cell
        self.cell = Cell(self.row, self.col, gs_game)

    def draw_food(self):
        '''在屏幕上绘制食物'''
        self.cell.draw_cell(self.settings.food_color)
