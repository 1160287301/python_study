# -*- coding:utf-8 -*-
# 对于io操作来说, 多进程和多线程性能差别不大

# 1.通过thread类实例化
import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


class GetDetailhtml(threading.Thread):
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")


if __name__ == '__main__':
    start_time = time.time()
    # thread1 = threading.Thread(target=get_detail_html, args=("", ))
    # thread2 = threading.Thread(target=get_detail_url, args=("", ))
    thread1 = GetDetailhtml()
    thread2 = GetDetailUrl()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # thread1.setDaemon(True)
    # thread2 .setDaemon(True)
    print(time.time() - start_time)
