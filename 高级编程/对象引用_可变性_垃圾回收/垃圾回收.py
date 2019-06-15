# -*- coding:utf-8 -*-

# python中的垃圾回收的算法是曹勇 引用计数
a = 1
b = a
# 此时1上面有两个引用


a = object()
b = a
del a
print(b)
print(a)


class A:
    def __del__(self):
        # 使用del语句的时候  python会调用del魔法函数
        pass
