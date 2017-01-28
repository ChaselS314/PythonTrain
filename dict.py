from collections import OrderedDict

my_dict = {
	'compliation' : '汇编',
	'compile' : '编译',
	'link' : '链接',
	'build' : '构建',
	'debug' : '调试',
	'release' : '释放。。',
}

my_ordered_dict = OrderedDict()

my_ordered_dict['compliation'] = 'huibian'
my_ordered_dict['compile'] = 'bianyi'
my_ordered_dict['link'] = 'lianjie'
my_ordered_dict['build'] = 'goujian'
my_ordered_dict['debug'] = 'tiaoshi'
my_ordered_dict['release'] = 'shifang'

for name, explanation in my_dict.items():
	print(name.title() + ' : ' + explanation)

for name, explanation in my_ordered_dict.items():
	print(name.title() + ' : ' + explanation)