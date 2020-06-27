#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.装饰类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

print('函数装饰类',end='\n\n')
#使用函数装饰一个类
def add_name(name,cls):
    cls.name = name

class Person: pass
print(Person.__dict__)
add_name('aa',Person)

print(Person.__dict__)
print(Person.name)

# 通过 查看类装饰前后的字典的对比，我们知道了类是否增加了属性
# 上面的意思其实就是 在类调用之前先增加了一个属性

#上面的函数起到的作用就好像我们下面写的这两行代码实现的功能一样
# class Person:pass
# Person.name = 'aa'

#然后我们把上面的函数变成装饰器来装饰我们的类
print('有参装饰器',end='\n\n')
def add_name():
    def inner(fn):
        fn.NAME = 'aa'
        return fn
    return inner

@add_name() #Person = add_name()(Person)
class Person: pass
print(Person.NAME)
print(type(Person))
print(type(Person()))
print(Person.__dict__.items())
print(Person().__dict__.items())

#上面是有参装饰器，这里在写个无参装饰器

print('无参装饰器',end='\n\n')
def add_name(fn):
    def wrapper():
        fn.NAME = 'newName'
        return fn
    return wrapper

@add_name  #    Person = add_name(Person)
class Person:
    a=1
print(Person().NAME)
print(type(Person))
print(type(Person()))
print(Person.__dict__.items())
print(Person().__dict__.items())