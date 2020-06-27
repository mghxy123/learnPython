"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from datetime import datetime

from django.conf.urls import url,include
from django.contrib import admin

from django.http import HttpRequest,HttpResponse,JsonResponse

#
# class A:
#     def __init__(self):
#         self.a = 100
# def index(request:HttpRequest):
#     # d = {
#     #     "method": request.method,
#     #     "pathinfo": request.path_info,
#     #     "path": request.path,
#     #     "qs": request.GET
#     # }
#     #
#     # # return HttpResponse('this test',status=222) # status状态码
#     # res = JsonResponse(d)
#
#     # t = get_template('index.html')
#     # context = t.render({},request)
#     #
#     # res = HttpResponse(context)
#     # return res
#
#     content = {
#         'a':100,
#         'b':'abc',
#         'c':list(range(9)),
#         'd':A(),
#         'e':{'a':200,'c':500},
#         'date':datetime.now()
#
#     }
#     res = render(request,'index.html',content)
#     return res
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/',include('post.urls')),
    url(r'^users/',include('user.urls')),
    url(r'^$',include('user.urls')),
]
