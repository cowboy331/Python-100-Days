"""
在学习asyncio之前，我们先来理清楚同步/异步的概念：
·同步是指完成事务的逻辑，先执行第一个事务，如果阻塞了，会一直等待，直到这个事务完成，再执行第二个事务，顺序执行。。。
·异步是和同步相对的，异步是指在处理调用这个事务的之后，不会等待这个事务的处理结果，直接处理第二个事务去了，通过状态、通知、回调来通知调用者处理结果。

协程（coroutine）- 可以在需要时进行切换的相互协作的子程序
Coroutine是编译器级的，Process和Thread是操作系统级的。
Coroutine的实现，通常是对某个语言做相应的提议，然后通过后成编译器标准，然后编译器厂商来实现该机制。
Process和Thread看起来也在语言层次，但是内生原理却是操作系统先有这个东西，然后通过一定的API暴露给用户使用，两者在这里有不同。
Process和Thread是os通过调度算法，保存当前的上下文，然后从上次暂停的地方再次开始计算，重新开始的地方不可预期，
每次CPU计算的指令数量和代码跑过的CPU时间是相关的，跑到os分配的cpu时间到达后就会被os强制挂起。
Coroutine是编译器的魔术，通过插入相关的代码使得代码段能够实现分段式的执行，重新开始的地方是yield关键字指定的，一次一定会跑到一个yield对应的地方。

关于asyncio的一些关键字的说明：

event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数
coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象.
task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果

python3.4: 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
把@asyncio.coroutine替换为async；
把yield from替换为await。

"""
import asyncio

from example15 import is_prime


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)  # yield from语法可以让我们方便地调用另一个generator


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """主函数"""
    loop = asyncio.get_event_loop() # 创建一个事件loop
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future) #将封装协程的任务注册到事件循环，并启动事件循环
    loop.close()


if __name__ == '__main__':
	main()


# import asyncio
#
# @asyncio.coroutine    # 把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)   # yield from语法可以让我们方便地调用另一个generator
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()



# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 可见3个连接由一个线程通过coroutine并发完成。