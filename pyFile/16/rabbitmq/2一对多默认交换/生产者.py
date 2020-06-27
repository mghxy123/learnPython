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



#队列
channel.queue_declare(queue=queue_name)
# # 队列声明
# channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建
# # q = channel.queue_declare(queue = '') #不指定Q名称,queue名称会随机产生
# # q = channle.queue_declare(queue = '',exclusice=True) # 在断开时,胡删除queue
# # q.method.queue
# # q
#
# # 将对列(多个队列)和某一个交换机关联,不关联不行,数据会发送到交换机,交换机才会发送到queue
# channel.queue_bind(exchange='logs',
#                    queue=result.method.queue)
# # 生产者 -->交换机 -->队列queue -->消费者
with connection:
    # 发消息
    for i in range(20):
        msg = 'data-{}'.format(i)

        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=msg)

    print(" [x] Sent 'Hello World!'")