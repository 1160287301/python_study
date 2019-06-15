# -*- coding:utf-8 -*-
from collections import abc

a = [1, 2]
c = a + [3, 4]
# c = a + (4, 5,)  # 报错
a += [3, 4]
print(a)
a += (4, 5,)
print(a)
a.extend(range(3))
print(a)
a.append(range(3))
print(a)
