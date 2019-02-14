"""

异常机制 - 处理程序在运行时可能发生的状态

Python中的strip用于去除字符串的首尾字符，同理，lstrip用于去除左边的字符，rstrip用于去除右边的字符。
这三个函数都可传入一个参数，指定要去除的首尾字符。
注意：如果不传参数，那么是指去掉左右两边的空白字符，不仅仅是空格，还包括换行符(\n)，水平制表(\t)等。

Version: 0.1
Author: 骆昊
Date: 2018-03-13

"""

import time
import sys

filename = input('请输入文件名: ')
try:
	with open(filename) as f:
		lines = f.readlines()
except FileNotFoundError as msg:
	print('无法打开文件:', filename)
	print(msg)
except UnicodeDecodeError as msg:
	print('非文本文件无法解码')
	sys.exit()
else:
	for line in lines:
		print(line.rstrip())
		time.sleep(0.5)
finally:
	# 此处最适合做善后工作
	print('不管发生什么我都会执行')
