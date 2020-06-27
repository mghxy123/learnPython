#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 生产者.py
# Author: HuXianyong
# Date  : 2019/7/28 15:07


'''
交换机只是个路由通道,不会存消息,能存的是队列,所以需要先启动消费者,
因此这个订阅模式需要先有消费者,生产者才能生产数据,不然数据会消失,没有被存储到队列中,
这个订阅模式的queue是在消费端的,生产者只能生产发送不能存储,
如果生产者使用队列的随机名,会导致消费者不知道找谁去拿资源,所以只能把队列放在消费者端,
但是有指定队列的名称就可以放在生产这这端了,这样也方便
'''
# 生产者 连接rabbitmq --> 建立信道 --> 声明交换机 --> 在交换机信道上发送消息 ,之后就不管了
import pika

exchange_name = 'logs'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 交换机,路由器
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')# 我绑定到这个交换机上,交换机只是个路由通道,不会存消息,能存的是队列,所以需要先启动消费者


# # 队列声明
# channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建
# q = channel.queue_declare(queue='') # 不指定名称,queue名称会随机生成,使用q.method.queue 获取名称
# q = channel.queue_declare(queue='',exclusive=True) # exclusive 断开时会删除queue


with connection:
    # 发消息
    for i in range(20):
        msg = 'data-{:02}'.format(i)

        channel.basic_publish(exchange=exchange_name, # 指定交换机
                      routing_key='',# routing_key不写就是给谁都发
                      body=msg)# 通过这个交换机进行无差别发送
        print(msg)
    print(" [x] Sent 'Hello World!'")