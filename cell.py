import pygame



class Cell:
    '''格子的类'''

    def __init__(self, row, col, gs_game):
        '''初始化格子并设置其所在行列'''
        self.settings = gs_game.settings
        self.screen = gs_game.screen
        self.gs_game = gs_game
        
        #格子所在的行列
        self.row = row
        self.col = col
        
        #计算各级的大小
        self.cell_width = self.settings.screen_width / self.settings.COL
        self.cell_height = self.settings.screen_height / self.settings.ROW
        
        #计算格子的坐标
        self.x = self.col * self.cell_width
        self.y = self.row * self.cell_height
        
    #复制当前格点
    def copy(self):
        return Cell(row=self.row, col=self.col, gs_game=self.gs_game)

    #渲染格子
    def draw_cell(self, color):
        
        #计算格子的坐标
        self.x = self.col * self.cell_width
        self.y = self.row * self.cell_height
        
        pygame.draw.rect(self.screen, color, (self.x,self.y,self.cell_width,self.cell_height))