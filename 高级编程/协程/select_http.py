# -*- coding:utf-8 -*-

import socket
from urllib.parse import urlparse
# import select # 一般不直接使用 因为有封装好的包DefaultSelector
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 使用select完成http请求
selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False
class Fetcher(object):
    def connect(self, key):
        selector.unregister(key.fd)  # 注销写事件
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 注册读事件
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:  # 已经读完,内核空间没有数据
            selector.unregister(key.fd)

            data = self.data.decode("utf8")
            html_data = data.split('\r\n\r\n')[1]
            print(html_data)
            self.client.close()

            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True



        # data = b""
        # while True:  # 不需要自己循环调用
        #     try:
        #         d = self.client.recv(1024)
        #     except BlockingIOError as e:
        #         continue
        #     if d:
        #         data += d
        #     else:
        #         break


    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == '':
            self.path = "/"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册事件到select,因为现在是send操作,所以注册写的事件
        selector.register(self.client.fileno(), EVENT_WRITE, self.connect)


def loop():
    # 事件循环,不停地请求socket的状态并调用对应的回调函数
    # geven 协程等都是用的回调+事件循环+select的模式
    # 1.select本身不支持register模式(所以要用defaultselector)
    # 2.socket状态变化后的回调是由程序员完成的(aio才是自动完成)
    while not stop:
        ready = selector.select()
        # 在window下会报错(OSError: [WinError 10022] 提供了一个无效的参数) 因为window默认调用select linux默认epoll
        for key, mask in ready:
            call_back = key.data  # 获取回调函数
            call_back(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()
