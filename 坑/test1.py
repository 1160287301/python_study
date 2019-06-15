# -*- coding:utf-8 -*-


# 坑1
# class A(object):
#     x = 1
#     gen = (x for _ in range(10))  # gen=(x for _ in range(10))
#
#
# if __name__ == "__main__":
#     print(list(A.gen))
'''
这个问题是变量作用域问题，在 gen=(x for _ in xrange(10)) 中 gen 是一个 generator ,在 generator 中变量有自己的一套作用域，与其余作用域空间相互隔离。因此，将会出现这样的 NameError: name 'x' is not defined 的问题，那么解决方案是什么呢？答案是：用 lambda 。
'''
# 填坑1
# class A(object):
#     x = '1'
#     gen = (lambda x: (x for _ in range(10)))(x)  # gen=(x for _ in range(10))
#
#
# if __name__ == "__main__":
#     print(list(A.gen))
########################################################################################################################
# 坑2
import time
# class Timeit(object):
#     def __init__(self, func):
#         self._wrapped = func
#
#     def __call__(self, *args, **kws):
#         start_time = time.time()
#         result = self._wrapped(*args, **kws)
#         print("elapsed time is %s " % (time.time() - start_time))
#         return result

# 这个装饰器能够运行在普通函数上：
# @Timeit
# def func():
#     time.sleep(1)
#     return "invoking function func"
# if __name__ == '__main__':
#     func()  # output: elapsed time is 1.00044410133
# 运行在方法上会报错
# class A(object):
#     @Timeit
#     def func(self):
#         time.sleep(1)
#         return 'invoking method func'
# if __name__ == '__main__':
#     a = A()
#     a.func()  # Boom!
# 填坑2
class Timeit(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('invoking Timer')
    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)

class A(object):
    @Timeit
    def func(self):
        time.sleep(1)
        return 'invoking method func'


@Timeit
def func1():
    time.sleep(1)
    return "invoking function func"
if __name__ == '__main__':
    a = A()
    # a.func()  # Boom!
    func1()