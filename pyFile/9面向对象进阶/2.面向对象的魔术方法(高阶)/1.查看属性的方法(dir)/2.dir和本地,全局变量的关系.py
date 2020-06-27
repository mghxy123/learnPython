#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.dir和本地,全局变量的关系.py
# Author: HuXianyong
# Date  : 2019/5/25 11:41

class Person:
    def show(self): #方法中
        a = 100
        t = int(a)
        print('show方法内属性dir--->',dir()) #
        print('show方法内本地变量--->',locals()) #
        print('show方法内全局变量--->',globals()) #

def test(a = 50,b = 100):
    c = 200
    print('test函数内属性dir--->', dir())  #
    print('test函数内本地变量--->', locals())  #
    print('test函数内全局变量--->', globals())  #
Person().show()
test()


print('当前文件属性dir---> {}'.format(dir()))  #
print('当前文件内本地变量--->', sorted(locals().keys()))  #
print('当前文件内全局变量--->', sorted(globals().keys()))  #