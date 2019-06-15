# -*- coding:utf-8 -*-

import os
import time
# fork只能用于linux/unix中

# 在输出的结果中 boddy会输出两次 下面的if else都会输出
# 因为fork会创建一个子进程 子进程会将父进程中os.fork()下面的代码全部原样拷贝
# print("boddy")  当boddy在这里  只会输出一遍
# pid = os.fork()
# print("boddy")
# if pid == 0 :
#     print('子进程 {}, 父进程 {}'.format(os.getpgid()), os.getppid())
# else:
#     print('我是父进程: {}'.format(pid))
#
# time.sleep(2)
import multiprocessing  # 多进程更底层的包

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub process")
    return n

class Myprocess(multiprocessing.Process):
    def run(self):
        pass

if __name__ == '__main__':
    import os
    progress = multiprocessing.Process(target=get_html, args=(0.2,))
    print(progress.pid)  # 没有start 是没有进程id的
    progress.start()
    print(progress.pid)
    progress.join()
    print("main process")

    # 使用multiprocess的线程池
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3, ))

    # 等待所有任务完成
    # pool.close()  # 必须先关闭pool,使它不会在接受任务
    # pool.join()
    # print(result.get())

    #imap   与imap_unordered相比 只是输出顺序不一样
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))

    # imap_unordered
    # for result in pool.imap_unordered(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))

