"""

多重继承
	- 菱形继承(钻石继承)
	- C3算法(替代DFS的算法)
	- Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :

MRO是一个有序列表L，在类被创建时就计算出来。
公式：
mro(Child(Base1，Base2)) = [ Child ] + merge( mro(Base1), mro(Base2),  [ Base1, Base2] )
（其中Child继承自Base1, Base2）
规律总结：
从 “当前子类” 向上查找它的父类，
若 “当前子类” 不是 “查找的父类” 的最后一个继承的子类时，
则跳过该 “查找的父类” 的查找，开始查找 “当前子类” 的下一个父类

Version: 0.1
Author: 骆昊
Date: 2018-03-12

"""


class A(object):

	def foo(self):
		print('foo of A')


class B(A):
	pass


class C(A):

	def foo(self):
		print('foo fo C')


class D(B, C):
	pass


class E(D):

	def foo(self):
		print('foo in E')
		print('super().foo:')
		super().foo()
		print('super(B,self).foo():')
		super(B, self).foo()
		print('super(C,self).foo():')
		super(C, self).foo()


if __name__ == '__main__':
	d = D()
	d.foo()
	e = E()
	e.foo()	#最后1个输出不明白。。

"""
结果：
foo fo C
foo in E
foo fo C
foo fo C
foo of A	
"""
