#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 2019/7/15 15:46

from django.conf.urls import url
from .views import reg,index,test,select,login,update,test1


urlpatterns = [
    url(r'^reg$',reg),
    url(r'^$',index),
    url(r'^test$',test),
    url(r'^test1$', test1),
    url(r'^login$', login),
    url(r'^select$',select),
    url(r'^update$',update),

]

