"""
管理事件的代码简化run_game()并隔离事件管理循环。
通过隔离事件循环，可将事件管理与游戏的其他方面（如 更新屏幕）分离。
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
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

def check_keyup_events(event, ship):
    # 响应放开按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    # 响应鼠标按键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''单击play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #变为初始设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #变为初始状态
        stats.reset_stats()
        stats.game_active = True
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
        #创建新的外形人群和新的飞船
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def fire_bullet(ai_settings, screen, ship, bullets):
    '''没到达限制就发射一颗子弹'''
    #创建新的子弹并将其加入到bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(ai_settings, screen, ship, bullets, aliens):
    '''跟新子弹的位置，并删除已消失的子弹'''
    #刷新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))测试log
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    '''响应子弹合外星人的碰撞'''
    #删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人,加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


'''重构create fleet函数'''

def check_fleet_edges(ai_settings, aliens):
    '''如果外星人到达边缘应该采取的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break



def change_fleet_direction(ai_settings, aliens):
    '''将整体外星人下移'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 #向下移以后改变其值为负。即为修改方向


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        #将ship_left - 1
        stats.ships_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    #清空外形人和子弹列表
    aliens.empty()
    bullets.empty()

    #创建一群新的外形人，并将飞船放到屏幕底端中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    #暂停
    sleep(0.5)



def check_aliens_bottom(ai_settings, screen, stats , ship, aliens, bullets):
    '''检查是否有外形人到达屏幕的底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, ship, aliens, bullets):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    #检测外形人撞击屏幕底部
    check_aliens_bottom(ai_settings, screen, stats,ship, aliens, bullets)


def get_number_alien(ai_settings, alien_width):
    #求出每行外星人的数量
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien = int(available_space_x / (2 * alien_width))
    return number_alien


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height
                         - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens,alien_number, row_number):
    #创建外星人加入编组并加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien = get_number_alien(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien):
        # 创建一个外星人加入
        # alien = Alien(ai_settings, screen)
        # alien.x = alien_width +2 * alien_width * alien_number
        # alien.rect.x = alien.x
        # aliens.add(alien)
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
