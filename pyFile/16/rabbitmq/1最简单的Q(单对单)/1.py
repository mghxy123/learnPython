#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/8/1 20:28
import time
import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')
connection = pika.BlockingConnection(params)

with connection:
    # 建立通信
    channel = connection.channel()
    # 创建一个消息队列，queue命名为hello，如果不存早，消息将被droped
    channel.queue_declare(queue = queue_name)

    for i in range(40):
        channel.basic_publish(exchange='', #交换机为空，使用缺省exchange
                              routing_key=queue_name,
                              body='hello rabbitmq {}'.format(i))
        time.sleep(0.5)
    print(" send ok")