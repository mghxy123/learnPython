#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.对实例的数据进行检验.py
# Author: HuXianyong
# Date  : 2019/5/28 16:19

# #写检查数据
# class Person:
#     def __init__(self,name:str,age:int):
#         params = ((name,str),(age,int))
#         if not self.checkdata(params):
#             raise TypeError()
#         self.name = name
#         self.age = age
#
#     def checkdata(self,params):
#         for param ,typ in params:
#             if not isinstance(param,typ):
#                 raise TypeError()
#         return True #这里的return为什么要写在外面?
#                     #那是因为,只有两个数据,或者所有的数据的类型都满足才不抛异常,
#                     #如果写在if同级的的话
# p = Person('tom',20)
# # p = Person('tom','20')
# #这里没有报错就显示正常

#########################################################
# #写检查数据
# class Person:
#     def __init__(self,name:str,age:int):
#         params = ((name,str),(age,int))
#         self.checkdata(params)
#         # if not self.checkdata(params):
#         #     raise TypeError()
#         self.name = name
#         self.age = age
#
#     def checkdata(self,params):
#         for param ,typ in params:
#             if not isinstance(param,typ):
#                 raise TypeError()
#         # return True #这里的return为什么要写在外面?
#                     #那是因为,只有两个数据,或者所有的数据的类型都满足才不抛异常,
#                     #如果写在if同级的的话
# p = Person('tom',20)
# # p = Person('tom','20')
# #这里没有报错就显示正常

# #################################################################
# class Person:
#     def __init__(self,name:str,age:int):
#         params = ((name,str),(age,int))
#         self.checkdata(params)
#         # if not self.checkdata(params):
#         #     raise TypeError()
#         self.name = name
#         self.age = age
#
#     def checkdata(self,params):
#         for param ,typ in params:
#             if not isinstance(param,typ):
#                 raise TypeError()
# p = Person('tom',20)
# # p = Person('tom','20')
# #这里没有报错就显示正常