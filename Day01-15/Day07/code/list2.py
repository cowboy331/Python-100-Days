"""

列表常用操作
	- 列表连接
	- 获取长度
	- 遍历列表
	- 列表切片
	- 列表排序
	- 列表反转
	- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06

"""


def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
	# 循环遍历列表元素
	for fruit in fruits:
		print(fruit.title(), end=' ')	#Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
	print()
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2)
	# fruit3 = fruits  # 没有复制列表只创建了新的引用
	fruits3 = fruits[:]		# 可以通过完整切片操作来复制列表
	print(fruits3)
	fruits4 = fruits[-3:-1]
	print(fruits4)
	fruits5 = fruits[::-1]
	print(fruits5)


if __name__ == '__main__':
	main()
