# -*- coding:utf-8 -*-
import os
import time

import win32
import requests
from zs_factor import getip



# def get_proxy():
#     env = os.environ
#     topic = env.get("ZS_FACTOR_TOPIC", "fixed,dailiyun,wasp")
#     group = env.get("ZS_FACTOR_GROUP", 'guazi')
#     num = env.get("ZS_FACTOR_NUM", 20)
#     return getip(topic, group=group, num=num)
#
# start_time = time.time()
# for i in range(100):
#     print(get_proxy())
# # print(get_proxy())
# print(time.time() - start_time)

def y(col=10):
    ll = None
    for i in range(1, col+1):
        if i <= 2:
            ll = [1] * i
            print(ll)
        else:
            aa = [1]
            for j in range(1, i-1):
                aa.append(ll[j] + ll[j-1])
            aa.append(1)
            print(aa)
            ll=aa
y()