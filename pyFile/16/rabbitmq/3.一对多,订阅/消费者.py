#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 消费者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07

# 消费者 连接rabbitmq --> 建立信道 --> 声明消息队列名称 --> 绑定交换机 --> 准备接收交换机消息 --> 开始接收
import pika

exchange_name = 'logs'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 交换机,路由器
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')# 广播扇出

# q = channel.queue_declare(queue='')  #不指定名称queue会随机生成 q.method.queue 作为名称
q1 = channel.queue_declare(queue='',exclusive=True) # exclusive 在断开时,会queue扇出
q2 = channel.queue_declare(queue='',exclusive=True) # exclusive 在断开时,会queue扇出

q1name = q1.method.queue
q2name = q2.method.queue
channel.queue_bind(exchange=exchange_name,queue=q1name) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name,queue=q2name) # 将队列和某一个交换机关联
def call_back(ch,method,properties,body):
    print("msg = {}".format(body))

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=call_back)

    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=call_back)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.

