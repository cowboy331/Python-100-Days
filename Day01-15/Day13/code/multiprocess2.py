"""

实现进程间的通信
1、run：如果在创建Process对象的时候不指定target，那么就会默认执行Process的run方法：
2、join方法官方文档的意思是：阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。


Version: 0.1
Author: 骆昊
Date: 2018-03-20

"""

import multiprocessing
import os


def sub_task(queue):
	print('子进程进程号:', os.getpid())
	counter = 0
	while counter < 1000:
		queue.put('Pong')
		counter += 1
		# print(counter)


if __name__ == '__main__':
	print('当前进程号:', os.getpid())
	queue = multiprocessing.Queue()
	p = multiprocessing.Process(target=sub_task, args=(queue,))
	p.start()	#通过调用start方法启动进程，跟线程差不多
	counter = 0
	while counter < 1000:
		queue.put('Ping')
		counter += 1
	print(counter)
	p.join()
	print('子任务已经完成.')
	for _ in range(2000):
		print(queue.get(), end='')
