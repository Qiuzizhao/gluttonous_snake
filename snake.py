from cell import Cell


class Snake:
    '''管理蛇的类'''

    def __init__(self, gs_game):
        '''初始化蛇并设置其初始项'''
        self.gs_game = gs_game
        self.screen = gs_game.screen
        self.settings = gs_game.settings

        #初始化蛇
        self.initial_snake()

    def center_snake(self):
        '''让蛇头回归初始位置'''
        self.head = Cell(self.settings.snake_init_pos[0],self.settings.snake_init_pos[1], self.gs_game)

    def initial_snake(self):
        '''重置蛇'''

        #定义蛇头,初始位置在屏幕中间
        self.center_snake()

        #定义蛇身
        self.body = []
        for i in range(self.settings.snake_init_length):
            temp = Cell(self.head.row, self.head.col + i + 1, self.gs_game)
            self.body.append(temp)
            
        #蛇的运动方向
        self.direction = self.settings.snake_init_direction

    def draw_snake(self):
        '''绘制蛇'''
        #绘制蛇头
        self.head.draw_cell(self.settings.snake_head_color)
        #绘制蛇身
        for i in self.body:
            i.draw_cell(self.settings.snake_body_color)
            
    def update(self):
        '''根据 direction 移动并调整位置'''
        if self.direction == 'left':
            self.head.col -=1
        elif self.direction == 'right':
            self.head.col +=1
        elif self.direction == 'up':
            self.head.row -=1
        elif self.direction == 'down':
            self.head.row +=1
            
    def move_snake(self,is_eat):
        '''处理蛇的移动'''
        #把原来的头插入到身体最前方
        self.body.insert(0,self.head.copy())
        
        #如果没有吃到食物，则把身体最后一项删除
        if not is_eat:
            self.body.pop()
            
