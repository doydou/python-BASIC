import pygame
from pygame.sprite import Sprite
#sprite 类和 Group类
"""
srite模块有两个主要的类。第一种是Sprite，它应该作为所有游戏对象的基类。
这个类本身并不做任何事情，它只是包含了一些帮助管理游戏对象的功能。
另一种类型是Group。Group类是不同sprite对象的容器。
"""
class Bullet(Sprite):
    '''对子弹管理的类'''

    def __init__(self,ai_settings,screen,ship):
        '''在飞船上创建子弹'''
        super().__init__()
        self.screen = screen

    #在屏幕上创建一个（0.0）点处表示子弹的矩形，再设置成正确的位置
