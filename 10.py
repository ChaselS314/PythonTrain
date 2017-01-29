# # # # # filename = 'learning_python.txt'

# # # # # with open(filename) as file_object:
# # # # # 	# contents = file_object.read()
# # # # # 	# print(contents)
# # # # # 	# for line in file_object:
# # # # # 		# print(line.rstrip())
# # # # # 	lines = file_object.readlines()

# # # # # for line in lines:
# # # # # 	new_line = line.replace('Python', 'C')
# # # # # 	print(new_line.rstrip())

# # # # filename = 'guest.txt'

# # # # guest_name = input("Input you name, I'll remeber you forever.")

# # # # with open(filename, 'w') as file_object:
# # # # 	file_object.write(guest_name + '\n')

# # # filename = 'guest_book.txt'

# # # while True:
# # # 	guest_name = input('Input you name to login or type "quit" to quit.\n')
# # # 	if guest_name == 'quit':
# # # 		break
# # # 	print('Nice to meet you, ' + guest_name + ' !')
# # # 	with open(filename, 'a') as file_object:
# # # 		file_object.write(guest_name + ' login once.\n')
# # while True:
# # 	a = input('Input a number : ')
# # 	if a == 'quit':
# # 		break
# # 	b = input('Input a number : ')
# # 	if b == 'quit':
# # 		break
# # 	try:
# # 		res = int(a) + int(b)
# # 	except ValueError:
# # 		mes = a + ', ' + b + ' are not right type.\nPlease input two number.\n'
# # 		print(mes)
# # 	else:
# # 		print(res)

# def printPetsName(filename):
# 	try:
# 		with open(filename) as file_object:
# 			names = file_object.read().split()
# 			for name in names:
# 				print(name)
# 	except FileNotFoundError:
# 		# mes = filename + ' is not found.\nPlease check again.'
# 		# print(mes)
# 		pass

# first_filename = 'cats.txt'
# second_filename = 'dogs.txt'

# printPetsName(first_filename)
# printPetsName(second_filename)

filename = 'the American Journal of Archaeology.txt'

try:
	with open(filename, 'r', encoding = 'utf-8') as file_object:
		contents = file_object.read()
		cnt = contents.lower().count('the')
		print("The word 'the' has occupied for " + str(cnt) + " times in <" + filename + "> .")
except FileNotFoundError:
	mes = filename + ' is not found.\nPlease check again.'
	print(mes)
