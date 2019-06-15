# -*- coding:utf-8 -*-
from django.urls import path
from . import views
# 避免url名称重复
app_name = 'url'

urlpatterns = [
    path('', views.url_include),
    path('sigin/', views.login, name='login'),
    path('index/', views.index, name='index'),
]