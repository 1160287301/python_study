# -*- coding:utf-8 -*-


# 生成器表达式
odd_gen = (i for i in range(10) if i % 2 ==1)
print(type(odd_gen))
print(odd_gen)
odd_gen = list(odd_gen)
print(type(odd_gen))
print(odd_gen)


# 字典推导式
mydict = {'1': 11, '2': 22, '3': 33}
dict_reversed = {value:key for key, value in mydict.items()}
print(dict_reversed)


# 集合推导式
myset = {key for key, value in mydict.items()}
print(type(myset))
print(myset)