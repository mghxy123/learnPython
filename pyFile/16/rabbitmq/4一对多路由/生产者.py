#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 生产者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07

import random
import pika

exchange_name='color'
colors = ('orange','black','green')


params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 声明一个交换价,直接把消息发送到交换机上,
channel.exchange_declare(exchange=exchange_name,
                      exchange_type = 'direct')


with connection:
    # 发消息

    for i in range(20):
        rk = random.choice(colors)
        msg = '{}-data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name,
                              routing_key=rk, # 从交换机上直接选择路由发送消息
                              body=msg)
        print(msg,'send ok')
    print(" [msg] Sent 'Hello World!'")