# -*- coding:utf-8 -*-
import numbers
class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("need int value")
        self.value = value  # 如果写instance.value  会无限递归

    def __delete__(self, instance):
        pass


class NonDateIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()

'''
如果user是某个类的实例,那么user.age(等价于getattr(user,'age'))
首先调用 __getattribute__ 如果定义了__getattr__方法,
那么在 __getattribute__ 抛出attributeerror的时候就会调用__getattr__,
而对于描述符(__get__)的调用,这是发生在__getattribute__内部的
user = User() 那么user.age 顺序如下

1 如果age是出现在User或其基类的__dict__中,且age是data descriptor, 那么调用数据描述符的__get__方法
2 如果age出现在user的__dict__中,那么直接返回obj.__dict__['age']
3 如果age出现在User或其基类的__dict__中
    1.如果age是non-data descriptor,那么调用其__get__方法,否则返回__dict__['age']
    2.如果User有__getattr__方法, 那就调用__getattr__方法,否则抛出attributeerror
'''
if __name__ == '__main__':
    u = User()
    u.age = 1  # 会调用IntField.__set__方法
    # print(u.age)