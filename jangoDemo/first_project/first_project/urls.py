"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from city import views
from django.urls import converters
from django.urls import include

def login(req):
    return HttpResponse("豆瓣登录")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urls.urls')),
    path('book/', views.book),
    path('book/<book_id>', views.book_id),
    path('book/author/', views.author_id),
    # publisher_id不是int 则返回404  默认使用str转换器
    path('book/publisher/<int:publisher_id>', views.publish),
    # 将url开头的url转到urls app中
    path('url1/', include('urls.urls', namespace='url1')),
    path('url2/', include(('urls.urls', 'url'), namespace='url2')),
]
