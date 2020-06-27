#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.正常的描述器.py
# Author: HuXianyong
# Date  : 2019/5/28 14:17

class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):# instance是owner的实例
        #由于我们第一次访问是直接类访问,所以是None ower是属主类B
        #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
        print('A__get__{} -- {} -- {}'.format(self,instance,owner))
        return self

class B:#B是A的属主 也就是get方法中的
    x = A()
    def __init__(self):
        print('B.init')
print('-'*20)
print(B.x) # 加上了__get__就变成了调用A类get的返回值了. 不加就是访问A对象 如果要访问A下面的属性,get方法需要返回实例self
print(B.x.a1) #抛异常AttributeError: 'NoneType' object has no attribute 'a1'
# print(B.x.a1) #这是是分阶段完成的,是访问A类,然后再去访问A类下的属性.,

print(''*20)
b = B()
print(b.x)
print(b.x.a1) #抛异常  AttributeError: 'NoneType' object has no attribute 'a1