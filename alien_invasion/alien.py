import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示一个外星人的类"""

	def __init__(self, screen, ai_settings, ):
		"""初始化外星人并设置起始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，并设置其rect值
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 每个外星人最初都在屏幕左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)

		# 表示外星人的移动方向，-表示左，+表示右
		self.move_direction = 1


	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)
