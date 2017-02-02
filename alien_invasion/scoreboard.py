import pygame.font

class Scoreboard():
	"""显示得分信息的类"""

	def __init__(self, ai_settings, screen, stats):
		"""初始化相关属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# 字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# 准备初始化得分图像
		self.prep_score()
		self.prep_max_score()


	def prep_max_score(self):
		"""将最高分转换为图像，并设置合适坐标"""
		# 将得分渲染成图像
		rounded_score = int(round(self.stats.max_score, -1))
		score_str = "{:,}".format(rounded_score)
		self.max_score_image = self.font.render(score_str, True, self.text_color,
			self.ai_settings.bg_color)

		# 将图像位置设置在屏幕右上角
		self.max_score_rect = self.max_score_image.get_rect()
		self.max_score_rect.centerx = self.screen_rect.centerx
		self.max_score_rect.top = self.screen_rect.top + 20

	def prep_score(self):
		"""将得分转换为图像，并设置合适坐标"""
		# 将得分渲染成图像
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.ai_settings.bg_color)

		# 将图像位置设置在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = self.screen_rect.top + 20

	def draw_score(self):
		"""在屏幕上显示得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.max_score_image, self.max_score_rect)