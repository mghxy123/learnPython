#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.py
# Author: HuXianyong
# Date  : 2019/6/28 10:24





class Meta(type):
    def __new__(cls, name,base, attrs:dict):
        print(cls)
        print(name)
        print(attrs)
        print()
        return super().__new__(cls,name+'123',base,attrs)

print('-'*39)

class A(Meta):  #这叫继承
    pass

print('~'*30)
class B(metaclass=Meta): #这叫做,修改元类
    pass

print('-'*30)
class C(B): # B继承时, 元类也一样继承下来
    pass

class D(Meta):pass # 这叫做继承元类 type这叫做元类

F = Meta('f', (), {}) # 这叫做元类实例化,也叫作修改源类,可以在这里添加修改元类的属性