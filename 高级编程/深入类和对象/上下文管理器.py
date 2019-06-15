# -*- coding:utf-8 -*-


import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {'1': '2'}
    print("file end")


with file_open("111.txt") as f:
    print(f.get('1'))