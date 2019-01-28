"""

函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-05

"""
"""
return的两个作用：
1、返回函数结果
2、结束函数的执行
"""

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor   #结束函数执行
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)

def test(x, y):
    if x > y:
        return 0    #结束函数的执行
    return 1


print(gcd(15, 27))
print(lcm(15, 27))
print(test(2, 1))
