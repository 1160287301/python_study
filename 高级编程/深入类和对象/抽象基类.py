# -*- coding:utf-8 -*-


class Company:
    def __len__(self):
        return len([1, 2, 3])

c = Company()
from collections.abc import Sized
# 1.我们检查某个类是否有某个方法
# 看c是否有__len__方法
# print(isinstance(c, Sized))

# 2.我们需要强制某个子类必须实现某些方法

# 如何去模拟一个抽象基类
# class CachBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def SET(self, key, value):
#         raise NotImplementedError
#
# class Cache1(CachBase):
#     pass
#
# # 如果不重写get set方法 调用时会报错
# cc = Cache1()
# cc.get('1')


# 使用abc写抽象基类
import abc
class CachBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    # @abc.abstractmethod
    # def SET(self, key, value):
    #     pass

class Cache1(CachBase):
    def get(self, key):
        pass
cc = Cache1()
cc.get('1')
