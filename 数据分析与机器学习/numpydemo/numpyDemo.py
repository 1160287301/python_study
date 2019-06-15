# -*- coding:utf-8 -*-

import numpy

# 读取txt文件
# txt = numpy.genfromtxt('test.txt', delimiter=",", dtype=str)
# print(type(txt))
# print(txt)
# print(help(numpy.genfromtxt))
# print(txt.shape)

# numbers = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(numbers)
# print(numbers.dtype)
# print(numbers.shape)
# print(numbers[0, 3])
# print(numbers[:, 3])

# numbers = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# index_ = (numbers == 2)
# print(index_)
# print(numbers[index_])  # 通过索引取值
# print((numbers == 2) & (numbers == 3))  # 与
# print((numbers == 2) | (numbers == 5))  # 或
# print(numbers.sum(axis=1))  # 求每行的和
# print(numbers.sum(axis=0))  # 求每列的和

# vector = numpy.array(["1", "2", "3"])
# print(vector.dtype)
# print(vector)
# vector = vector.astype(float)  # 类型转换
# print(vector.dtype)
# print(vector)
# print(vector.min())  # 求极值

# a = numpy.arange(18)
# print(a)
# a = a.reshape(3, 6)
# print(a)
# print(a.ndim)  # 维度  该矩阵是二维  输出2
# print(a.dtype.name)
# print(a.size)

# a = numpy.zeros((3, 4))
# print(a)  # 初始化3行4列 元素为0的矩阵
# a = numpy.ones((3, 3, 4), dtype=numpy.str)  # 3层 3行 4列
# print(a)

# a = numpy.arange(1, 10, 1)  # [1 2 3 4 5 6 7 8 9]
# print(a)
# print(a.size)
# print(a.reshape((3, 3)))

# a = numpy.random.random((2, 3))  # -1 到 +1区间里的值
# print(a)

# a = numpy.linspace(0, 2*numpy.pi, 100)  # 从0到2*π  平均取 100个值
# print(a)
# a = numpy.array([30])
# print(numpy.sin(a))

# a = numpy.array([20, 30, 40, 50])
# b = numpy.arange(4)
# print(a-b)  # [20 29 38 47]
# print(a-1)  # 每个元素都减一
# print(b**2)  # 平方
# print(a<=35)


# a = numpy.array([[1, 1], [0, 1]])
# b = numpy.array([[2, 0], [3, 4]])
# print(a)
# print(b)
# print('-'*10)
# print(a*b)  # 相同索引想乘
# print('-'*10)
# print(a.dot(b))  # 第一行乘第一列  第一行乘第二列 第二行乘第一列 第二行乘第二列
# print(numpy.dot(a, b))


# b = numpy.arange(3)
# print(b)
# print(numpy.exp(b))  # 求e的指数
# print(numpy.sqrt(b))  # 开根号

# a = numpy.floor(10 * numpy.random.random((3, 4)))  # -10到10 3行4列 向下取整
# print(a)
# print(a.ravel())  # 矩阵变向量
# print(a.shape)
# a.shape = (6, 2)  # 改变矩阵行列
# print(a)
# print(a.T)  # 行列转换
# print(a.reshape(3, -1))  # 填-1 会自动帮忙计算

# a = numpy.floor(10 * numpy.random.random((2, 2)))
# b = numpy.floor(10 * numpy.random.random((2, 2)))
# print(a)
# print(b)
# print(numpy.hstack((a, b)))  # 矩阵横着拼接 第一行+第一行 第二行+第二行
# print(numpy.vstack((a, b)))  # 矩阵竖着拼接


# a = numpy.floor(10 * numpy.random.random((5, 5)))
# print(a)
# print(numpy.hsplit(a, 3))  # 按行分 分3行
# print(numpy.hsplit(a, (3, 4)))
# print(numpy.vsplit(a, (3, 4)))

# a = numpy.floor(10 * numpy.random.random((3, 3)))
# c = a.view()  # 浅拷贝
# c = a.copy()  # 深拷贝
# print(c)
# c[1, 1] = 1234
# print(a)

# data = numpy.sin(numpy.arange(20)).reshape(5, 4)
# print(data)
# ind = data.argmax(axis=0)  # 按列分最大值的索引
# print(ind)
# data_max = data[ind, range(data.shape[1])]  # 取出最大值
# print(data_max)

# a = numpy.arange(0, 40, 10)
# print(a)
# b = numpy.tile(a, (2, 3))  # 扩展
# print(b)

# a = numpy.array([[4, 3, 5], [1, 2, 1]])
# print(a)
# b = numpy.sort(a, axis=1)  # 按行排序  axis=0 按列排序
# print(b)

a = numpy.array([4, 3, 1, 2])
print(a)
j = numpy.argsort(a)  # 求array里面大小排序的索引(默认升序) 输出[2 3 1 0]
print(j)
print(a[j])  # 排序完成后的结果