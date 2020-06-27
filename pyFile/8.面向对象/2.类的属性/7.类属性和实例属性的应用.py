#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.类属性和实例属性的应用.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016


class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name= name
        self.age = age

tom = Person('Tom') #实例化、初始化
jerry = Person('Jerry',20)
Person.age = 30
print(1,Person.age,tom.age,jerry.age) #会输出什么？ 答案是30 18 20 应为实例没有属性的时候才会去类里面去寻找类的属性来使用
print(2,Person.height,tom.height,jerry.height) #这又会输出什么？ 170 170 170 应为实例中都没有这个属性， 需要到类里面去寻找
print()
Person.height=175
print(3,Person.height,tom.height,jerry.height) #是输出什么？ 175 175 175 应为实例调出来的结果都是累的属性

print()
tom.height +=10
print(4, Person.height,tom.height,jerry.height) #输出又会是什么？ 175 185 175 应为我们增加的是tom的height，与其他的无关

print()
Person.height +=15
print(5,Person.height,tom.height,jerry.height) # 输出结果为 190 185 190 应为tom的height已经是tom的私有属性了，儿jerry的依旧是Person的属性
print(5,'Person',Person.__dict__)
print(5,'tom',tom.__dict__)
print(5,'jerry',jerry.__dict__)
#通过查看字典我们就可以知道，tom的height已经成为了私有的属性， 它不再依赖Person了，而jerry还是依赖Person的

print()

Person.weight = 70
print(6,Person.weight,tom.weight,jerry.weight) #输出结果是70 70 70 应为这是给Person类新增了一个属性，而每个实例都可以调用类的属性
print()
print(7,tom.__dict__['height']) #可以吗 这个可以的，应为我们在上面查看tom的字典的时候height已存在在tom的属性之内了
print(8,tom.__dict__['weight']) #可以吗 这个不可以，应为这个是类的属性，不存在于tom的属性里面。