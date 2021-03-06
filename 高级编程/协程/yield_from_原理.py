# -*- coding:utf-8 -*-
# pep380


# 1.RESULT = yield from EXPR可以简化成下面这样
# 一些说明
'''
_i: 子生成器,同时也是一个迭代器
_y: 子生成器生产的值
_r: yield from 表达式最终的值
_s: 调用方通过send()发送的值
_e: 异常对象
'''

# _i = iter(EXPR)  # expr是一个可迭代对象,_i其实是生成器
# try:
#     _y = next(_i)  # 预激子生成器,把产出的第一个值存在_y中
# except StopIteration as _e:
#     _r = _e.value  # 如果抛出了StopIteration异常, 那么将对象的value赋值
# else:
#     while 1:  # 尝试执行这个循环, 委托生成器会阻塞
#         _s = yield _y  # 生产子生成器的值,等等调用方send()值, 发送过来的值将保存在_s中
#         try:
#             _y = _i.send(_s)  # 转发_s, 并且尝试向下执行
#         except StopIteration as _e:
#             _r = _e.value  # 如果子生成器抛出异常, 那么获取异常对象的'value'属性存到
#             break
# RESULT = _r  # _r就是整个yield from 表达式返回的值


#  总结

'''
1.子生成器生产的值,都是直接传给调用方的,调用方通过.send()发送的值都是直接传递给子生成器的;如果发送的是None,会调用子生成器的__next__()方法,如果不是None,会调用子生成器的.send()方法;
2.子生成器退出的时候,最后的return EXPR,会触发一个StopIteration(EXPR)异常
3.yield from表达式的值,是子生成器终止的,传递给StopIteration异常的第一个参数
4.如果调用的时候出现StopIteration异常,委托生成器会恢复运行.同时其他的异常会向上冒泡
5.传入委托生成器的异常里,除了GeneratorExit之外,其他的所有的异常全部传递给子生成器.throw()方法;如果调用throw()的时候出现了StopIteration异常,那么就恢复委托生成器的运行,其他的异常全部向上冒泡
6.如果在委托生成器上调用.close()或传入除了GeneratorExit之外异常,会调用子生成器的.close()方法,没有的话就不调用.如果在调用.close()的时候抛出异常,那么就向上冒泡,否则的话委托生成器会抛出GeneratorExit异常
'''