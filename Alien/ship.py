import pygame

class Ship():

    def __init__(self,screen):
        '''初始化飞船及其位置'''
        self.screen = screen

        #加载飞船图像并获取其外形
        self.image = pygame.image.load('images/ship.bmp')#返回一个表示飞船的surface
        self.rect = self.image.get_rect()#获取相应的surface的属性
        self.screen_rect = screen.get_rect()#将表示屏幕的矩形存储在self.screen_rect

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #在指定位置上绘制飞创
        self.screen.blit(self.image,self.rect)