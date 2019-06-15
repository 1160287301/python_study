# -*- coding:utf-8 -*-

from threading import Condition
import threading
# 条件变量,用于复杂的线程间的同步
# 通过condition完成读诗
class Xiaoai(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond


    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 好啊".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 君住长江尾".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 共饮长江水".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 此恨何时已".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 定不负相思意".format(self.name))

class Tianmao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫")
        self.cond = cond

    def run(self):
        self.cond.acquire()
        print("{}: 小爱同学".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 我们来对古诗吧".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 我住长江头".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 日日思君不见君".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 此水几时休".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 只愿君心似我心".format(self.name))
        self.cond.notify()

        self.cond.release()

if __name__ == '__main__':
    cond = Condition()
    tianmao = Tianmao(cond)
    xiaoai = Xiaoai(cond)
    # 1启动顺序很重要
    # 2在调用with cond之后才能调用wait或者notify方法
    # 3condition有两层锁,一把底层锁会在线程调用了wait方法的时候释放
    # 上面的锁会在每次调用wait的时候分配一把并放入cond的等待队列中,等待notify方法的唤醒
    xiaoai.start()
    tianmao.start()
