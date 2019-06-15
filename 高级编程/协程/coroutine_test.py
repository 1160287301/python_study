# -*- coding:utf-8 -*-


# def get_html(url):
#     pass
#
#
# def parse_url(html):
#     pass
#
#
# def get_url(url):
#     # do someting 1
#     html = get_html(url)
#     # # parse html
#     # urls = parse_url(html)

def gen_fun():
    # 1.可以产出值 2.可以接受值(调用方传递过来的值)
    html = yield "url"
    yield 1
    yield 2
    yield 3
    return 4

if __name__ == '__main__':
    gen = gen_fun()
    # 启动生成器的方式有两种, next(), send
    # url = next(gen)
    # 在调用send发送非none值之前,我们必须启动一次生成器,方式有两种 1.gen.send(none) 2.next(gen)
    url = next(gen)
    html = "body"
    # send方法可以传递值进入生成器内部,同时还可以重启生成器执行返回(next())
    print(gen.send(html))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
