"""
'_'与'__'开头的属性均可被访问，前者可直接访问，后者方法方法见如下代码。
"""

class Test:

	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')


def main():
	test = Test('hello')
	test._Test__bar()
	print(test._Test__foo)	#对以"__"开头属性的访问方法


if __name__ == "__main__":
	main()
