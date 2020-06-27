#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.用类实现分发器.py
# Author: HuXianyong
# Date  : 2019/5/24 17:08
class A:
    def ls(self):
        print("ls")
    def pwd(self):
        print('pwd')

    def cd(self):
        print('pwd')

getattr(o,name,default=0)
setattr(o,name,value=0)