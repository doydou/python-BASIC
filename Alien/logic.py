import sys#使用sys模块来退出游戏
import pygame
from settings import Settings
from ship import Ship
import functions as func
from pygame.sprite import Group
from button import Button
from game_stats import GameStats


def run_game():
    pygame.init() #初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #设置屏幕大小
    pygame.display.set_caption("Alien Invasion")

    #创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    func.create_fleet(ai_settings, screen, aliens, ship)

    #开始游戏的主循环
    while True:

        func.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        #bullets.update()


        func.update_bullet(ai_settings,screen,ship, bullets, aliens)
        func.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # #删除以消失子弹(优化主循环，将此放入function中)
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            # print(len(bullets))

        #每次循环时都重绘屏幕
        func.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()