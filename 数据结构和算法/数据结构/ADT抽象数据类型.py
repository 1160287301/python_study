# -*- coding:utf-8 -*-

class Bag:

    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, 'item must in the bag'
        return self._items.remove(item)

    def __iter__(self):
        return _BagIterator(self._items)


class _BagIterator:
    def __init__(self, seq):
        self._bag_item = seq
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self._bag_item):
            item = self._bag_item[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


b = Bag()
b.add(1)
b.add(2)
for i in b:  # for使用__iter__构建，用__next__迭代
    print(i)

"""
# for 语句等价于
i = b.__iter__()
while True:
    try:
        item = i.__next__()
        print(item)
    except StopIteration:
        break
"""
