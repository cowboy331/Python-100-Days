"""

Python常用模块
	- 运行时服务相关模块: copy / pickle / sys / ...
	- 数学相关模块: decimal / math / random / ...
	- 字符串处理模块: codecs / re / ...
	- 文件处理相关模块: shutil / gzip / ...
	- 操作系统服务相关模块: datetime / os / time / logging / io / ...
	- 进程和线程相关模块: multiprocessing / threading / queue
	- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
	- Web编程相关模块: cgi / webbrowser
	- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: 骆昊
Date: 2018-03-05

"""

import time
import shutil
import os

############ the formated code by me####################################
seconds = time.time()
print("seconds: %.4f"%seconds)
localtime = time.localtime(seconds)
print('localtime: {0}'.format(localtime))
print('localtime.tm_year: %d' %localtime.tm_year)
print('localtime.tm_mon: %i'%localtime.tm_mon)
print('localtime.tm_mday: %a'%localtime.tm_mday)
asctime = time.asctime(localtime)
print('asctime: {}'.format(asctime))
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print('strtime: {}'.format(strtime))
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print('mydate: {}'.format(mydate))

shutil.copy('c:/Users/kk/hello.py', 'c:/Users/kk/Desktop/first.py')
os.system('ls -l')
os.chdir('c:/Users/kk')
os.system('ls -l')
os.mkdir('test')

######## the original code by the author###############
# seconds = time.time()
# print(seconds)
# localtime = time.localtime(seconds)
# print(localtime)
# print(localtime.tm_year)
# print(localtime.tm_mon)
# print(localtime.tm_mday)
# asctime = time.asctime(localtime)
# print(asctime)
# strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
# print(strtime)
# mydate = time.strptime('2018-1-1', '%Y-%m-%d')
# print(mydate)
#
# shutil.copy('c:/Users/kk/hello.py', 'c:/Users/kk/Desktop/first.py')
# os.system('ls -l')
# os.chdir('c:/Users/kk')
# os.system('ls -l')
# os.mkdir('test')
