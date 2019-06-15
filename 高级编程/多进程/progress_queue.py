# -*- coding:utf-8 -*-
import time
from multiprocessing import Process, Queue, pool


def prodecer(queue):
    queue.put("a")
    time.sleep(2)

def prodecer1(a):
    a + 1

def prodecer2(a):
    a.send("a")

def prodecer3(a):
    a['prodecer3'] = 'prodecer3'


def consumer(queue):
    print(queue.get())

def consumer1(a):
    print(a)

def consumer2(a):
    print(a.recv())

def consumer3(a):
    a['consumer3'] = 'consumer3'


if __name__ == '__main__':
    # 通信1 使用multiprocessing.queen
    # queue = Queue(maxsize=10)
    # p = Process(target=prodecer, args=(queue,))
    # c = Process(target=consumer, args=(queue,))
    # p.start()
    # c.start()
    # p.join()
    # c.join()

    # 使用共享全局变量不适用与多进程
    # a = 1
    # p = Process(target=prodecer1, args=(a,))
    # c = Process(target=consumer1, args=(a,))
    # p.start()
    # c.start()
    # p.join()
    # c.join()

    # 方法2 multiprocessing中的queue不能用于pool进程池
    # 此处只能使用Manager对象中的Queue()
    # import multiprocessing
    # from multiprocessing import Manager
    # queue = Manager().Queue()
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # pool.apply_async(prodecer, args=(queue, ))
    # pool.apply_async(consumer, args=(queue, ))
    # pool.close()  # 必须先关闭pool,使它不会在接受任务
    # pool.join()

    # 方法3 通过pipe实现进程中的通信
    # pipe只能用于两个进程中的通信, 但性能优于queue
    # from multiprocessing import Pipe
    # recevie_pipe, send_pipe = Pipe()
    #
    # p = Process(target=prodecer2, args=(send_pipe,))
    # c = Process(target=consumer2, args=(recevie_pipe,))
    # p.start()
    # c.start()
    # p.join()
    # c.join()

    # 方法4 可以使用manager的数据类型
    from multiprocessing import Manager
    progress_dict = Manager().dict()
    p = Process(target=prodecer3, args=(progress_dict,))
    c = Process(target=consumer3, args=(progress_dict,))
    p.start()
    c.start()
    p.join()
    c.join()

    print(progress_dict)





