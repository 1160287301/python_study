# -*- coding:utf-8 -*-

# semaphore 是用于控制进入数量的值
# 比如 对于文件的读写, 写一般是一个线程写,读可以允许有多个

import threading
import time

class Htmlspider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class Urlproducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = Htmlspider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    h = Urlproducer(sem)
    h.start()
