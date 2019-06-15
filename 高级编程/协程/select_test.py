# -*- coding:utf-8 -*-

# 1.epoll并不代表一定比select好
# 在并发高,连接活跃度不高(电商网站),epoll比select好
# 并发性不高,同时连接很活跃(游戏),select比epoll好

# 通过非阻塞io实现http请求

import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = "/"
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  # 不会等待3次握手
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    # 阻塞不会消耗CPU
    # 需要while不停地循环去检查状态,询问连接是否建立好
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()

if __name__ == '__main__':
    get_url("http://www.baidu.com")