# -*- coding:utf-8 -*-

import dis
import threading
from threading import Lock
from threading import RLock  # 可重入得到锁
# 在同一个线程里面,可以连续调用多次acquire,一定要注意acquire的次数要和release次数相同

total = 0
# rlock = Lock()
rlock = RLock()
# 用锁会影响性能
# 锁会影响死锁


def add1(lock):
    global total
    for i in range(100000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc1(lock):
    global total
    for i in range(100000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = threading.Thread(target=add1, args=(rlock, ))
thread2 = threading.Thread(target=desc1, args=(rlock, ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)