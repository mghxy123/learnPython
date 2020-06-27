#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 17.对象的销毁.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

import time

class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
    def __del__(self):
        print('delete {}'.format(self.name))

def test():
    tom = Person('tom')
    tom.__del__() #手动调用
    tom.__del__()
    tom.__del__()
    tom.__del__()

    print('======start======')

    tom2 = tom
    tom3 = tom2
    print(1,'del')
    del tom
    time.sleep(3)

    print(2,'del')

    del tom2
    time.sleep(3)
    print('~'*10)

    del tom3 #注释一下看看效果
    time.sleep(3)
    print('=========end')
test()