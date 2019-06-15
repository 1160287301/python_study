# -*- coding:utf-8 -*-


import asyncio

async def hello():
    print("hello world 1")
    r = await asyncio.sleep(1)
    print("hello world 2")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(), hello()]))
loop.close()