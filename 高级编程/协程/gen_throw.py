# -*- coding:utf-8 -*-

def gen_fun():
    # 1.可以产出值 2.可以接受值(调用方传递过来的值)
    try:
        yield "url"
    except Exception as e:
        print(e.args)
    yield 1
    yield 2
    yield 3
    return 4

if __name__ == '__main__':
    gen = gen_fun()
    print(next(gen))
    gen.throw(Exception, "download error")