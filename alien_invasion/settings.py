class Settings():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self,):
		"""初始化游戏的静态设置"""
		# 屏幕设置
		self.screen_width = 960
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# 飞船设置 
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 8 # 允许同时存在的子弹最大数量


		# 速度加快的尺度
		self.speedup_scale = 1.1

		# 得分增加的速度
		self.scoreup_scale = 1.5

		# 初始化游戏的动态设置
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""初始化游戏的动态设置"""
		# 相关速度设置
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor_x = 1
		self.alien_speed_factor_y = 50
		
		# 击杀单个外星人的初始得分
		self.alien_score = 50


	def increase_speed(self):
		"""提高游戏速度"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor_x *= self.speedup_scale
		self.alien_speed_factor_y *= self.speedup_scale
		self.alien_score = int(self.alien_score * self.scoreup_scale)

