#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : celery_use.py
# Author: HuXianyong
# Date  : 2019/7/26 11:12

from celery import Celery

import time

app = Celery('mytask')
app.conf.broker_url = 'redis://192.168.18.181:6379/0' # 0号库存执行任务队列
# 重复执行,直指问题解决
# 如果超过visibility_timeout,Celery会认为此次任务失败.
# 如果worker执行的时间过长或失败,会再次分配其他worker执行该任务,这样会照成重复执行,所以visibility_timeout可以调大一些.
# 注意,如果慢任务执行过长时,超过visibility_timeout依然会执行.

app.conf.broker_transport_options = {'visibility_timeout': 43200} # 12 hours
app.conf.result_backend = 'redis://192.168.18.181:6379/1' # 1号库 存储 结果

app.conf.update(
    enable_utc = True,
    timezone = 'Asia/Shanghai'
)

# 为celery添加任务
# @app.task # 没名字的,会取默认的名字
@app.task(name = 'firsttask')
# @app.task(ignore_result=True) #忽略执行的结果
def add(x, y):
    print('this is start~~~~~~~~~~~~~')
    time.sleep(4)
    res = x + y
    print('this is end~~~~~~~~~~')
    return res

if __name__ == '__main__':
    # 推荐价任务到中间人broker中
    print('in main Send task')
    add.delay(10, 20)
    add.apply_async((100,200), countdown=5) #5秒后启动
    print('end ~~~~~~~~~~~')

