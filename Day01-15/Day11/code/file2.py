"""

读取圆周率文件判断其中是否包含自己的生日
strip函数用法：
函数原型
声明：s为字符串，rm为要删除的字符序列
s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
注意：
1. 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')

Version: 0.1
Author: 骆昊
Date: 2018-03-13

"""

birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
	lines = f.readlines()	# readlines返回的是列表
	pi_string = ''
	for line in lines:
		pi_string += line.strip()
	if birth in pi_string:
		print('Bingo!!!')
