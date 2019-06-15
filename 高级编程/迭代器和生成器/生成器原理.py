# -*- coding:utf-8 -*-

# 1.python中函数的工作原理
import inspect

frame = None


def bar():
    global frame
    frame = inspect.currentframe()


def foo():
    bar()


# python.exe会调用一个叫做pyEval_EvalFramEx(C函数)去执行foo函数
# 首先会创建一个栈枕
'''
python一切皆对象 , 栈帧对象
当foo调用子函数 bar 又会创建一个栈帧
所有的栈帧都是分配在堆内存上的 这就决定了栈帧可以独立于调用者存在
'''
import dis
# print(dis.dis(foo))

# foo()
# print(frame.f_code.co_name)  # 打印栈帧
# call_frame = frame.f_back
# print(call_frame.f_code.co_name)  # 打印调用者的栈帧

def gen_func():
    yield 1
    name = "boddy"
    yield 2
    age = 30
    return "ioomm"

gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)  # -1 还没开始调用
print(gen.gi_frame.f_locals)  # {}
next(gen)
print(gen.gi_frame.f_lasti)  # 2 调用到第2行字节码  2 YIELD_VALUE
print(gen.gi_frame.f_locals) # {}
next(gen)
print(gen.gi_frame.f_lasti)  # 12
print(gen.gi_frame.f_locals)  # {'name': 'boddy'}


from collections import UserList