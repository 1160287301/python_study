# -*- coding:utf-8 -*-
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    '1': '1',
    '2': '1',
    '3': '1',
}


# for v in chain(my_list, my_dict, range(5, 10)):
#     print(v)
#
# def my_chain(*args, **kwargs):
#     for iter in args:
#         yield from iter  # 必须要是iterable对象
#
#         # for v in iter:
#         #     yield v
#
#
# for v in my_chain(my_list, my_dict, range(5, 10)):
#     print(v)


def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


# if __name__ == '__main__':
    # for i in g1(range(10)):
    #     print(i)  # 返回range(10)对象
    # for i in g2(range(10)):
    #     print(i)  # 会遍历rang(10)

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 1.main 调用方 g1: 委托生成器  gen:子生成器
# 一般函数 子生成器返回值给委托生成器
# yield from 会在调用方和子生成器中间建立一个双向通道