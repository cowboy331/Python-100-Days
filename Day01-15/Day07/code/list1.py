"""

定义和使用列表
	- 用下标访问元素
	- 添加元素
	- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06

"""


def main():
	fruits = ['grape', '@pple', 'strawberry', 'waxberry']
	print(fruits)
	# 通过下标访问元素
	print(fruits[0])
	print(fruits[1])
	print(fruits[-1])
	print(fruits[-2])
	# print(fruits[-5]) # IndexError
	# print(fruits[4])	# IndexError
	fruits[1] = 'apple'
	print(fruits)
	# 添加元素
	fruits.append('pitaya')		#在列表末尾添加新的对象
	fruits.insert(0, 'banana')		#将对象插入列表
	print(fruits)
	# 删除元素
	del fruits[1]
	fruits.pop()		#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
	fruits.pop(0)
	fruits.remove('apple')		#remove() 函数用于移除列表中某个值的第一个匹配项，没有返回值。

	print(fruits)


if __name__ == '__main__':
	main()
