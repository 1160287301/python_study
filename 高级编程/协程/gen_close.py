# -*- coding:utf-8 -*-

def gen_fun():
    try:
        yield "url"
    except GeneratorExit:  # 继承baseexception
    # except Exception:  # 正常运行 不抛异常
        # pass # 会在gen.close()抛异常RuntimeError: generator ignored GeneratorExit
        raise StopIteration # 会在close下面的next抛异常StopIteration
    yield 1
    yield 2
    yield 3
    return "body"

if __name__ == '__main__':
    gen = gen_fun()
    print(next(gen))
    gen.close()  # 会在两次next之间抛出异常StopIteration
    print(next(gen))
