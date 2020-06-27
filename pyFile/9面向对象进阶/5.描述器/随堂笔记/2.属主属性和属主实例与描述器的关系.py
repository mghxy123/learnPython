#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.py
# Author: HuXianyong
# Date  : 2019/5/27 10:44

class A:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        print('A init')
    def __get__(self, instance, owner):# instance是owner的实例
        #由于我们第一次访问是直接类访问,所以是None ower是属主类B
        #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
        print('get______',self.__class__.__name__,instance,owner)
        print(self.__dict__)
        return self

class B: #B是A的属主 也就是get方法中的
    x = A() #类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法.
    def __init__(self):
        self.y = A() #属主实例属性和描述器无关
        print('B init')

print('-'*30)
print(B.x) # 加上了__get__就变成了调用A类get的返回值了. 不加就是访问A对象 如果要访问A下面的属性,get方法需要返回实例self
print(B.x.a) #这是是分阶段完成的,是访问A类,然后再去访问A类下的属性.,
print()

b = B()
print(B.x.a)
print(b.x.a)
print(b.y.a)  #只与属主B的类属性相关,和B属主实例属性无关,y是类实例的属性.  实例属性不会调用描述其效果的

# 也可以说描述器和类实例无关.