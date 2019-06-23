# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 对象创建
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# dates = pd.date_range('20170101', periods=7)
# print(dates)
#
# df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
# print(df)
# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20170102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo'})
#
# print(df2)

# 查看数据
dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
print(df.head())
print("--------------" * 10)
print(df.tail(3))
print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(df.values)

