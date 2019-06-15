# -*- coding:utf-8 -*-

class People:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print("deleter name")
        del self._name

if __name__ == '__main__':
    p = People("bobby")
    print(p.name)
    p.name = "lisa"
    print(p.name)
    del p.name