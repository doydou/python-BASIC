import sys#使用sys模块来退出游戏
import pygame
import settings


def run_game():
    pygame.init()#初始化背景设置
    screen = pygame.display.set_mode((1200,800)) #设置屏幕大小
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标时间
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(bg_color)
        #让屏幕可见
        pygame.display.flip()

run_game()