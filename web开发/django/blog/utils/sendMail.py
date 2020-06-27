#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : testMail.py
# Author: HuXianyong
# Date  : 2019/7/26 14:24

from __future__ import absolute_import,unicode_literals

from datetime import datetime

from blog.celery import app

from django.core.mail import send_mail
from blog import  settings

# send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
#           settings.EMAIL_HOST_USER, fail_silently=False)

# def sendMail():
#     send_mail(
#         '测试专用',
#         'test',
#         'mghxy123@163.com',
#         ['mghxy123@163.com','mghuxy123@163.com'],
#         fail_silently=False,
#         html_message="<h1>这是链接<a href='www.baidu.com'>打开百度</a></h1>"
#     )
#
# sendMail()

@app.task(name = 'sendmail')
def sendMail():
    send_mail(
        '测试专用',
        'test',
        settings.EMAIL_HOST_USER,
        ["mghxy123@163.com"],
        fail_silently=False,
        html_message="<h1>这是一封测试邮件,"
                     "<br>时间是{:%Y%m%d-%H:%M:%S}"
                     "<hr>这是链接"
                     "<a href='{}'><hr>打开百度</a>"
                     "</h1>".format(datetime.now(),'https://cn.bing.com')
    )
# sendMail()