#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : pika1.py
# Author: HuXianyong
# Date  : 2019/7/28 14:51
import pika
from pika.credentials import PlainCredentials

queue_name = 'hello'
cred = PlainCredentials('hxy','hxy')

params = pika.ConnectionParameters(
    '192.168.18.181', #broker，port
    5672, #port
    'test', #virtual host
    credentials=cred # user，password
)
# params = pika.ConnectionParameters('192.168.18.181')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# 队列
channel.queue_declare(queue = queue_name)

with connection:
    # 发消息
    msg = 'Hello World!'
    channel.basic_publish(exchange='', #交换机为空
                          routing_key='hello',
                          body=msg)
    print(" [x] Sent 'Hello World!'")