# -*- coding:utf-8 -*-
'''
errno模块定义了一些符号错误码，如ENOENT（“找不到该目录”）以及EPERM（“没有权限”）。

如果需要区分不同的错误代码，则可以使用符号名称。
'''
import errno
try:
    fp = open('no.such.file')
except IOError as e:
    # 报错:[Errno 2] No such file or directory: 'no.such.file'
    # 其中e.errno就是数字2
    # if e.errno == errno.ENOENT:
    #     print('no such file')
    # elif e.errno == errno.EPERM:
    #     print('permission denied')
    # else:
    #     print(e)
    print(e)
