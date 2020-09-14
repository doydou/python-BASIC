"""
管理事件的代码简化run_game()并隔离事件管理循环。
通过隔离事件循环，可将事件管理与游戏的其他方面（如 更新屏幕）分离。
"""
import sys
import pygame
import ship


def check_events(ship):
    '''响应按键和鼠标时间'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        elif event.type == pygame.KEYDOWN:#每次按键都会被注册为一个ketdown时间
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                #向右移动飞船
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()