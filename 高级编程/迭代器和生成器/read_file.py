# -*- coding:utf-8 -*-
# 读500g文件
# 如果是一行一行的可以用with open

# 只有一行
def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):  # 文件, 分隔符
        print(line)
