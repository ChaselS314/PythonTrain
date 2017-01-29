import pygame
import sys

class Role():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('role.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((720, 480))
bg_color = (0, 0, 255)
screen.fill(bg_color)
role = Role(screen)

while True:
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	role.blitme()
	pygame.display.flip()

