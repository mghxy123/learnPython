#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.命令分发器练习.py
# Author: HuXianyong
# Date  : 2019/5/26 20:46

class Dispatcher:
    def __init__(self):
        pass
    def reg(self,name,fn):
        setattr(self,name,fn)

    def run(self):
        while True:
            cmd = input('>>>'.strip())
            if cmd == 'quit':
                break
            getattr(self,cmd,lambda :print('Unkown Cmd {}'.format(cmd)))()

dis = Dispatcher()
dis.reg('ls',lambda :print('ls'))
# print(getattr(dis,'ls')())
dis.run()