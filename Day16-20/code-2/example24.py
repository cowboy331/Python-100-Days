"""
aiohttp - 异步HTTP网络访问
异步I/O（异步编程）- 只使用一个线程（单线程）来处理用户请求
用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
Redis/Node.js - 单线程 + 异步I/O
Celery - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - uvloop

不要为每次的连接都创建一次session,一般情况下只需要创建一个session，然后使用这个session执行所有的请求。
每个session对象，内部包含了一个连接池，并且将会保持连接和连接复用（默认开启）可以加快整体的性能。

既然已经有了requests了，那为什么还要说aiohttp了？重点来了，aiohttp是异步的。
在python3.5中，加入了asyncio/await关键字，使得回调的写法更加直观和人性化。
而aiohttp是一个提供异步web服务的库，asyncio可以实现单线程并发IO操作。

requests写爬虫是同步的，是等待网页下载好才会执行下面的解析、入库操作，如果在下载网页时间太长会导致阻塞，使用multiprocessing或者threading加速爬虫也是一种方法。

貌似 C# 最早使用 async/await 模式？
异步编程模型以前基于事件、回调函数、协程什么的各种复杂麻烦，现在很多编程语言都引入了 async/await 模式简化异步编程（函数声明时 +async 前缀，调用函数时 +await 前缀），
现在的异步编程只要和同步编程一样了，甚至不需要知道原理和前面几章的内容，你只要知道哪些操作（函数）是异步的即可，
现在编程普遍都是异步的，而 await 又要配合 async 签名，所以一旦某个函数内出现 await，包容函数就要 async，而调用者也要 await 该函数，结果是调用者自身也要 async。

python3.4: 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
把@asyncio.coroutine替换为async；
把yield from替换为await。

"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp: #使用了aiohttp.ClientSession.get方法
        return await resp.text()    # await要跟coroutine类型的generator



async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
