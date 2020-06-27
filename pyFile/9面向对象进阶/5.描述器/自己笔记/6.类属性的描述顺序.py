#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.类属性的描述顺序.py
# Author: HuXianyong
# Date  : 2019/5/28 14:47

class A:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
    def __get__(self, instance, owner):
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self

    def __set__(self, instance, value):
        print('set------',self,instance,value)
        self.data = value #这里设置属性A的实例a的属性data,可以直接被调用
class B:
    x = A()
    def __init__(self):
        self.x = 'b.z' #新增自己的实例属性x

print('-'*20)
print(B.x)
print(B.x.a)
print('='*20)
b = B()
print(b.x)
print(b.x.a)
print(b.x.data)

print('+'*30)
b.x= 500
print(b.x)
print(b.__dict__)

#数据描述器,改变了属主属性访问的优先级
#当存在数据描述器的时候,不管类实例中的属性是否存在,有限访问数据描述器的属性.

B.x = 600 #如果类的属性x是描述器,那么不要使用这样的赋值语句
print(b.x)
print(b.__dict__)
#这里的输出结果是500 这里是实例的字典x是500,已经和描述器无关了,还有就是我们访问的是类实例属性,因而是500
