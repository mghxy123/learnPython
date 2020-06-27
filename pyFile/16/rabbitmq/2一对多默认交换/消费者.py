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

def call_back(ch,method,properties,body):
    print(1,body)
def call_back1(ch,method,properties,body):
    print(2,body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=call_back)


    ## 这里模拟一生产者对二个消费者的情况,可以是一个信道对应连个consume
    ## 也可以是开启两个进程两个信道对应两个consume

    # channel.basic_consume(queue=queue_name,
    #                       auto_ack=True,
    #                       on_message_callback=call_back1)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.
