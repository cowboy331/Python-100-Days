"""
使用装饰器实现单例模式
装饰类的装饰器 - 单例模式 - 一个类只能创建出唯一的对象
上下文语法：
__enter__ / __exit__

当多线程中需要“独占资源”的时候，要使用锁来控制，防止多个线程同时占用资源而出现其他异常
#创建锁
mutex = threading.Lock()
#锁定
mutex.acquire([timeout])
#释放
mutex.release()
"""
import threading

from functools import wraps


def singleton(cls):
    """单例装饰器"""
    instances = {}
    # 创建锁
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:  # with Lock的作用相当于自动获取和释放锁(资源)，锁定期间，其他线程不可以干活
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    print(President.__name__)
    p1 = President('特朗普', '美国')
    p2 = President('奥巴马', '美国')
    print(p1 == p2)
    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
