#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.hash方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022


# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return '<Person {} {}>'.format(self.name,self.age)
#
# # print(hash(1),hash(2),hash(5000000))#哈希之后的值,也是其本身
# # #整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# # print(1%4,2%4,3%4,4%4,5%4)#这就叫取模
#
#
# print(hash(Person('tom')))
#
# #得出一个哈希值,

###########################################################
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __hash__(self):
        return 1

    def __repr__(self):
        return '<Person {} {}>'.format(self.name,self.age)

# print(hash(1),hash(2),hash(5000000))#哈希之后的值,也是其本身
# #整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# print(1%4,2%4,3%4,4%4,5%4)#这就叫取模


print(hash(Person('tom')))
print(hash(Person('jerry')))

#得出一个哈希值,这样得到的哈希值都是1

###############################################################
# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return 'abc'
#
#     def __repr__(self):
#         return '<Person {} {}>'.format(self.name,self.age)
#
# # print(hash(1),hash(2),hash(5000000))#哈希之后的值,也是其本身
# # #整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# # print(1%4,2%4,3%4,4%4,5%4)#这就叫取模
#
#
# print(hash(Person('tom')))
# print(hash(Person('jerry')))
#
# #这样的哈希会报错

#######################################################
# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return 1
#
#     def __repr__(self):
#         return '<Person {} {}>'.format(self.name,self.age)
#
# # print(hash(1),hash(2),hash(5000000))#哈希之后的值,也是其本身
# # #整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# # print(1%4,2%4,3%4,4%4,5%4)#这就叫取模
#
#
# print(hash(Person('tom')))
# print(hash(Person('jerry')))
#
# p1 = Person('tom')
# p2 = Person('tom')
#
# print(p1 is p2)
# print(id(p1),id(p2))
# print(hash(p1),hash(p2))
# #得出一个哈希值,这样得到的哈希值都是1
#
# print({123,123})#内容相同,哈希值就想等,就可以去重 所以这里可议去重
# print({p1,p2}) #这里面没有去重,应为虽然他们的哈希值相同,但是内容却是不同的所以没有去重
# print(p1 == p2)

#######################################################
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __hash__(self):
        return 123

    def __repr__(self):
        return '<Person {} {}>'.format(self.name,self.age)

# print(hash(1),hash(2),hash(5000000))#哈希之后的值,也是其本身
# #整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# print(1%4,2%4,3%4,4%4,5%4)#这就叫取模




p1 = Person('tom')
p2 = Person('tom')

print(p1 is p2)
print(id(p1),id(p2))
print(hash(p1),hash(p2))
#得出一个哈希值,这样得到的哈希值都是1

print({123,123})#内容相同,哈希值就想等,就可以去重 所以这里可议去重
print({p1,p2}) #这里面没有去重,应为虽然他们的哈希值相同,但是内容却是不同的所以没有去重
print(p1 == p2)

#当我们把它们的内容也变成相等了就会去重了
#相等是内容相等,不是哈希相等