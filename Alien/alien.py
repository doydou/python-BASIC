import pygame
from pygame.sprite import Sprite

#创建Alien类
class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置其起始位置'''
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

    #加载外形人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.tmp')
        self.rect = self.image.get_rect()

    #每个外星人最初都在