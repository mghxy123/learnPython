#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 消费者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07

import pika

queue_name = 'hello'
exchange_name='color'
colors = ('orange','black','green')
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.exchange_declare(exchange=exchange_name,
                         exchange_type = 'direct')


q1 = channel.queue_declare(queue='', exclusive=True) #exclusive 在断开时，会queue删除
q2 = channel.queue_declare(queue='', exclusive=True) #exclusive 在断开时，会queue删除
q1name = q1.method.queue
q2name = q2.method.queue
print(q1name,q2name)
channel.queue_bind(exchange=exchange_name, queue=q1name, routing_key=colors[0]) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name, queue=q2name, routing_key=colors[1]) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name, queue=q2name, routing_key=colors[2]) # 将队列和某一个交换机关联



def call_back(ch,method,properties,body):
    print(1,body)

def call_back1(ch,method,properties,body):
    print(2,body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=call_back)

    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=call_back1)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.

