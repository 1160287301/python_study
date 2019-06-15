# -*- coding:utf-8 -*-

# 不建议继承list和dict
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)
#
#
# my_dict = Mydict(one=1)
# print(my_dict)
# my_dict['one'] = 1
# print(my_dict)
#
# # 需要继承userdict
# from collections import UserDict
#
# class Mydict(UserDict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)
#
# dict1 = Mydict(one=1)
# print(dict1)


# defaultdict  __missing__方法
from collections import defaultdict
my_dict = defaultdict(dict)
print(my_dict['a'])
my_dict1 = defaultdict(list)
print(my_dict1['a'])