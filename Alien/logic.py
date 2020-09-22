import sys#使用sys模块来退出游戏
import pygame
from settings import Settings
from ship import Ship
import functins as func

def run_game():
    pygame.init()#初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #设置屏幕大小
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞创
    ship = Ship(ship_index,screen)

    #开始游戏的主循环
    while True:

        func.check_events(ship)
        ship.update()
        #每次循环时都重绘屏幕
        func.update_screen(ai_settings,screen,ship)

run_game()