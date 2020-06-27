#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 消费者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07

import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建

# with connection:
#     # 消费
#     # x = channel.basic_get(queue=queue_name)
#     # 这里使用的是ack机制,如果没有回ack,rabbitmq就会认为消息发送失败,继续保留消息
#     x = channel.basic_get(queue_name,True)
#     #这里加True就是确认发送ack 消息就会在rabbit中变为0,被消费了
#     # print(type(x),x)
#     method, properties, body = x
#     print(body)

def call_back(ch,method,properties,body):
    print(body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=call_back)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.

    # basic_get

