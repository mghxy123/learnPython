#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 11.访问控制（私有属性）.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#     def growup(self,i=1):
#         if 0< i <150: #控制逻辑
#             self.age +=1
#         print(self.age)
#
# p1 = Person('tom')
# p1.growup(20)#正常范围 在原有的age（18）上加1
# p1.age= 160 #这里指定了实例的age为160
# print(p1.age) #输出的就是上面的age等于160
# p1.growup(200)#i超出了正常范围 age（160）还是原来的age
# p1.growup(20)#正常范围 在原有的age（160）上加1

#######################################################
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
    def growup(self,i=1):
        if 0< self.age <150: #控制逻辑
            self.age +=i
        print(self.age)

p1 = Person('tom')
p1.growup() #正常的范围内，在原有的基础上+1 输出为19
p1.growup(20)#正常范围 在原有的age（18）+1基础上再上加20
p1.age= 160
p1.growup() #超出了范围，跳过逻辑判断输出age为160

