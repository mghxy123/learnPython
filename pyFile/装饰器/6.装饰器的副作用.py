#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.装饰器的副作用.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/23 0023

'''
装饰器的副作用就是为了解决用户在调用被装饰函数的时候
出现的属性都是装饰器函数的属性，比如函数名，除了结果是
和被装饰函数相同的，其余的都是装饰器的
'''

#一、原函数
# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     return wrapper
#
# @decorate
# def add(a,b):
#     return a+b
# print(add(6,7))
#############################################################################
# #二、查看被装饰函数的属性
# def decorate(func):
#     def wrapper(*args,**kwargs):
#         '''
#         this is wrapper function
#         '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''
#     this is add function
#     '''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))

'''
这样输出的结果为
before
this function is add wrapper 
        this is wrapper function
        
end  13
13
'''

'''
从上面的装饰器中我们是可以得出add函数的结果，
但是我们只要把add函数的函数名输出出来，
就会发现，add函数已经不是我们定义的函数了，
为了尽可能的不被使用这发觉，这个add函数已经不是他之前调用的add
函数，我们就需要对装饰器函数进行伪装
'''
#############################################################################
#三、修改装饰器函数属性
'''
解决用户发现这个add函数已经变成装饰器的wrapper函数，
所以我们需要对wrapper函数的属性做修改
我们在原有函数上增加了两行，来修改函数的属性
    wrapper.__name__ = add.__name__
    wrapper.__doc__ = add.__doc__
'''

# def decorate(func):
#     def wrapper(*args,**kwargs):
#         '''this is wrapper function'''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''this is add function'''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))
'''
我们修改了add函数的属性之后我们再来看看这样的输出结果
before
this function is add add 
    this is add function
    
end  13
13

输出的结果很明显已经达到了我们需要结果

'''
#############################################################################
#四、对现有的装饰器做修改，把修改属性的两行组成一个函数
'''
为什么要把属性修改的两行房子函数里面？
应为修改的可能不只是一两个函数，所以放在一个函数里面
方便查看与修改
'''

def decorate(func):
    def changeAttribute(source,destination):#把源函数属性赋值给目标函数属性
        destination.__name__ = source.__name__
        destination.__doc__ = source.__doc__
    def wrapper(*args,**kwargs):
        ''' this is wrapper function '''
        print('before')
        result = func(*args,**kwargs)
        print('end ',result)
        return result
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    #这里改成调用函数
    changeAttribute(func,wrapper)
    return wrapper

@decorate
def add(a,b):
    '''this is add function'''
    print('this function is add',add.__name__,add.__doc__)
    return a+b

print(add(6,7))

'''
输出的结果为：
before
this function is add add this is add function
end  13
13

这样的结果也很理想了
'''
