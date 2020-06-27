#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.装饰器的应用2.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/23 0023

def decorate(func):
    def inner(a,b):
        print('3 给函数添加一个求和的输出 {} {}'.format(a,b))
        print('4 我要打印func函数', func)
        result = func(a,b)
        print('6 我要打印add函数', add)
        print('7 我要打印func函数', func)
        print('8 我要打印inner函数', inner)
        return result
    print('2 我要打印decorate函数',decorate)
    return inner

@decorate
def add(a,b):
    print('5 我要打印add函数', add)
    return a+b
print('1 我应该是首个打印的')
print('9 这是函数输出的结果',add(1,2))

'''
由上面的输出，我们可以看得出来，装饰器的执行顺序是,213456789;
那是因为@装饰器函数，然后相当于把函数add传给了装饰器，从而变成了add = decorate(add)，这里调用了decorate函数把函数add传到了
装饰器内部，然后就打印了第二步，由于没有后续的调用，程序就在这里在inner处停滞等待被调用，而inner的实际指针已经指向了add函数
所以打我们打印func的时候输出的是add函数，并没有带locals，这里就不属于decorate的内部函数，而我们装饰器下面的add函数却已经成
为了inner的内部函数了，接下来的逻辑就是正常的函数执行逻辑了
#装饰器过程
@decorare+add --》decorate--》inner--》result=func 即 result=add--》
#调用过程
(新add)add(1,2)--》result(1,2)--》（被装饰函数add）add(1,2)--》输出结果
但是经过了装饰器这两个add只是同名而已
'''









# def add(a,b):
#     return a+b
#
# #装饰器用到了柯里化加上
#
# def decorate(func):
#     def inner(a,b):
#         print('我这里就只加了这个输出')
#         result = func(a,b)
#         return result
#     return inner
#
# cc = decorate(add)
# print(cc)
# print(add)
# # print(cc(1,2))
# add = decorate(add)
# print(add)

# print(add(1,2))

# positional
# arguments

# def func(fu):
#     print('1')
#     def inner():
#         print(2)
#         result = fu()
#         return result
#     print(3)
#     return inner
#
# print('i am number 1')
#
# @func
# def func3():
#     print('100')
#     return "hello"
#
# # print(func3)

