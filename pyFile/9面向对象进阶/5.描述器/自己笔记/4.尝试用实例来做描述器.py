#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.尝试用实例来做描述器.py
# Author: HuXianyong
# Date  : 2019/5/28 14:20


class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print('A__get__{} -- {} -- {}'.format(self,instance,owner))
        return self

class B:#B是A的属主 也就是get方法中的
    x = A()#类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法
    def __init__(self):
        print('B.init')
        self.b = A() #实例属性也指向一个A的实例
        # 属主实例属性和描述器无关

print('-'*20)
print(B.x)
print(B.x.a1)

print('='*20)
b = B()
print(b.x)
print(b.x.a1)
print('+'*30)
print('使用类实例来做描述器')
print(b.b) #并没有触发__get__
print(b.b.a1) ##只与属主B的类属性相关,和B属主实例属性无关,y是类实例的属性.  实例属性不会调用描述其效果的

