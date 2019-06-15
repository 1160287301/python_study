# -*- coding:utf-8 -*-


def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError:
        print("Keyerror")
        return 2
    else:
        print("else")
        return 3
    finally:
        print("finally")
        return 4

print(exe_try())
# code started
# Keyerror
# finally
# 4
# 打印code started->将2压入栈帧->打印finally->将4压入栈帧->后进先出原则->返回4