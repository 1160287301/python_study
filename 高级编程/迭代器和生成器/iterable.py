# -*- coding:utf-8 -*-

# 迭代器是访问集合内元素的一种方式,一般用来遍历数据

from collections.abc import Iterable, Iterator
a = [1, 2]  # 可迭代,但不是迭代器
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

a = iter(a)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))


# 实现了__iter__  就是可迭代的Iterable
# 实现了__iter__ __next__ 就是迭代器的 Iterator
