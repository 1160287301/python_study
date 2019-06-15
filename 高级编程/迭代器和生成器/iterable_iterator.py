# -*- coding:utf-8 -*-
from collections.abc import Iterator

class Company:
    def __init__(self, e_list):
        self.employee = e_list

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)

    def __iter__(self):
        return Myiterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]

# 自定义迭代器
class Myiterator(Iterator):
    def __init__(self, a_list):
        self.list_ = a_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 真正返回迭代值得方法
        try:
            word = self.list_[self.index]
        except IndexError:  # 因为使用的list做例子 list只会报IndexError
            raise StopIteration  # for语句只能处理StopIteration
        self.index += 1
        return word

if __name__ == '__main__':
    c = Company([1, 2, 3, 4])
    for i in c:  # 会先寻找__iter__方法  没有就照__getitem__  还没有就报错
        print(i)
        # next(i)

    # for循环做的事
    # c_itor = iter(c)
    # while True:
    #     try:
    #         next(c_itor)
    #     except StopIteration:
    #         pass