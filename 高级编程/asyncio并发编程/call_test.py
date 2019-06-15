# -*- coding:utf-8 -*-
import asyncio


def callback(sleep_times):
    print("sleep {} success".format(sleep_times))

def callback2(sleep_times, loop):
    print(loop.time())

def stoploop(loop):
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 在队列里等待下一个循环的时候,立即执行
    # loop.call_soon(callback, 2)  # 函数, 参数
    # loop.call_soon(stoploop, loop)
    # call_soon_threadsafe 与call_soon用法一样,线程安全

    # call_soon

    # 在队列等待之后,执行
    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)

    # call_soon比call_later快
    # loop.call_soon(callback, 5)


    # call_at 在内部时间的基础上,执行
    now = loop.time()
    loop.call_at(now+2, callback2, 2, loop)
    loop.call_at(now+3, callback2, 3, loop)
    loop.call_at(now+1, callback2, 1, loop)
    loop.call_at(now+4, stoploop, loop)

    loop.run_forever()

