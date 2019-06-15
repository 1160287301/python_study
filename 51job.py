# -*- coding:utf-8 -*-


import requests

session = requests.session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
}


url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%2B,2,2000.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
headers = {
    'Referer': 'https://search.51job.com/list/010000,000000,0000,00,9,99,%2B,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
r = session.get(url=url, headers=headers)
# print(r.request.headers)
r.encoding = r.apparent_encoding
print(r.text)