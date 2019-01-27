"""

打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01

"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):  #以_开头的变量名
        print('*', end='')  #去掉结尾的\n
    print()     #print()默认以'\n'结尾

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
