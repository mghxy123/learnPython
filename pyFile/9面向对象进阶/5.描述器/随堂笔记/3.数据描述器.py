#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.数据描述器.py
# Author: HuXianyong
# Date  : 2019/5/27 11:07
# class A:
#     def __init__(self):
#         self.a = 'a'
#         self.b = 'b'
#     def __get__(self, instance, owner):# instance是owner的实例
#         #由于我们第一次访问是直接类访问,所以是None ower是属主类B
#         #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
#         print('get______',self.__class__.__name__,instance,owner)
#         print(self.__dict__)
#         return self
#
#     def __set__(self, instance, value):
#         print('set------',instance,value)
#         instance.__dict__['x'] = value
#
#
# class B: #B是A的属主 也就是get方法中的  A类叫做描述器
#     x = A() #类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法.
#     def __init__(self):
#         self.x = 'b.z' #
#
# print('-'*30)
# print(B.x) # 加上了__get__就变成了调用A类get的返回值了. 不加就是访问A对象 如果要访问A下面的属性,get方法需要返回实例self
# print(B.x.a) #这是是分阶段完成的,是访问A类,然后再去访问A类下的属性.,
# print()
#
# b = B()
# print(111,b.x)
# print(b.__dict__)#set 属性为pass b实例的字典为空
#
## 上面的数据描述器,我们访问b实例的字典是空的,虽然我们也能
# #数据描述器,改变了属主属性访问的优先级,数据描述器的优先级更高,
## 属性查找的优先级,数据描述器>类实例属性>非数据描述器



# class A:
#     def __init__(self):
#         self.a = 'a'
#         self.b = 'b'
#     def __get__(self, instance, owner):# instance是owner的实例
#         #由于我们第一次访问是直接类访问,所以是None ower是属主类B
#         #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
#         print('get______',self.__class__.__name__,instance,owner)
#         print(self.__dict__)
#         return self
#
#     def __set__(self, instance, value):
#         print('set------',instance,value)
#         instance.__dict__['x'] = value
#         # self.data = value
#
# class B: #B是A的属主 也就是get方法中的  A类叫做描述器
#     x = A() #类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法.
#     def __init__(self):
#         self.x = 'b.z' #
#
# print('-'*30)
# print(B.x) # 加上了__get__就变成了调用A类get的返回值了. 不加就是访问A对象 如果要访问A下面的属性,get方法需要返回实例self
# print(B.x.a) #这是是分阶段完成的,是访问A类,然后再去访问A类下的属性.,
# print()
#
# b = B()
# print(111,b.x)
# print(b.__dict__)#set 属性为pass b实例的字典为空
# # print(b.x.data)
#
# b.x= 500
# print(b.x)
# print(b.__dict__)
#
# #数据描述器,改变了属主属性访问的优先级
# #当存在数据描述器的时候,不管类实例中的属性是否存在,有限访问数据描述器的属性.
#
# B.x = 600 #如果类的属性x是描述器,那么不要使用这样的赋值语句
# print(b.x)
# print(b.__dict__)
# #这里的输出结果是500 这里是实例的字典x是500,已经和描述器无关了,还有就是我们访问的是类实例属性,因而是500


class A:
    def __init__(self):
        # self.a = 'a'
        self.b = 'b'
    def __get__(self, instance, owner):# instance是owner的实例
        #由于我们第一次访问是直接类访问,所以是None ower是属主类B
        #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self

    # def __set__(self, instance, value):
    #     print('set------',self,instance,value)
    #     # instance.__dict__['x'] = value
    #     # self.data = value
    #     # setattr(instance,'x',value)
    #     # if instance:
    #     #     raise AttributeError('cat\'t set attribute') #如果这样设置了,就和property属性装饰器时候一样的
class B: #B是A的属主 也就是get方法中的  A类叫做描述器
    x = A() #类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法.
    def __init__(self):
        self.x = 'b.z' #

b = B()
print(b.x)
b.x= 100
print()

#描述器可以阻止用户修改类实例的属性,.