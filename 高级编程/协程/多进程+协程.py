# -*- coding:utf-8 -*-


import asyncio
import random
import re
import threading
import multiprocessing
import time
from multiprocessing import Queue, Pool, Process
import aiohttp
import execjs
from zs_factor import getip


import os
def get_proxy():
    env = os.environ
    topic = env.get("ZS_FACTOR_TOPIC", "fixed,dailiyun,wasp")
    group = env.get("ZS_FACTOR_GROUP", 'guazi')
    num = env.get("ZS_FACTOR_NUM", 50)
    return getip(topic, group=group, num=num)


async def crawl_(ip_):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        try:
            url = random.choice(['https://www.guazi.com/www/', 'https://www.guazi.com/www/buy/'])
            async with session.get(url=url, headers=headers, timeout=1, verify_ssl=False, proxy=ip_) as r:
                # content, text = await r.read(), await r.text(encoding='utf-8', errors='ignore')
                text = await r.text(encoding='utf-8', errors='ignore')
                js = re.findall(r'''(eval\(.*?'antipas';)''', text, re.S)[0]
                code = execjs.compile(
                    r'''%s
                    function get_cookies() {
                        return value;
                    }
                    ''' % (js))
                antipas = code.call('get_cookies')
                # session.headers['Cookie'] = 'antipas={}'.format(antipas)
                proxies_cookies = {
                    'proxies': ip_,
                    'cookies': {'antipas': antipas},
                }
                print(proxies_cookies)
        except:
            pass


def process_start(*ip_list):
    tasks = [asyncio.ensure_future(crawl_(ip_)) for ip_ in ip_list]
    loop = asyncio.get_event_loop()
    # for name in namelist:
    #     tasks.append(asyncio.ensure_future(crawl(name)))
    loop.run_until_complete(asyncio.wait(tasks))


def task_start(process_count=8):
    ip_set = set()
    for i in range(100):
        ip_set.add(get_proxy())
    ip_list = list(ip_set)
    count = len(ip_list) // process_count
    group_list = [ip_list[index: index+count] for index in range(0, len(ip_list), count)]
    if len(group_list) > process_count:
        extend = group_list.pop(-1)
        group_list[-1].extend(extend)
    for i in range(process_count):
        ip_list = group_list[i]
        p = Process(target=process_start, args=ip_list)
        p.start()
        p.join()


if __name__ == '__main__':
    start_time = time.time()
    task_start()
    print(time.time() - start_time)
