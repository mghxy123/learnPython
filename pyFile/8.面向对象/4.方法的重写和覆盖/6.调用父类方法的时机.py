#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.调用父类方法的时机.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


# 实例 1
'''
说明，，这里的类B在实例化的时候，由于其本身并没有初始化方法，所以这里调用了它父类
的初始化方法，也因此继承了它父类的属性a1、a2
'''
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('init in A')
#
# class B(A):
#     pass
#
# b = B()
# print(b.__dict__)

#########################################################
# 实例2
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('init in A')
#
# class B(A):
#     def __init__(self):
#         self.b1 = 'b1'
#         print('init in B')
#
# b = B()
# print(b.__dict__)
#
# '''
# B实例一旦定义了初始化`__init__`方法,就不会自动调用父类的初始化`__init__`方法，应为B类的`__init__`覆盖了A类的`__init__`，需要手动的去调用。
# '''
#########################################################
# # 实例3
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('init in A')
#
# class B(A):
#     def __init__(self):
#         self.b1 = 'b1'
#         print('init in B')
#         A.__init__(self)
#
# b = B()
# print(b.__dict__) #注意__a2
#########################################################
# # 实例4 如何正确的初始化
# class Animal:
#     def __init__(self,age):
#         print('init in Animal')
#         self.age = age
#     def show(self):
#         print(self.age)
#
# class Cat(Animal):
#     def __init__(self,age,weight):
#         print('init in Cat')
#         self.age = age + 1
#         self.weight = weight
#
# c = Cat(10,5)
# c.show() #会打印什么？
#########################################################
# # 实例5如何正确的初始化
# class Animal:
#     def __init__(self,age):
#         print('init in Animal')
#         self.age = age
#     def show(self):
#         print(self.age)
#
# class Cat(Animal):
#     def __init__(self,age,weight):
#         super().__init__(age)
#         print('init in Cat')
#         self.age = age + 1
#         self.weight = weight
#         # super().__init__(age) #在前面调用和在后面调用有何区别？
#
# c = Cat(10,5)
# c.show() #会打印什么？


######################################################################
#实例六 私有属性与重载顺序
class Animal:
    def __init__(self,age):
        print('init in Animal')
        self.__age = age
    def show(self):
        print(self.__age)

class Cat(Animal):
    def __init__(self,age,weight):
        super().__init__(age)
        print('init in Cat')
        self.__age = age + 1
        self.__weight = weight
        # super().__init__(age) #在前面调用和在后面调用有何区别？

c = Cat(10,5)
c.show() #会打印什么？
print(c.__dict__)
print(Animal(6).__dict__)
