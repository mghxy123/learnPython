#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.makefile练习.py
# Author: HuXianyong
# Date  : 2019/7/7 21:44

import socket
import threading
import datetime
import logging
FROMAT = logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(message)s')

class  ChatServer:
    def __init__(self,ip='127.0.0.1',port=60000): # 启动服务
        self.sock = socket.socket()
        self.addr = (ip,port)
        self.clients = {} # 客户端
        self.event = threading.Event()
        self.lock = threading.Lock()


    def start(self): # 启动监听
        self.sock.bind(self.addr) #绑定
        self.sock.listen(5) # 监听
        # accept会阻塞主线程,所以开启一个新线程
        threading.Thread(target=self.accept).start() # 阻塞

    def accept(self): # 多人连接
        while not self.event.is_set():
            sock,client = self.sock.accept()# 阻塞
            f = sock.makefile('rw') # 支持读写
            with self.lock:
                self.clients[client] = f,sock #添加到客户端字典
            # 准备接收数据,热诚是阻塞的,开始新的线程
            threading.Thread(target=self.recv,args=(f,client)).start()

    def recv(self, f, client): # 接受客户端数据
        while not self.event.is_set():
            data = f.readline() # 阻塞到数据的到来

            msg = data.strip()
            print(msg,'+++++++++++++++++++')
            # 客户端退出命令
            if msg == 'quit' or msg =='': # 主动断开得到空串
                with self.lock:
                    _,sock = self.clients.pop(client)
                    f.close()
                    sock.close()
                logging.info('{} quits'.format(client))
                break
            msg = "{:%Y%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client, data)
            logging.info(msg)
            with self.lock:
                # msg = msg.encode()
                for ff,_ in self.clients.values():
                    ff.write(msg)
                    ff.flush()

    def stop(self): # 停止服务
        self.event.set()
        with self.lock:
            for f,s in self.clients.values():
                s.close()
                f.close()
        self.sock.close()
cs = ChatServer()
cs.start()

while True:
    cmd = input('>> ').strip()
    if cmd == 'quit':
        cs.stop()
        threading.Event().wait(3)
        break
    logging.info(threading.enumerate()) # 用来观察断开后线程的变化
    logging.info(cs.clients)
