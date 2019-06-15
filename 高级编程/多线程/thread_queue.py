# -*- coding:utf-8 -*-

import time
import threading


def get_list_url(url):
    while True:
      # print(url.pop())
        print(url.get())


def get_detail_url(url):
    for i in range(20):
        url.put('http:www.{}.com'.format(i))
        # url.append('http:www.{}.com'.format(i))


class getlist(threading.Thread):
    def __init__(self, name):
        super.__init__(name=name)

    def run(self):
        print('start list url')
        time.sleep(2)
        print('end list url')


class getdetail(threading.Thread):
    def __init__(self, name):
        super.__init__(name=name)

    def run(self):
        print('start detail url')
        time.sleep(2)
        print('end detail url')


if __name__ == '__main__':
    import queue  # 本身就是线程安全的
    url = queue.Queue(maxsize=1000)
    get_detail_url(url)
    for i in range(3):
        a = threading.Thread(target=get_list_url, args=(url,))
        a.start()

    # url.join()  # 和线程的url类似
    # url.task_done()  # 队列完成