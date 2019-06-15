# -*- coding:utf-8 -*-

'''
Maps or Dict: 键值对,python内部采用hash实现
'''
class Map:
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, item):
        ndx = self._findPosition(item)
        return ndx is not None

    def add(self, key, value):
        ndx = self._findPosition(key)
        # if ndx

    def _findPosition(self, item):
        pass