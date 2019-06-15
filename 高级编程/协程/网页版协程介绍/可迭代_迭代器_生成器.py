# -*- coding:utf-8 -*-

import collections
from collections.abc import Iterator, Iterable, Generator


import collections
from collections.abc import Iterable, Iterator, Generator

# # 字符串
# astr = "XiaoMing"
# print("字符串：{}".format(astr))
# print(isinstance(astr, Iterable))
# print(isinstance(astr, Iterator))
# print(isinstance(astr, Generator))
#
# # 列表
# alist = [21, 23, 32,19]
# print("列表：{}".format(alist))
# print(isinstance(alist, Iterable))
# print(isinstance(alist, Iterator))
# print(isinstance(alist, Generator))
#
# # 字典
# adict = {"name": "小明", "gender": "男", "age": 18}
# print("字典：{}".format(adict))
# print(isinstance(adict, Iterable))
# print(isinstance(adict, Iterator))
# print(isinstance(adict, Generator))
#
# # deque
# adeque=collections.deque('abcdefg')
# print("deque：{}".format(adeque))
# print(isinstance(adeque, Iterable))
# print(isinstance(adeque, Iterator))
# print(isinstance(adeque, Generator))
class MyList(object):  # 定义可迭代对象类

    def __init__(self, num):
        self.end = num  # 上边界

    # 返回一个实现了__iter__和__next__的迭代器类的实例
    def __iter__(self):
        return MyListIterator(self.end)


class MyListIterator(object):  # 定义迭代器类

    def __init__(self, end):
        self.data = end  # 上边界
        self.start = 0

    # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self
    def __iter__(self):
        return self

    # 迭代器类必须实现的方法，若是Python2则是next()函数
    def __next__(self):
        while self.start < self.data:
            self.start += 1
            return self.start - 1
        raise StopIteration


# if __name__ == '__main__':
    # my_list = MyList(5)  # 得到一个可迭代对象
    # print(isinstance(my_list, Iterable))  # True
    # print(isinstance(my_list, Iterator))  # False
    # # 迭代
    # for i in my_list:
    #     print(i)

    # my_iterator = iter(my_list)  # 得到一个迭代器
    # print(isinstance(my_iterator, Iterable))  # True
    # print(isinstance(my_iterator, Iterator))  # True
    #
    # # 迭代
    # print(next(my_iterator))
    # print(next(my_iterator))
    # print(next(my_iterator))
    # print(next(my_iterator))
    # print(next(my_iterator))
    # print(next(my_iterator))  # StopIteration

    # print(dir(my_list))
    # print(dir(my_iterator))

###################################################################################################################

# def mygen(n):
#     now = 0
#     while now < n:
#         yield now
#         now += 1
#
# def myfun(n):
#     now = 0
#     while now < n:
#         1
#         now += 1
#
# if __name__ == '__main__':
#     gen = mygen(4)
    # gen = myfun(4)

    # 通过交替执行，来说明这两种方法是等价的。
    # 预激生成器必须发送None的原因
    # 当一个函数使用了yield 那这个函数就不是普通的函数
    # 运行了gen = mygen(4)之后  字节码不会运行到yield now这一行
    # 所以send一个非空的值 这个值就没有能赋值的对象
    # print(gen.send(None))
    # print(next(gen))
    # print(gen.send(None))
    # print(next(gen))

###################################################################################################################
# from inspect import getgeneratorstate
#
# def mygen(n):
#     now = 0
#     while now < n:
#         yield now
#         now += 1
#
# if __name__ == '__main__':
#     gen = mygen(2)
#     print(getgeneratorstate(gen))
#
#     print(next(gen))
#     print(getgeneratorstate(gen))
#
#     print(next(gen))
#     gen.close()  # 手动关闭/结束生成器
#     print(getgeneratorstate(gen))
###################################################################################################################
# def mygen(n):
#     now = 0
#     while now < n:
#         yield now
#         now += 1
#     raise StopIteration
#
# if __name__ == '__main__':
#     gen = mygen(2)
#     next(gen)
#     next(gen)
#     next(gen)
###################################################################################################################
def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    itr = jumping_range(5)
    print(next(itr))
    print(itr.send(2))
    print(next(itr))
    print(itr.send(-1))
