# -*- coding:utf-8 -*-
import types
from collections import Awaitable
# async def downloader(url):
#     return "bobby"

@types.coroutine
def downloader(url):
    yield "bobby"


async def download_url(url):
    # dosomethings
    html = await downloader(url)
    return html


if __name__ == '__main__':
    core = download_url("htt[://baidu.com")
    # next(core)  # sys:1: RuntimeWarning: coroutine 'download_url' was never awaited
    core.send(None)

