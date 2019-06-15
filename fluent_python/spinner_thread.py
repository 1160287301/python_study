# -*- coding:utf-8 -*-
import itertools
import sys
import threading
import time


class Signal:
    go = True


def spin(msg, Signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        write('\x08' * len(status))
        time.sleep(.1)
        if not Signal.go:
            break

    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking', Signal))
    print("spinner object:", spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("answer:", result)


if __name__ == '__main__':
    main()
