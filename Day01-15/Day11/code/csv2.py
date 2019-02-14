"""
写入CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13

对newline参数的解释：
参数newline是用来控制文本模式之下，一行的结束字符。可以是None，’’，\n，\r，\r\n等。

当在读取模式下，如果新行符为None，那么就作为通用换行符模式工作，意思就是说当遇到\n，\r或\r\n都可以作为换行标识，并且统一转换为\n作为文本输入的换行符。当设置为空’’时，也是通用换行符模式工作，但不作转换为\n，输入什么样的，就保持原样全输入。当设置为其它相应字符时，就会判断到相应的字符作为换行符，并保持原样输入到文本。
"""

import csv


class Teacher(object):

	def __init__(self, name, age, title):
		self.__name = name
		self.__age = age
		self.__title = title
		self.__index = -1

	@property
	def name(self):
		return self.__name

	@property
	def age(self):
		return self.__age

	@property
	def title(self):
		return self.__title


filename = 'teacher.csv'
teachers = [Teacher('骆昊', 38, '叫兽'), Teacher('狄仁杰', 25, '砖家')]

try:
	# 如果不加newline='',每一行数据后都会自动增加一个空行
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)
		for teacher in teachers:
			writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
	print('无法写入文件:', filename)
else:
	print('保存数据完成!')
