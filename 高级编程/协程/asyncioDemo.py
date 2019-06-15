# -*- coding:utf-8 -*-
import time
import asyncio

# now = lambda: time.time()
# async def do_some_work(x):
#     print('Waiting: ', x)
# start = now()
# coroutine = do_some_work(2)
# # 创建一个事件循环
# loop = asyncio.get_event_loop()
# # 将协程注册到事件循环(其实是run_until_complete方法将协程包装成为了一个任务（task）对象)
# # asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task
# # task = asyncio.ensure_future(coroutine)
# task = loop.create_task(coroutine)
# print('1', task)
# loop.run_until_complete(task)
# print('2', task)
# print('TIME: ', now() - start)


### 绑定回调
import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

# def callback(future):
#     print('Callback: ', future.result())
def callback(t, future):
    print('Callback:', t, future.result())




start = now()
import functools
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
task.add_done_callback(functools.partial(callback, 2))
loop.run_until_complete(task)

print('TIME: ', now() - start)
