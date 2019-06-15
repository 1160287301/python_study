from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 视图函数的返回结果必须是httpResponseBse对象或其子类对象

def book(request):
    return HttpResponse("图书首页")


def book_id(request, book_id):
    return HttpResponse(book_id)


def author_id(request):
    author_id = request.GET.get('id')
    return HttpResponse("作者的id是{}".format(author_id))


def publish(request, publisher_id):
    return HttpResponse("出版社id是{}".format(publisher_id))