# -*- coding:utf-8 -*-


# __getattr__ 在差找不到属性的时候调用
# __getattribute__ 访问属性就调用
class A:
    aaa = {
        '1': 1
    }
    def __init__(self, name, info={}):
        self.name = name
        self.info = info

    def __getattr__(self, item):
        return "no"

    def __getattribute__(self, item):
        # return "__getattribute__"
        print(1)

    def add(self, key, value):
        self.info[key] = value

if __name__ == '__main__':
    a = A("bobby")
    # b = A("bobby")
    # print(a.name)
    print(a.name1)
    # a.add('a', 'b')
    # print(a.info)
    # print(b.info)