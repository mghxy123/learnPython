#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.带装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/23 0023


'''
我们通常用的装饰器都是无参装饰器，例如@decorate
但有时无参装饰器无法满足我们的需求的时候就需要用到带参装饰器了，例如@decorate(fn)

'''

'''
以我们之前装饰器的副作用的例子来讲解带参装饰器
'''
#一、原函数为：
# def decorate(func):
#     def changeAttribute(source,destination):#把源函数属性赋值给目标函数属性
#         destination.__name__ = source.__name__
#         destination.__doc__ = source.__doc__
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     # wrapper.__name__ = func.__name__
#     # wrapper.__doc__ = func.__doc__
#     #这里改成调用函数
#     changeAttribute(func,wrapper)
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''this is add function'''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))
#############################################################################
#二、提出修改属性的函数
'''
如果我们有多个装饰器，都需要修改被装饰函数的属性，这样一来我们每个装饰器都需要去
添加修改被装饰函数的属性，这样就很繁琐，所以我们可以把修改装饰器属性的函数提出来
单独的使用
'''

# def changeAttribute(source, destination):  # 把源函数属性赋值给目标函数属性
#     destination.__name__ = source.__name__
#     destination.__doc__ = source.__doc__
# def decorate(func):
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     changeAttribute(func,wrapper)
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''this is add function'''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))
##############################################################################
#三、把修改属性的函数柯里化，
# def changeAttribute(source):
#     def _copy(destination):  # 把源函数属性赋值给目标函数属性
#         print('***',destination.__name__)
#         destination.__name__ = source.__name__
#         destination.__doc__ = source.__doc__
#         print('***',destination.__name__)
#         # return destination #这里为什么要返回destination？
#         # #那是因为
#     return _copy
# def decorate(func):
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     changeAttribute(func)(wrapper)
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''this is add function'''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))

#######################################################################################
#四、柯里化之后的changeAttribute作为装饰器使用
# def changeAttribute(source):
#     def _copy(destination):  # 把源函数属性赋值给目标函数属性
#         print('***',destination.__name__)
#         destination.__name__ = source.__name__
#         destination.__doc__ = source.__doc__
#         print('***',destination.__name__)
#         # return destination #这里为什么要返回destination？
#         # #那是因为
#     return _copy
# def decorate(func):
#     @changeAttribute(func)
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     # changeAttribute(func)(wrapper)
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
在这里我们可以看到当changgeAttribute作为装饰器的时候返回了这样的报错TypeError: 'NoneType' object is not callable
类型错误，对象是不可被调用的
整个的输出结果为
Traceback (most recent call last):
*** wrapper
*** add
  File "C:/Users/Administrator/Desktop/马哥/装饰器/7.带参装饰器.py", line 127, in <module>
    print(add(6,7))
TypeError: 'NoneType' object is not callable

为什么会出现这样的结果呢 ？
那是因为我们装饰器内的函数_copy没有给出一个返回，所以默认的返回就是一个none
而none却不能wrapper函数所以使用，就会报错，

为什么我们的changeAttribute(func)(wrapper)没有报错呢？
那是因为这里只是属于调用，而不是给wrapper传一个返回值，所以不会报错
，因此当changeAttribute作为函数使用的时候我们需要把destination传给wrapper
这样就不会报错了

'''

# #五、装饰器返回值，传参
# def changeAttribute(source):
#     def _copy(destination):  # 把源函数属性赋值给目标函数属性
#         print('***',destination.__name__)
#         destination.__name__ = source.__name__
#         destination.__doc__ = source.__doc__
#         print('***',destination.__name__)
#         return destination
#         # return destination #这里为什么要返回destination？
#         # #那是因为,我们对这个函数进行了修改，我们要的就是这个函数的结果，所以我们需要返回他
#
#     return _copy
# def decorate(func):
#     @changeAttribute(func)#wrapper = changeAttribute(func)(wrapper)
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     # changeAttribute(func)(wrapper)
#     return wrapper
#
# @decorate
# def add(a,b):
#     '''this is add function'''
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))

#经过上面的一系列的修改终于达到了我们的目的，
#吧修改属性的函数作为装饰器，装饰下面装饰原函数的装饰器，
#同事还用到了我们前面说到的带参装饰器


##########################################################################################
# #六、python内部改变装饰器属性的函数
'''
有我们上面的例子我们可以修改装饰器的内部属性变成，被装饰函数的属性，
这其实就是一个属性赋值的过程，我们能想到的python 装饰器的开发者当然也能想到
，在系统里面的有这样一个模块，叫做functools的wraps
'''
# from functools import wraps
#
# #导入了这个模块之后我们的函数就可以简化为
# def decorate(func):
#     @wraps(func)#wrapper = changeAttribute(func)(wrapper)
#     def wrapper(*args,**kwargs):
#         ''' this is wrapper function '''
#         print('before')
#         result = func(*args,**kwargs)
#         print('end ',result)
#         return result
#     # changeAttribute(func)(wrapper)
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
这样的出的结果也是和上面的装饰器的结果是一样的
before
this function is add add this is add function
end  13
13
'''

##########################################################################################

#六、带参装饰器加上缺省值
'''
需求，当我们的装饰器logger需要加上一个缺省值的时候，我们的现有装饰器已经不能满足我们
现有的需求了，就需要对装饰器进行改进从而达到，decorate（n）的需求

分析，由于我们之前的装饰器时属于无参装饰器，即有一个函数作为参数传了进去，如果我们再传
一个参数进去的话会导致装饰器的解构无法判断从而出错（原本的装饰器是@decorate,我们不可能写成@decorate
,应为这样会把格式变成add = decorate(n)(add)，从而出错），我们只能再一次的进行柯里化

'''

#七、带缺省值的装饰器
# from time import sleep
# from datetime import datetime
# from functools import wraps
#
# def decorate(duration = 3):
#     def _decorate(func):
#         @wraps(func)#wrapper = changeAttribute(func)(wrapper)
#         def wrapper(*args,**kwargs):
#             ''' this is wrapper function '''
#             start_time = datetime.now()
#             print('before')
#             result = func(*args,**kwargs)
#             print('end ',result)
#             end_time = datetime.now()
#             delta = (end_time - start_time).total_seconds()
#             if delta > duration:
#                 print('{} took {:.2f}s. too slow'.format(func.__name__,delta))
#             else:
#                 print('too fast')
#             return result
#         # changeAttribute(func)(wrapper)
#         return wrapper
#     return _decorate
#
# # # 不带缺省值，技术没有缺省值，我们也不能写成@decorate，应为这样会变成 add = decorate（add） 但是
# # # 我们需要的是add = decorate（）（add）
# # @decorate()
# # def add(a,b):
# #     '''this is add function'''
# #     sleep(2)
# #     print('this function is add',add.__name__,add.__doc__)
# #     return a+b
# #
# # print(add(6,7))
# #带上缺省值
# #带上缺省值的装饰器
# @decorate(4)
# def add(a,b):
#     '''this is add function'''
#     sleep(2)
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))
#########################################################################################################
# 八、带缺省值的装饰器，
'''
当我们需要把装饰器内的内容保存到另一个函数，文件或者数据库中的时候，我们
还需要对装饰进行修改，但是我们写装饰气的理念就是尽量少的对装饰器或者函数本身进行修改，我们
就要在装饰器外面把功能加到装饰器里面，现在就是我们需要把被装饰函数的执行时间和相关东西单独提取出来
下面我们就要进行修改了
'''

# from time import sleep
# from datetime import datetime
# from functools import wraps
#
# def input_logger(fn,delta,duration):
#     if delta > duration:
#         print('{} took {:.2f}s. too slow'.format(fn.__name__, delta))
#     else:
#         print('too fast')
#
# def decorate(duration = 3,fn = input_logger):#这里的默认输出函数是input_logger，
#     # 如果我们没有比的函数的话，这样就达到了我们输出到另外一个函数的目的
#     def _decorate(func):
#         @wraps(func)#wrapper = changeAttribute(func)(wrapper)
#         def wrapper(*args,**kwargs):
#             ''' this is wrapper function '''
#             start_time = datetime.now()
#             print('before')
#             result = func(*args,**kwargs)
#             print('end ',result)
#             end_time = datetime.now()
#             delta = (end_time - start_time).total_seconds()
#             fn(func,delta,duration)
#             return result
#         return wrapper
#     return _decorate
# @decorate(4)
# def add(a,b):
#     '''this is add function'''
#     sleep(2)
#     print('this function is add',add.__name__,add.__doc__)
#     return a+b
#
# print(add(6,7))

###########################################################################################################

#九、装饰器的封顶是什么？
# 就是当装饰器外面函数的参数是多个的时候就不需要在进行柯里化了，这就是封顶
#类似这样的装饰器我们就没有必要做柯里化了，就算是封顶了
from functools import wraps
from datetime import datetime
from time import sleep
def decorate(duration,func=lambda name,delta:print(name,delta)):
    def wrapper(fn):
        @wraps(fn)
        def inner(*args):
            start = datetime.now()
            result = fn(*args)
            delta = (datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__,delta)
            return result
        return inner
    return wrapper
@decorate(2)
def add(a,b):
    sleep(3)
    print(add.__name__)
    return a+b
print(add(4,5))
###########################################################################################################
'''
函数没调用之前，装饰器就已经把函数给装饰了

带参装饰器
    1、它是一个函数
    2、函数作为它的形参
    3、返回值是一个不带参的装饰器函数
    4、使用functionName(参数列表方式)调用
'''
