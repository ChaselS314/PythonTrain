# # filename = 'learning_python.txt'

# # with open(filename) as file_object:
# # 	# contents = file_object.read()
# # 	# print(contents)
# # 	# for line in file_object:
# # 		# print(line.rstrip())
# # 	lines = file_object.readlines()

# # for line in lines:
# # 	new_line = line.replace('Python', 'C')
# # 	print(new_line.rstrip())

# filename = 'guest.txt'

# guest_name = input("Input you name, I'll remeber you forever.")

# with open(filename, 'w') as file_object:
# 	file_object.write(guest_name + '\n')

filename = 'guest_book.txt'

while True:
	guest_name = input('Input you name to login or type "quit" to quit.\n')
	if guest_name == 'quit':
		break
	print('Nice to meet you, ' + guest_name + ' !')
	with open(filename, 'a') as file_object:
		file_object.write(guest_name + ' login once.\n')
