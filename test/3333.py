# -*- coding:utf-8 -*-

import requests


url = 'http://shaoq.com:7777/exam'
url = 'http://shaoq.com:7777/img/2.png'
r = requests.get(url=url)
print(r.content)