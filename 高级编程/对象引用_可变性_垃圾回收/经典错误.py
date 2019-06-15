# -*- coding:utf-8 -*-

def add(a, b):
    a += b  # 当a是列表(可变)时  += 操作会改变a的值
    return a

class Company:
    def __init__(self, stuffs=[]):
        self.stuff = stuffs

    def add(self, name):
        self.stuff.append(name)

if __name__ == '__main__':
    # a = 1
    # b = 2
    # c = add(a, b)
    # print(c)
    # print(a, b)
    #
    # a = [1, 2]
    # b = [3, 4]
    # c = add(a, b)
    # print(c)
    # print(a, b)
    #
    # a = (1, 2)
    # b = (3, 4)
    # c = add(a, b)
    # print(c)
    # print(a, b)

    com1 = Company()
    com2 = Company()
    com1.add('com1_staff')
    # com1和com2使用的是同一个staff列表
    print(com2.stuff)
    print(Company.__init__.__defaults__)  # 当初始化没有传递stuff是,都会使用这个值