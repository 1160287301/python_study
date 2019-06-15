# -*- coding:utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
# 多进程编程
# 耗cpu的操作,用多进程编程,对于io操作来说,使用多线程编程,进程切换代价要高于线程

# 1.对于耗cpu的操作,多进程优于多线程


def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)


# with ThreadPoolExecutor(3) as executor:
# window下使用多进程会报错,这时放在main下执行就可(concurrent.futures.process.BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.)
# if __name__ == '__main__':
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25,35)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exe result: {}".format(data))
#
#         print("time is:{}".format(time.time()-start_time))


# 2.对于io操作来说,多线程优于多进程
def rendom_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(rendom_sleep, (num)) for num in [2] * 20]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("time is:{}".format(time.time()-start_time))