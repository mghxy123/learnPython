#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/5/27 10:18

# class A:
#     def __init__(self):
#         self.a = 'a'
#         print('A init')
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B init')
# #如果下面什么都没写的时候只会是输出 A init
# #因为在定义B类的时候给A类实例化了,就输出A init
# print('-'*30)
#
# print(B.x)
# print(B.x.a)
#
# b = B()
# print(b.x)
# print(b.x.a)


class A:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        print('A init')
    def __get__(self, instance, owner):# instance是owner的实例
        #由于我们第一次访问是直接类访问,所以是None ower是属主类B
        #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self

class B: #B是A的属主 也就是get方法中的
    x = A()
    def __init__(self):
        print('B init')

print('-'*30)
print(B.x) # 加上了__get__就变成了调用A类get的返回值了. 不加就是访问A对象 如果要访问A下面的属性,get方法需要返回实例self
print(B.x.a) #这是是分阶段完成的,是访问A类,然后再去访问A类下的属性.,
print()

b = B()
print(b.x)