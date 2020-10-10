"""
管理事件的代码简化run_game()并隔离事件管理循环。
通过隔离事件循环，可将事件管理与游戏的其他方面（如 更新屏幕）分离。
"""
import sys
import pygame
import ship
from bullet import Bullet

# def check_events(ship):
#     '''响应按键和鼠标时间'''
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#            sys.exit()
#         elif event.type == pygame.KEYDOWN:#每次按键都会被注册为一个ketdown时间
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#             #松开按键为keyup
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False
#                 向右移动飞船
#                 ship.rect.centerx +=1

'''重构check_events（）'''

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    # 创建一颗子弹，并将其加入到编组bullrts中


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    # 响应放开按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # 响应鼠标按键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    '''跟新子弹的位置，并删除已消失的子弹'''
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))测试log
