# -*- coding:utf-8 -*-

# python2.2之前  class a:  a不会继承object
# 之后 会继承 称之为新式类


# c3算法

# __mro__  输出属性查找顺序


class a:
    def __init__(self):
        pass
class b(a):
    def __init__(self):
        super().__init__()
# 当继承多个类super().__init__()方法䦹按照mro算法
# 加载父类的init方法的
# 所以python不推荐继承多个类


print(b.__mro__)

# mixin继承模式特点
#1,mixin类功能单一
#2.不和基类关联可以和任意基类组合,基类可以不和minix关联就能初始化成功
#3.在minix中不要使用super().__init__这种用法
string = "iphone"

def aa(string):
    if 'iphone' in string:
        return 'ios'
    elif not string:
        return None
    else:
        return 'android'