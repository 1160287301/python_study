from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
# Create your views here.



def url_include(request):
    return HttpResponse("已转到urls的app中")


def index(request):
    name = request.GET.get('name')
    current_nameplace = request.resolver_match.namespace
    if not name:
        # return redirect('/login')
        # return redirect(reverse('url:login'))
        return redirect(reverse('{}:login'.format(current_nameplace)))
    return HttpResponse('{}前台首页'.format(current_nameplace))


def login(reuqest):
    return HttpResponse('前台登录页面')