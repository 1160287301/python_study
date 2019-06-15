# -*- coding:utf-8 -*-

import bisect

# 用来处理已排序的序列,用来维持已排序的序列,升序
# 二分查找
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 7)
bisect.insort(inter_list, 5)
print(inter_list)  # [1, 2, 3, 4, 4, 5, 6]

# 返回相同元素的后一个索引
print(bisect.bisect(inter_list, 3))
print(bisect.bisect_left(inter_list, 3))
print(bisect.bisect_right(inter_list, 3))