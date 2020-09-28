import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        '''初始化飞船及其位置'''
        self.screen = screen
        self.ai_settings = ai_settings  #形参列表中添加了形参

        #加载飞船图像并获取其外形
        self.image = pygame.image.load('images/ship.bmp') #返回一个表示飞船的surface
        self.rect = self.image.get_rect() #获取相应的surface的属性
        self.screen_rect = screen.get_rect() #将表示屏幕的矩形存储在self.screen_rect

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小属值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        #更新飞船的center值，而不是rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center跟新rect对象
        self.rect.centerx = self.center
    def blitme(self):
        #在指定位置上绘制飞创
        self.screen.blit(self.image,self.rect)

