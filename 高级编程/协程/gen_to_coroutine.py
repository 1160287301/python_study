# -*- coding:utf-8 -*-
# 生成器是可以暂停的函数
import inspect
def gen_func():
    # 1.返回值给调用方 2.调用方通过send方式返回值给gen
    value = yield 1
    return "bobby"

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))  # 获取状态
    next(gen)
    print(inspect.getgeneratorstate(gen))  # 获取状态
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))  # 获取状态
