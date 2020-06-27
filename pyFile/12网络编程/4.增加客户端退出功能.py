#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.增加客户端退出功能.py
# Author: HuXianyong
# Date  : 2019/7/7 10:38



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
        self.event = threading.Event()

    def start(self): # 启动监听
        self.sock.bind(self.addr) #绑定
        self.sock.listen(5) # 监听
        # accept会阻塞主线程,所以开启一个新线程
        threading.Thread(target=self.accept).start() # 阻塞

    def accept(self): # 多人连接
        while not self.event.is_set():
            sock,client = self.sock.accept()# 阻塞
            self.clients[client] = sock #添加到客户端字典
            # 准备接收数据,热诚是阻塞的,开始新的线程
            threading.Thread(target=self.recv,args=(sock,client)).start()

    def recv(self, sock:socket.socket, client): # 接受客户端数据
        while not self.event.is_set():
            data = sock.recv(1024) # 阻塞到数据的到来

            msg = data.decode().strip()
            # 客户端退出命令
            if msg == 'quit' or msg =='': # 主动断开得到空串
                self.clients.pop(client)
                sock.close()
                logging.info('{} quits'.format(client))
                break
            msg = "{:%Y%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client, data.decode())
            logging.info(msg)
            msg = msg.encode()
            for s in self.clients.values():
                s.send(msg)


    def stop(self): # 停止服务
        self.event.set()
        for s in self.clients.values():
            s.close()
        self.sock.close()
cs = ChatServer()
cs.start()

while True:
    cmd = input('>> ').strip()
    if cmd == 'quit':
        cs.stop()
        threading.Event().wait(3)
        break