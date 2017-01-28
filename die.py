from random import randint

class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))

six_dies = Die()

count_number = 0
while count_number < 10:
	count_number += 1
	six_dies.roll_die()


ten_dies = Die(10)

count_number = 0
while count_number < 10:
	count_number += 1
	ten_dies.roll_die()


twenty_dies = Die(20)

count_number = 0
while count_number < 10:
	count_number += 1
	twenty_dies.roll_die()