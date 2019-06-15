# -*- coding:utf-8 -*-


# 生成器函数: 函数里只要有yield关键字

def gen_func():
    yield 1
    yield 2
    yield 3


# 惰性求值

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    ll = [0, 1]
    a, b = ll[0], ll[1]
    for _ in range(index - 2):
        a, b = b, a + b
        ll.append(b)
    print(ll)

def gen_fib2(index):
    n, a, b = 0, 0, 1
    while n<index:
        yield b
        a, b = b ,a+b
        n += 1

def func():
    return 1


if __name__ == '__main__':
    # 返回生成器对象 python在编译字节码的时候碰到yield就产生了
    # gen = gen_func()
    # for i in gen:
    #     print(i)
    # fun = func()
    # pass
    fib2(10)
    for i in gen_fib2(3):
        print(i)
