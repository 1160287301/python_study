# -*- coding:utf-8 -*-



## this import makes a1_func directly accessible from packA.a1_func
from packA.a2 import a2_func

def packA_func():
    print("running packA_func()")