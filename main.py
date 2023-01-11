import sys

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from snake import Snake
from food import Food


class GluttonousSnake:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''

        pygame.init()
        self.settings = Settings()
        '''
        # 全屏模式
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height
        '''

        self.screen = pygame.display.set_mode(self.settings.screen_size)

        pygame.display.set_caption("Glottonous Snake")  #设置标题

        #创建一个用于存储游戏统计信息的实例
        #   并创建记分牌
        self.stats = GameStats(self)
        self.score_board = Scoreboard(self)

        self.snake = Snake(self)

        #创建粮仓
        self.granary = pygame.sprite.Group()

        self._creat_granary()

        #创建 Play 按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        '''开始游戏的主循环'''

        clock = pygame.time.Clock()

        while True:
            self._check_events()

            if self.stats.game_active:
                self._check_eat_food()
                self.snake.move_snake(self.is_eat)
                self.snake.update()
                self._check_snake_hit()

            self._update_screen()

            clock.tick(self.settings.fps)

    def _check_events(self):
        '''监视键盘和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #点击鼠标
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                #按下键盘
                self._check_keydown_events(event)

            elif event.type == pygame.MOUSEMOTION:
                #鼠标移动控制
                self._check_mousemotion(event)

    def _check_mousemotion(self, mouse_pos):
        #通过鼠标移动控制小蛇
        if self.stats.game_active:
            x = mouse_pos.rel[0]
            y = mouse_pos.rel[1]
            #通过x和y的绝对值比较，判断是横轴移动还是数轴移动

            if abs(x) > abs(y):
                #横轴移动
                if x > 0:
                    if not self.snake.direction == 'left':
                        self.snake.direction = 'right'
                else:
                    if not self.snake.direction == 'right':
                        self.snake.direction = 'left'
            else:
                #数轴移动
                if y < 0:
                    if not self.snake.direction == 'down':
                        self.snake.direction = 'up'
                else:
                    if not self.snake.direction == 'up':
                        self.snake.direction = 'down'

    def _check_play_button(self, mouse_pos):
        '''在玩家单击 Play 按钮时开始新游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.score_board.prep_score()

            #清空食物
            self.granary.empty()
            #生成新的食物
            self._creat_granary()

            #重置蛇
            self.snake.initial_snake()

            #隐藏鼠标光标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        '''响应按键'''
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            if not self.snake.direction == 'down':
                self.snake.direction = 'up'
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if not self.snake.direction == 'up':
                self.snake.direction = 'down'
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if not self.snake.direction == 'right':
                self.snake.direction = 'left'
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if not self.snake.direction == 'left':
                self.snake.direction = 'right'

    def _creat_granary(self):
        '''创建食物，并将其加入编组 granary 中'''
        is_not_full = len(self.granary) < self.settings.food_number
        while is_not_full:
            is_not_full = len(self.granary) < self.settings.food_number
            if is_not_full:
                new_food = Food(self)
                self.granary.add(new_food)

    def _check_eat_food(self):
        '''相应蛇吃到食物'''

        self.is_eat = False

        #检查蛇头是否与 granary 中的食物坐标相同
        for food in self.granary.sprites():
            if self.snake.head.row == food.row and self.snake.head.col == food.col:

                self.is_eat = True

                #将食物从 granary 中删除
                self.granary.remove(food)

                #重新填充食物
                self._creat_granary()

                #分数+1
                self.stats.score += 1

                #重新渲染分数
                self.score_board.prep_score()
                self.score_board.check_high_score()

                break

    def _check_snake_hit(self):
        '''检测蛇碰撞'''
        #1.撞墙
        if self.snake.head.col < 0 or self.snake.head.row < 0 or self.snake.head.col >= self.settings.COL or self.snake.head.row >= self.settings.ROW:
            self._snake_dead()
        #2.头碰到身体
        for cell in self.snake.body:
            if self.snake.head.col == cell.col and self.snake.head.row == cell.row:
                self._snake_dead()
                break

    def _snake_dead(self):
        '''响应蛇死亡'''
        self.stats.game_active = False

        #恢复显示鼠标光标
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        #每次循环都重绘屏幕
        self.screen.fill(self.settings.bg_color)

        self.snake.draw_snake()

        for food in self.granary.sprites():
            food.draw_food()

        #显示得分
        self.score_board.show_score()

        #如果游戏处于非活动状态，就绘制 Play 按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        #让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    gs = GluttonousSnake()
    gs.run_game()