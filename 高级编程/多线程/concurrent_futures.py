# -*- coding:utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import Future

# future:未来对象(task的返回容器)



# 为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态,以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中, submit是立即返回的,也就是主线程和子线程一起运行
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# done方法判断某个线程是否运行完成
# print(task1.done())
# # 在线程运行前可以cancel
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# # result方法可以获取task的执行结果
# print(task1.result())

# 要获取已经成功的task的返回值
urls = [1, 2, 3]
all_task = [executor.submit(get_html, (url)) for url in urls]
for future in as_completed(all_task):
    data = future.result()
    print("get {} page".format(data))

# 通过executor获取已经完成的task
# urls = [1, 2, 3]
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))

# from concurrent.futures import wait, FIRST_COMPLETED
# urls = [1, 2, 3]
# all_task = [executor.submit(get_html, (url)) for url in urls]
# wait方法: 设置多少个线程执行完后,在执行主线程
# return_when=FIRST_COMPLETED  执行完一个线程后,打印main(执行主线程)
# wait(all_task, return_when=FIRST_COMPLETED)
# print("main")