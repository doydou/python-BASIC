import sys#使用sys模块来退出游戏
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()#初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #设置屏幕大小
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞创
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让屏幕可见
        pygame.display.flip()

run_game()