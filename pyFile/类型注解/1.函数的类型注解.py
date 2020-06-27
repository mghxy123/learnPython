#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 类型注解.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025

'''

参数注解,由3.5引入
对函数的参数进行类型注解
对函数的返回值进行类型注解,
指对函数参数做一个辅助的说明,并不对函数参数先进性类型检查
提供给笛梵方的工具,做代码分析,发现隐藏的bug
函数注解的信息.保存在__annotation__属性中

我们通常在定义一个函数的时候,都会给函数做一些注释,方便代码的理解
但是有的时候我们懒得写这样的注释,但是有必须要用的时候,可以用类型注解
参数注解是在3.5之后新加的功能,类型注解可以写部分,也可以全写
'''
#
# #1.普通的函数
# def add(x,y):
#     return x + y
#
# print(add(2,4))
# print(add('b','a'))
# print(add([2],[4]))
#
#
# print('*'*60)
# #类型注解的函数
# def add1(x:int,y:int):
#     return x + y
#
# print(add1(2,4))
# print(add1('b','a'))
# print(add1([2],[4]))
# #这样虽然函数调用没有报错,但是不影响函数的运行结果,
# #这样的不友好显示,可以忽略

# #2.参数注解我们也可以作用在函数调用上面
# def add1(x:int,y:str=6) -> int: #定义函数add1的返回值的类型注释为int
#     '''
#     :param x:
#     :param y:
#     :return: str
#     '''
#     return x + y
#
# print(add1(2))
# print(add1(2,4))
#
# l:list = add1([4],[5])
# l.append('6')
# print(l)
# print(add1.__annotations__) #annotation 查看字典的注解 annotation(注释)

#######################################################################################
# #3.关于函数类型注解的判断
# '''
#     在类型的注解的时候,如果我们只是提示,不做限制,
#     那么我们的注解也就没用了,注解关乎到我们下面函数
#     的使用,所以我们需要加以判断,才能使用
# '''
# def add1(x:int,y:str=6) -> int: #定义函数add1的返回值的类型注释为int
#     # if not (x is int and y is str):
#     if not (isinstance(x,int) and isinstance(y,str)):
#
#         return 'you  input is wrong'
#     return x + y
#
# print(add1(2))
# print(add1(2,4))
#
# print(add1.__annotations__) #annotation 查看字典的注解 annotation(注释)

########################################################################################
#4.关于函数类型注解的判断的装饰器
'''
    但是这样的判断不可能只有一个地方在使用,
    我们不可能都要写一遍,所以就要用到了装饰器
'''
import inspect #导入检查的模块

def check(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(add1)
        parameters = sig.parameters
        print(parameters) #OrderedDict([('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
        ret =  fn(*args,**kwargs)
        return ret
    return wrapper
@check#add1 = check(add1)
def add1(x:int,y:str=6) -> int: #定义函数add1的返回值的类型注释为int
    if not (isinstance(x,int) and isinstance(y,str)):
        return 'you  input is wrong'
    return x + y

print(add1(2,4))
print(add1.__annotations__) #annotation 查看字典的注解 annotation(注释)__annotations__

def fib(n):
    yield from range(10)
print(inspect.isgenerator(fib)) #检查函数是否是生成器
print(inspect.isgeneratorfunction(add1)) #检查函数是否是生成函数
print(inspect.signature(fib)) #检查函数的签名
print(inspect.signature(add1)) #检查函数的签名
