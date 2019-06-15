# -*- coding:utf-8 -*-
from collections.abc import Coroutine
import asyncio


# async def hello(name):
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     # 生成协程对象, 并不会运行函数内的代码
#     coroutine = hello("world")
#
#     # 检查是否是协程coroutine类型
#     print(isinstance(coroutine, Coroutine))
###################################################################################################################
# import asyncio
# from collections.abc import Generator,Coroutine
#
# '''只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。实际上，它的本质还是一个生成器。标记后，它实际上已经可以当成协程使用。后面会介绍。'''
# @asyncio.coroutine
# def hello():
#     yield from asyncio.sleep(1)
#
# if __name__ == '__main__':
#     coroutine = hello()
#     print(isinstance(coroutine, Coroutine))  # False
#     print(isinstance(coroutine, Generator))  # True
###################################################################################################################
# import asyncio
#
#
# async def hello(name):
#     await asyncio.sleep(2)
#     print('Hello,', name)
#
#
# async def hello1(name):
#     await asyncio.sleep(2)
#     print('Hello,', name)
#
#
# # 定义协程对象
# coroutine = hello("World")
# coroutine1 = hello1("World1")
#
# # 定义事件循环对象容器
# loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(coroutine)
#
# # 将协程转为task任务
# task = loop.create_task(asyncio.wait([coroutine, coroutine1]))
#
# # 将task任务扔进事件循环对象中并触发
# loop.run_until_complete(task)

# yield from 后面可接 可迭代对象，也可接future对象/协程对象；
# await 后面必须要接 future对象/协程对象

###################################################################################################################
# import asyncio
# import time
# async def _sleep(x):
#     time.sleep(2)
#     return '暂停了{}秒！'.format(x)
#
# coroutine = _sleep(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
# #  task.result() 可以取得返回结果
# print('返回结果：{}'.format(task.result()))
##############################################协程嵌套#####################################################################
# 用于内部的协程函数
# async def do_some_work(x):
#     print("waitting:", x)
#     await asyncio.sleep(x)
#     return "done after {}s".format(x)
#
#
# # 外部的协程函数
# async def main():
#     # 创建3个协程对象
#     cor1 = do_some_work(1)
#     cor2 = do_some_work(2)
#     cor3 = do_some_work(4)
#
#     # 将协程转换成task, 并组成list
#     tasks = [
#         asyncio.ensure_future(cor1),
#         asyncio.ensure_future(cor2),
#         asyncio.ensure_future(cor3),
#     ]
#
#     # await 一个task列表(协程)
#     # dones: 表示已经完成的任务
#     # pendings: 表示未完成的任务
#     # dones, pendings = await asyncio.wait(tasks)
#     # for task in dones:
#     #     print('Task ret', task.result())
#
#     # 使用gather 返回结果和await不一样
#     results = await asyncio.gather(*tasks)
#     for result in results:
#         print('Task ret', result)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
##############################################动态添加协程#####################################################################
# # 1.主线程是同步的
# import time
# import asyncio
# from queue import Queue
# from threading import Thread
#
# def start_loop(loop):
#     # 一个在后台永远运行的事件循环
#     asyncio.set_event_loop(loop)
#     loop.run_forever()
#
# def do_sleep(x, queue, msg=""):
#     time.sleep(x)
#     queue.put(msg)
#
# queue = Queue()
#
# new_loop = asyncio.new_event_loop()
#
# # 定义一个线程,并传入一个时间循环对象
# t = Thread(target=start_loop, args=(new_loop, ))
# t.start()
# print(time.ctime())
# # 动态添加两个协程, 这种方法, 在主线程是同步的
# new_loop.call_soon_threadsafe(do_sleep, 6, queue, "第一个")
# new_loop.call_soon_threadsafe(do_sleep, 3, queue, "第二个")
#
# while True:
#     msg = queue.get()
#     print("{} 协程运行完..".format(msg))
#     print(time.ctime())

# 2.主线程是异步的
import time
import asyncio
from queue import Queue
from threading import Thread

def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_sleep(x, queue, msg=""):
    await asyncio.sleep(x)
    queue.put(msg)

queue = Queue()

new_loop = asyncio.new_event_loop()

# 定义一个线程,并传入一个时间循环对象
t = Thread(target=start_loop, args=(new_loop, ))
t.start()
print(time.ctime())
# 动态添加两个协程, 这种方法, 在主线程是异步的
asyncio.run_coroutine_threadsafe(do_sleep(6, queue, "第一个"), new_loop)
asyncio.run_coroutine_threadsafe(do_sleep(3, queue, "第二个"), new_loop)

while True:
    msg = queue.get()
    print("{} 协程运行完..".format(msg))
    print(time.ctime())