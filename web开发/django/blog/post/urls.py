#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 2019/7/18 10:49


from django.conf.urls import url
from .views import getpost,PostView


urlpatterns = [

    # View类调用as_view之后等价于一个视图函数,可以被装饰
    # 装饰器函数返回调用函数
    url(r'^$',PostView.as_view()), # /posts/ 视图类PostView
    url(r'^(\d+)$', getpost),
]




