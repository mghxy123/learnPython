#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : testredis.py
# Author: HuXianyong
# Date  : 2019/7/24 11:34


from celery import Celery
import time
app = Celery('mytask')

print(app)

@app.task(name='firstTask')
def add(x,y):
    time.sleep(3)
    print('start')

    ret  = x+y
    print('end')
    return ret

app.conf.broker_url = 'redis://192.168.18.181:6379/0'

app.conf.broker_transport_options = {'visibility_tomeout': 3600}
app.conf.result_backend = 'redis://192.168.18.181:6379/1'

app.conf.update(
    enable_utc=True,
    timezone='Asia/Shanghai',
)

if __name__ == '__main__':
    # add(1,2) #这样就是直接运行,是同步的
    add.delay(4,5) # 下发一个任务到broler的Queue里面去
    add.apply_async((10,20),countdown=3) #传值,3秒后运行
    # 这两个都是派发任务
    print('mian end ------------')