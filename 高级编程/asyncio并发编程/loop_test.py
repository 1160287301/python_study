# -*- coding:utf-8 -*-
# 事件循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado, gevent, twisted(scrapy, django的channels)
# tornado(实现web服务器), Django+flask(uwsgi, gunicorn+nginx)
# tornado可以直接部署, nginx+tornado


# 使用asyncio
import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get url:{}".format(url))
    # time.sleep(2)
    await asyncio.sleep(2)
    # time.sleep(2)
    return "bobby"


def callback(url, future):
    # 需要的参数必须放在前面
    print("send email bobby from {}".format(url))


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("http://www.imooc.com"))
    # 提交列表到事件循环
    # loop.run_until_complete(asyncio.wait([get_html("http://www.imooc.com") for i in range(10)]))
    # loop.run_until_complete(asyncio.gether(*[get_html("http://www.imooc.com") for i in range(10)]))

    # 获取返回值1
    # get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # task是future的子类 future与线程的future类似 task主要解决了两个问题
    # 1.协程初始化需要send(None)
    # 2.协程抛出StopIteration异常  值在异常的value中

    # 获取返回值2
    # task = loop.create_task(get_html("http://www.imooc.com"))
    # 添加callback函数
    # task.add_done_callback(callback)
    # 如果callback函数需要参数,使用偏函数
    # task.add_done_callback(partial(callback, "http://www.imooc.com"))
    # loop.run_until_complete(task)
    # print(task.result())

    # asyncio.wait中的wait gether
    # wait中的wait类比于线程池找那个的wait
    # gather可以完成wait的功能,比wait更高级,可以分组(两组协程可以交替运行,而不是一批运行完在运行下一批)
    group1 = [get_html("http://baidu.com") for i in range(2)]
    group2 = [get_html("http://imooc.com") for i in range(4)]
    # gro1 = asyncio.gather(*group1)
    # gro2 = asyncio.gather(*group2)
    # 可以分批取消
    # gro2.cancel()
    # loop.run_until_complete(asyncio.gather(*group1, *group2))
    loop.run_until_complete(asyncio.wait(group1))
    loop.run_until_complete(asyncio.wait(group2))
    # loop.run_until_complete(asyncio.gather(gro1, gro2))

    print(time.time() - start_time)
