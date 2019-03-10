"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
Python提供的Condition对象提供了对复杂线程同步问题的支持。

Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。
线程首先acquire一个条件变量，然后判断一些条件。
如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。
不断的重复这一过程，从而解决复杂的同步问题。
除了acquire方法、 release方法、notify方法、wait方法外还有notifyAll方法。

"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()


# 生产者消费者问题
# import threading
# import time
# class Producer(threading.Thread):
#     def run(self):
#         global count
#         while True:
#             if con.acquire():
#                 if count > 1000:
#                     con.wait()
#                 else:
#                     count = count+100
#                     msg = self.name+' produce 100, count=' + str(count)
#                     print msg
#                     con.notify()
#                 con.release()
#                 time.sleep(1)
# class Consumer(threading.Thread):
#     def run(self):
#         global count
#         while True:
#             if con.acquire():
#                 if count < 100:
#                     con.wait()
#                 else:
#                     count = count-3
#                     msg = self.name+' consume 3, count='+str(count)
#                     print msg
#                     con.notify()
#                 con.release()
#                 time.sleep(1)
# count = 500
# con = threading.Condition()
# def test():
#     for i in range(2):
#         p = Producer()
#         p.start()
#     for i in range(5):
#         c = Consumer()
#         c.start()
# if __name__ == '__main__':
#     test()




