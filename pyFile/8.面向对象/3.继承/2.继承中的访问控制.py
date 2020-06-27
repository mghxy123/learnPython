#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.继承的定义.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

# class 子类名(基类1[,基类2..]):
#     语句块

# class A:
#     pass
# #等价于
# class A(object):
#     pass

class Animal:
    __COUNT = 100
    HEIGHT = 0

    def __init__(self,age,weight,height):
        self.__COUNT += 1
        self.age = age
        self.__weight = weight
        self.HEIGHT = height

    def eat(self):
        print('{} eat '.format(self.__class__.__name__))

    def __getweight(self):
        print(self.__weight)

    @classmethod
    def showcount1(cls):#静态方法传入的就是类，会直接调用类方法
        print(cls)
        print(cls.__dict__)
        # print(Animal.__dict__)
        # print(Animal._Animal__COUNT)
        print(cls.__COUNT) #是多少？为什么？

    @classmethod
    def __showcount2(cls):
        print(cls.__COUNT)

    def showcount3(self):
        print(self.__COUNT) #是多少？为什么

class Cat(Animal):
    NAME = 'CAT'
    __COUNT = 200

# c = Cat()#参数错误
c= Cat(3,5,15)
c.eat() #eat方法里面传入的self是Cat，所以会输出Cat eat
print(c.HEIGHT) #这里借用了父类的初始化，初始化输入的height为15，所以这里输出的是15
########################################################################
# print(c.__COUNT) 可以访问吗？ #这里的__COUNT不能访问，应为私有属性，已经改名了，不管是子类的还是父类的都已经不再是源来的名字了
# 如果想要访问Cat的COUNT 可以使用_Cat__COUNT来进行访问，如果想访问Animal的可以使用_Animal__COUNT来访问,如下所示：
# print(c._Cat__COUNT) #200
# print(c._Animal__COUNT) #101
########################################################################
# c.__getweight()# 可对访问吗？假如不能，怎么样才能访问这个方法？ #私有属性和私有方法一般，改名了，无法使用这样访问
#可以使用下划线+类名+双下划线+方法名来访问。如下所示：
print(c._Animal__getweight())
########################################################################
c.showcount1() #会输出多少?
#输出结果如下：
'''
Cat()
Cat().__dict__
Cat()._Animal__COUNT #100 应为它直接调用的是Animal的私有属性COUNT,而不是初始化之后的COUNT我们可以直接查看Animal的字典就可以看出来了
#cls是类的调用，self是实例的调用，类的调用不经过初始化，实例的调用要是用初始化
#print(Animal._Animal__COUNT)
'''

########################################################################
# c.__showcount2() # 可以访问吗？如何才能访问?私有属性和私有方法一般，改名了，无法使用这样访问
c.showcount3() #会输出什么结果？ 应为这个是Animal的私有属性，只能在Animal里面被调用,且调用的永远都是Animal的私有属性，
# 故而输出的结果是100，这个和上面的count1的分析结果一样，但是这里使用的是self.然而self是实例化之后的结果，
# 实例化之后的COUNT就变成了101了 所以输出的还是101
########################################################################

########################################################################
print(c._Cat__COUNT) #能否访问？是多少？可以，这里调用的是cat的count所以是200
print(c._Animal__COUNT) #能否访问？是多少？ 可以，这里调用的是Animal的count，c是实例化之后的，所以count是101
print(c.__dict__)
print(c.NAME)
#
print('{}'.format(Animal.__dict__))
print('{}'.format(Cat.__dict__))
print(c.__dict__)
print(c.__class__.mro())