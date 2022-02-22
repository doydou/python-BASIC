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

    def __init__(self, ai_settings, screen, ship):
        '''在飞船上创建子弹'''
        super().__init__()
        self.screen = screen

        #在屏幕上创建一个（0.0）点处表示子弹的矩形，再设置成正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示子弹位置
        self.y = float(self.rect.y)#子弹的y值会一直发生变化，而x值不变

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''使子弹向上移动'''
        #更新子弹位置的小数值
        self.y -= self.speed_factor
        #更新子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
