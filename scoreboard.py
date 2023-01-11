import pygame.font

from snake import Snake


class Scoreboard:
    '''显示得分信息的类'''

    def __init__(self, gs_game):
        '''初始化显示得分涉及的属性'''
        self.gs_game = gs_game
        self.screen = gs_game.screen
        self.screen_rect = gs_game.screen.get_rect()
        self.settings = gs_game.settings
        self.stats = gs_game.stats

        #显示得分信息时使用的字体设置
        self.text_color = self.settings.scoreboard_text_color
        self.font = self.settings.scoreboard_font

        #准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()

    def check_high_score(self):
        '''检查是否诞生了新的最高得分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_score(self):
        '''将得分转换为一副渲染的图像'''

        score_str = "SCORE" + "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        #在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分转换为渲染的图像'''

        high_score_str = "HIGHEST" + "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.settings.bg_color)

        #将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)