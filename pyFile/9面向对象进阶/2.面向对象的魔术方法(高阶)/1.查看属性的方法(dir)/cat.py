#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : cat.py
# Author: HuXianyong
# Date  : 2019/5/25 10:19

import animal

from animal import Animal
class Cat(Animal):
    x = 'cat'
    y = 'abcd'

class Dog(Animal):
    def __dir__(self):
        return ['dog'] #必须要返回可迭代对象

print('直接使用dir方法来查看属性')
print('Cutrrent Module\'s name = {}'.format(dir()))#既是模块命名空间内的属性,,即当前cat.成员  cat可以调用的所有属性与方法
print('Animal Module\'s name = {}'.format(dir(animal))) #制定模块名词空间内的属性,既是animal所可以调用的所有属性,这和直接在animal内直接调用dir时的结果一般无二

print('\n使用字典来查看属性\n')
print('object\' __dir__ = {}'.format(sorted(object.__dict__.keys()))) #object的字典key
print('Animal\'s dir() = {}'.format(dir(Animal))) #类Animal的dir()属性
print('Cat\'s dir() = {}'.format(dir(Cat))) #类Cat的dir()属性
print('\n使用dir来查看实例的属性\n')
tom = Cat('tom')
print(sorted(dir(tom)))#实例tom的属性,cat类及所有祖先类的属性,
print(sorted(tom.__dir__())) #同上
print('\ndir()的等价近似如下,__dir__()字典包括了所有属性\n')
print(dir())
print(sorted(set(tom.__dict__.keys())|set(Cat.__dict__.keys())|set(Animal.__dict__.keys())|set(object.__dict__.keys())))
print(sorted(set((tom.__dict__.keys()|Cat.__dict__.keys()|Animal.__dict__.keys()|object.__dict__.keys()))))
print()
print('Dog\'s dir = {}'.format(dir(Dog)))
dog = Dog('hashiqi')

print(dir(dog))
print(dog.__dict__)

