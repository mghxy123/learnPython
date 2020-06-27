#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.多人聊天程序.py
# Author: HuXianyong
# Date  : 2019/7/7 1:30


import socket
import threading
import datetime
import logging
FROMAT = logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s [%(message)s]')

class  ChatServer:
    def __init__(self,ip='127.0.0.1',port=60000): # 启动服务
        self.sock = socket.socket()
        self.addr = (ip,port)
        self.clients = {} # 客户端

    def start(self): # 启动监听
        self.sock.bind(self.addr) #绑定
        self.sock.listen(5) # 监听
        # accept会阻塞主线程,所以开启一个新线程
        threading.Thread(target=self.accept).start() # 阻塞

    def accept(self): # 多人连接
        while True:
            sock,client = self.sock.accept()# 阻塞
            self.clients[client] = sock #添加到客户端字典
            # 准备接收数据,热诚是阻塞的,开始新的线程
            threading.Thread(target=self.recv,args=(sock,client)).start()

    def recv(self, sock:socket.socket, client): # 接受客户端数据
        while True:
            data = sock.recv(1024) # 阻塞到数据的到来
            msg = "{:%Y%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(),*client,data.decode())
            logging.info(msg)
            msg = msg.encode()
            for s in self.clients.values():
                s.send(msg)


    def stop(self): # 停止服务
        for s in self.clients.values():
            s.close()
        self.sock.close()
cs = ChatServer()
cs.start()