# -*- coding:utf-8 -*-

class Set:
    '''使用list实现set ADT'''

    def __init__(self):
        self._theElement = list()

    def __len__(self):
        return len(self._theElement)

    def __contains__(self, item):
        return item in self._theElement

    def add(self, element):
        if element not in self:
            self._theElement.append(element)

    def remove(self, element):
        assert element in self, 'The element must be set'
        self._theElement.remove(element)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            return self.isSubsetOf(other)

    def isSubsetOf(self, setB):
        for element in self._theElement:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

a = Set()
a.add(1)
b = Set()
b.add(2)
a == b