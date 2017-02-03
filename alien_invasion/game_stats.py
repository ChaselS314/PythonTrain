import os

class GameStats():
	"""管理游戏的运行状态的统计信息"""

	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# 游戏状态
		self.game_active = False
		# 游戏最高分
		self.filename = 'max_score'
		try:
			with open(self.filename, 'r') as file_object:
				self.max_score = int(file_object.read().strip())
		except FileNotFoundError:
			self.max_score = 0
		except ValueError:
			self.max_score = 0
			os.remove(self.filename)


	def update_max_score(self):
		"""更新最高得分"""
		if self.score > self.max_score:
			self.max_score = self.score
		# 将最高得分写入文件保存
		with open(self.filename, 'w') as file_object:
			file_object.write(str(self.max_score))


	def reset_stats(self):
		"""初始化游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		# 当前得分
		self.score = 0
		self.level = 1


