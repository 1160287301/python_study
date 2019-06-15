# -*- coding:utf-8 -*-

# ~*~ Twisted - A Python tale ~*~
from time import sleep
import threading
# Hello, I'm a developer and I mainly setup Wordpress.
def install_wordpress(customer):
   # Our hosting company Threads Ltd. is bad. I start installation
        print("Start installation for", customer)
        # ...then wait till the installation finishes successfully. It is
        # boring and I'm spending most of my time waiting while consuming
        # resources (memory and some CPU cycles). It's because the process
        # is *blocking*.
        sleep(3)
        print("All done for", customer)
# I do this all day long for our customers
def developers_day(customers):
    # But we now have to synchronize... a.k.a. bureaucracy
    lock = threading.Lock()
    #
    def dev_day(id):
        print("Goodmorning from developer", id)
        # Yuck - I hate locks...
        lock.acquire()
        while customers:
            customer = customers.pop(0)
            lock.release()
            # My Python is less readable
            install_wordpress(customer)
            lock.acquire()
        lock.release()
        print("Bye from developer", id)
    # We go to work in the morning
    devs = [threading.Thread(target=dev_day, args=(i,)) for i in
range(5)]
    [dev.start() for dev in devs]
    # We leave for the evening
    [dev.join() for dev in devs]
# We now get more done in the same time but our dev process got more
# complex. As we grew we spend more time managing queues than doing dev
# work. We even had occasional deadlocks when processes got extremely
# complex. The fact is that we are still mostly pressing buttons and
# waiting but now we also spend some time in meetings.
developers_day(["Customer %d" % i for i in range(15)])
