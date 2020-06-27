#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 11.完整的客户端.py
# Author: HuXianyong
# Date  : 2019/7/7 23:19



import socket
import threading
import datetime
import logging
FROMAT = '%(asctime)s %(threadName)s %(name)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FROMAT)

class ChatServer:
    def __init__(self,ip='127.0.0.1',port=60000):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.addr)
        self.send('I\'m ready')
        # 准备接收数据,recv是阻塞的,开启新的线程
        threading.Thread(target=self.recv,name='recv').start()

    def recv(self): #接收客户端的数据
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as  e:
                logging.error(e)
                break
            msg = "{:%Y%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *self.addr, data.strip())
            logging.info(msg)

    def send(self,msg:str):
        data = "{}\n".format(msg.strip()).encode() # 服务端需要一个换行符
        self.sock.send(data)

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info('Client stops')

def main():
    cc = ChatServer()
    cc.start()

    while True:
        cmd = input('>> ').strip()
        if cmd == 'quit':
            cc.stop()
            break
        cc.send(cmd)

if __name__ == '__main__':
    main()