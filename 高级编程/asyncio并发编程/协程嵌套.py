# -*- coding:utf-8 -*-

# 1.run_until_complete  # 在运行指定的协程后会停止
import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()  # 不会停止,会一直运行

# 1.loop会被放到future中
# 2.取消future/task

import asyncio
import time


async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))


async def compute(x, y):
    print("compute %s + %s..." % (x, y))
    await asyncio.sleep(1)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


if __name__ == '__main__':
    # task1 = get_html(2)
    # task2 = get_html(3)
    # task3 = get_html(3)
    #
    # tasks = [task1, task2, task3]
    # loop = asyncio.get_event_loop()
    # try:  # 当按下ctrl + c 想终止协程
    #     loop.run_until_complete(asyncio.wait(tasks))
    # except KeyboardInterrupt as e:
    #     all_task = asyncio.Task.all_tasks()
    #     for task in all_task:
    #         print("cancel task")
    #         print(task.cancel())
    #     loop.stop()
    #     loop.run_forever()
    # finally:
    #     loop.close()

    # 协程嵌套
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
