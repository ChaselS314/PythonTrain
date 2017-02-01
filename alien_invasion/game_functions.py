import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
	# 创建一颗子弹并加入编组bullets
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""响应按键松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环前都重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	# todo: draw aliens
	aliens.draw(screen)
	# 绘制每一颗子弹
	for bullet in bullets:
		bullet.draw_bullet()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings, screen, ship, bullets, aliens):
	"""更新子弹的位置，并删除消失的子弹"""
	bullets.update()
	check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)
	# 删除已消失的子弹
	# 但是为什么要用.copy()？
	for bullet in bullets.copy():
		if bullet.y <= 0:
			bullets.remove(bullet)
	# print(len(bullets))


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
	# 检测子弹与外星人的碰撞
	# 修改后面两个参数可以调整碰撞时是否消失
	pygame.sprite.groupcollide(aliens, bullets, True, True)
	# 当外星人全被消灭时，新建一个外星人群，并删除当前子弹
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)


def update_aliens(ai_settings, screen, stats, ship, bullets, aliens):
	"""更新外星人的位置"""
	for alien in aliens.sprites():
		# 当有外星人到达边界时，整个外星人群向下移动，并转向
		if alien.rect.right >= ai_settings.screen_width or alien.rect.left <= 0:
			for alien in aliens:
				alien.rect.y += ai_settings.alien_speed_factor_y
				alien.move_direction *= -1
			break
	
	for alien in aliens:
		alien.x += alien.move_direction*ai_settings.alien_speed_factor_x
		alien.rect.x = alien.x

	# 检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, ship, bullets, aliens)

	# 检测外星人是否到达屏幕底端
	for alien in aliens:
		if alien.rect.bottom >= ai_settings.screen_height:
			ship_hit(ai_settings, screen, stats, ship, bullets, aliens)
			break


def ship_hit(ai_settings, screen, stats, ship, bullets, aliens):
	"""响应外星人与飞船相撞"""
	if stats.ships_left > 0:
		# ship剩余数量减1
		stats.ships_left -= 1

		# 清空外星人和子弹
		aliens.empty()
		bullets.empty()

		# 创建一个新的外星人群，并将飞船放到屏幕底部中央
		create_fleet(ai_settings, screen, ship, aliens)
		ship.rect.centerx = ship.screen_rect.centerx

		# 暂停
		sleep(0.5)
	else:
		stats.game_active = False 


def get_number_rows(ai_settings, ship, alien_height):
	"""计算屏幕能容纳外星人的行数"""
	available_space_y = ai_settings.screen_height - alien_height*2 - ship.rect.height
	return available_space_y // (alien_height*2)


def get_number_aliens_x(ai_settings, alien_width):
	"""计算一行可以容纳的外星人数量"""
	available_space_x = ai_settings.screen_width - alien_width*2
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x


def create_alien(screen, ai_settings, aliens, alien_number, alien_row):
	"""创建一个外星人并将其加入当前行"""
	alien = Alien(screen, ai_settings)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien.x = alien_width + alien_width*2*alien_number
	alien.rect.x = alien.x
	# Alien没有y属性，为什么不报错？
	alien.y = alien_height + alien_height*2*alien_row
	alien.rect.y = alien.y
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens): 
	"""创建外星人群"""
	# 创建一个外星人，并计算一行可以容纳的外星人数量
	# 外星人间距为外星人宽度
	# 创建一个alien实例以获得外星人宽度
	alien = Alien(screen, ai_settings)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship, alien.rect.height)

	for alien_row in range(number_rows):
		# 创建一行aliens
		for alien_number in range(number_aliens_x):
			create_alien(screen, ai_settings, aliens, alien_number, alien_row)

