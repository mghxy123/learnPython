#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.lambda函数.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/5 0005

#这样输出的是一个定义函数lambda 和我们def定义的函数一样,没有被调用
# print(lambda x,y:x+y)
#
# #这样是调用了函数,输出的结果是9
# print((lambda x,y:x+y)(4,5))

#lambda 冒号前面接受的是参数,冒号后面接受的是表达式,然后返回结果
############################################################
# def add(x,y):
#     return x+y
# f1 = add(4,5)
#
# f2 = lambda x,y:x+y
# f3=f2(4,5)
# #这两个函数其实定义和形式上是一样的
# print(f1)
# print(f3)

#############################################################
# print([lambda x:x+1][0](1))
# #这句的意思是lambda函数传给列表,然后列表的第零个元素加1
# #可以等价为:
# aa = [lambda x:x+1]
# print(aa)
# print(aa[0](1))

###########################################################
# #无参lambda
# print((lambda :100)())#这样就可以直接调用了
#
# #无返回值lambda,只能成none不能为空
# print((lambda x:None)(1))

#lambda函数比较列表
# l1 = [1,'a','1',2]
# def fn(x): #判断传入的字符是否是字符串,是就返回转化的数字,不是就原封不动的返回
#     if isinstance(x,str):
#         return ord(x)
#     else:
#         return x
#
# l2 = sorted(l1,key=fn)
# print(l2)
#
# #用lambda表达式来做可以写成
# l3 = sorted(l1,key=lambda x:ord(x) if isinstance(x,str) else x)
# print(l3)
#
# #这样的lambda表达式就可以实现函数fn的功能了

#####################################################################################
#返回常量的函数
print((lambda :0)())

#加法匿名函数,带缺省值
print((lambda x,y=3:x+y)(3))
print((lambda x,y=3:x+y)(3,5))

#keyword-noly参数
print((lambda x,*,y=30:x+y)(5))
print((lambda x,*,y=30:x+y)(5,y=10))

#可变参数
print((lambda *args:[*args])(*range(10)))#传入一个元组,返回一个列表
print((lambda *args:[i for i in args])(*range(10)))
print((lambda *args:(x for x in args))(*range(10)))#这是一个生成器表达式,返回一个惰性的对象
print((lambda *args:[x+1 for x in args])(*range(10)))
print((lambda *args:{x%2 for x in args})(*range(10)))

for i in (lambda *args:(x for x in args))(*range(10)):
    print(i)

#高阶函数

print([x for x in (lambda *args:map(lambda x:(x+1,args),args))(*range(5))])