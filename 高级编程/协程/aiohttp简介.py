# -*- coding:utf-8 -*-
import asyncio
import functools
import os
import time

import requests
from aiohttp import ClientSession

# tasks = []
# url = "https://www.baidu.com/{}"
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response.request.headers)
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(hello(url))

class MyRequest(object):
    def __init__(self):
        self.list = []
        self.make_list()

    def make_list(self):
        for i in range(1000):
            self.list.append('https://www.baidu.com/')


async def crawler(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    # 利用BaseEventLoop.run_in_executor()可以在coroutine中执行第三方的命令，例如requests.get()
    # 第三方命令的参数与关键字利用functools.partial传入
    response = await asyncio.get_event_loop().run_in_executor(None, functools.partial(requests.get, url, headers=headers))
    print(response.status_code)


if __name__ == '__main__':
    start_time = time.time()
    # 预先设定需要抓取的URL列表
    req = MyRequest()
    # 创建并执行协程任务
    loop = asyncio.get_event_loop()
    tasks = [crawler(url) for url in req.list]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    # 同步访问
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    # for i in req.list:
    #     print(requests.get(url=i, headers=headers).status_code)
    print('time: ', time.time() - start_time)
