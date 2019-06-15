# -*- coding:utf-8 -*-


import requests

session = requests.session()

# 前置请求
url = 'https://web.immomo.com/live/404349330'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
r = session.get(url=url, headers=headers)

url = 'https://web.immomo.com/webmomo/api/scene/profile/roominfos'
data = {
    'stid': '404349330',
    'src': 'url',
}
headers = {
    'Origin': 'https://web.immomo.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://web.immomo.com/live/404349330',
}
r = session.post(url=url, data=data, headers=headers)
url = 'https://web.immomo.com/webmomo/api/scene/recommend/lists'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Referer': 'https://web.immomo.com/live',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}
r = session.post(url=url, headers=headers)
print(session.cookies)
print(r.text)