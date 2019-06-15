# -*- coding:utf-8 -*-

'''sys.path注意点'''
import sys, os
# import packA.a1
# print(sys.path)
# 输出   因为sys.path是导入模块所共享的  所以packA.a1中也可访问与start同级目录下的other.py
# this is other.py
# this is packA.a1.py

'''__init__.py详解'''
# import packA  # "import packA.a1" will work just the same
# print(packA)  # <module 'packA' from 'C:\\myApp\\PycharmProjects\\study\\test_package\\packA\\__init__.py'>
# packA.packA_func()  # running packA_func()
# packA.a2_func()  # running a2_func()
# packA.a2.a2_func()  # running a2_func()

'''absolute导入与relative导入：重点'''
# print(sys.path)
# print(os.path.abspath('.'))


'''案例'''
# from packA.subA.sa1 import helloWorld

from packA import a2