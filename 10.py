filename = 'learning_python.txt'

with open(filename) as file_object:
	# contents = file_object.read()
	# print(contents)
	# for line in file_object:
		# print(line.rstrip())
	lines = file_object.readlines()

for line in lines:
	new_line = line.replace('Python', 'C')
	print(new_line.rstrip())

