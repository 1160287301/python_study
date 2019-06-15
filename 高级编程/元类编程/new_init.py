# -*- coding:utf-8 -*-

class User:
    def __new__(cls, *args, **kwargs):
        # 生产对象之前调用的方法,能对类进行操作
        print(" in new")
        return super().__new__(cls)  # 不return不会调用init方法

    def __init__(self, name):
        # init函数的参数需要和new函数的参数保持一致
        print(" in init")
        self.name = name
        pass

# new是用来控制对象的生成过程,在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象 则不会调用init函数 return super().__new__(cls)
if __name__ == '__main__':
    a = User("aa")
