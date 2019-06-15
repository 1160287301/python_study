# -*- coding:utf-8 -*-


'''
array: 定长，操作有限，但是节省内存
list: 会预先分配内存，操作丰富，但是耗费内存
'''

'''
list.append: 如果之前没有分配够内存，会重新开辟新区域，然后复制之前的数据，复杂度退化
list.insert: 会移动被插入区域后所有元素,O(n)
list.pop: pop不同位置需要的复杂度不同pop(0)是O(1)复杂度,pop()首位O(n)复杂度
list[]: slice操作copy数据（预留空间）到另一个list
'''
import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, 'array size must be > 0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._element = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        assert len(self) > item >= 0, 'out of rang'
        return self._element[item]

    def __setitem__(self, key, value):
        assert len(self) > key >= 0, 'out of rang'
        self._element[key] = value

    def clear(self, value):
        ''' 设置每个元素为value '''
        for i in range(len(self)):
            self._element[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idex < len(self._items):
            val = self._items[self._idx]
            self._idex += 1
            return val
        else:
            raise StopIteration


# a = Array(size=5)
# a[0] = 0
# print(len(a))
# print(a[1])

# 二维数组
class Array2D:
    def __init__(self, numrows, numcols):
        self._the_rows = Array(numrows)
        for i in range(numrows):
            self._the_rows[i] = Array(numcols)
        self.clear(None)

    @property
    def numRows(self):
        return len(self._the_rows)

    @property
    def numCols(self):
        return len(self._the_rows[0])

    def clear(self, value):
        for row in self._the_rows:
            row.clear(value)

    def __getitem__(self, item):
        assert len(item) == 2
        row, col = item[0], item[1]
        assert (self.numRows > row >= 0) and (self.numCols > col >= 0)
        return self._the_rows[row][col]

    def __setitem__(self, ndx_tuple, value):
        assert len(ndx_tuple) == 2
        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and
                col >= 0 and col < self.numCols)
        the_1d_array = self._the_rows[row]
        the_1d_array[col] = value

    def __str__(self):
        return