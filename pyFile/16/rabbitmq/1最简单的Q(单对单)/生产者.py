#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 生产者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07


import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建


with connection:
    # 发消息
    for i in range(10):
        msg = 'data-{}'.format(i)
        channel.basic_publish(exchange='', #交换机为空
                              routing_key='hello',
                              body=msg)
        print(" [x] Sent 'Hello World!'")