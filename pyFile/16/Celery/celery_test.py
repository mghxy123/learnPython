#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : celery_test.py
# Author: HuXianyong
# Date  : 2019/7/26 10:43


from celery import Celery

app = Celery('mytask')
print(app)

@app.task
def add(x, y):
    ret = x+y
    return ret

print(add.name)
print(add)
print(app.tasks)
print(app.conf)
print('-'*30)
print(*list(app.conf.items()),sep='\n')

