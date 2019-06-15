# -*- coding:utf-8 -*-
import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery
import traceback

start_url = 'http://www.jobbole.com/'
waitting_urls = []  # 待爬取url
seen_urls = set()  # 已爬取url
stopping = False  # 是否抓取完成
sem = asyncio.Semaphore(3)  # 同时并发数


async def fetch(url, session):
    async with sem:
        try:
            async with session.get(url) as resp:
                print("url start: {}".format(resp.status))
                if resp.status in [200, 201]:
                    return await resp.text()
        except Exception as e:
            print(traceback.print_exc())


def extract_html(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startwith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def init_urls(url, session):
    # 初始要爬取的url
    html = await fetch(url, session)
    extract_html(html)


async def article_handler(url, session, pool):
    # 获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_html(html)
    pq = PyQuery(html)
    title = pq('title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into article_test(title) value('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:  # 如果用queen就不用判断
                await asyncio.sleep(0.5)
                continue

            url = waitting_urls.pop()
            print("start get url: {}".format(url))
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    # 等待mysql链接建立好
    pool = await aiomysql.create_pool(
        host='localhost', port=3306,
        user='root', password='',
        db='mysql', loop=loop,
        charset='utf8', autocommit=True  # 这两个参数是坑
    )
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_html(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
