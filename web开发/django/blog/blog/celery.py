#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : celery.py
# Author: HuXianyong
# Date  : 2019/7/26 17:01

from __future__ import absolute_import, unicode_literals
from celery import  Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings') # 必须修改文件名
app = Celery('blog') # 可以修改
app.config_from_object('django.conf:settings',namespace='CELERY')


app.autodiscover_tasks()

app.conf.broker_url = 'redis://192.168.18.181:6379/0'
# 如果超过visibility_timeout,celery会认为任务失败
# 如果是将过长,任务没有完成,会重新分配其他worker执行该任务,这样会重复执行,visibility_timeout这个值尽可能设置的大一些
# 注意,如果任务执行的长超过visibility_timeout依然会多执行.
app.conf.broker_transport_options = {'visibility_timeout': 3600}
app.conf.result_backend = 'redis://192.168.18.181:6379/1'

app.conf.update(
    enable_utc = True,
    timezone = 'Asia/Shanghai'
)
