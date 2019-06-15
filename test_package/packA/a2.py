# -*- coding:utf-8 -*-
import os
import sys

print("this is a2.py")

def a2_func():
    print("running a2_func()")


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from packA.subA import sa2

