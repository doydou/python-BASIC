import pygame
from pygame.sprite import Sprite

#创建Alien类
class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置其起始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外形人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的精确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置上绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x