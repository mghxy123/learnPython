#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 生产者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07

import random
import pika

queue_name = 'hello'
exchange_name='products'
topics = ('phone.*','*.red')
products = ('phone','pc','tv')
colors = ('orange','black','red')


params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.exchange_declare(exchange=exchange_name,
                      exchange_type = 'topic')


with connection:
    # 发消息
    for i in range(20):
        rk = "{}.{}".format(
            random.choice(products),
            random.choice(colors)
        )
        msg = '{}-data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name, #交换机为空
                              routing_key=rk,
                              body=msg)
        print(msg)
    print(" [x] Sent 'Hello World!'")