#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 装饰器编写缓存.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/26 0026

'''

二、实现一个cache装饰器，实现可过期被清除的功能
简化设计，函数的形参定义不包含可变位置参数、可变关键词参数和keyword-only参数
可以不考虑缓存大小，也不用考虑缓存满了之后的换出问题
# 进阶
def add(x=4, y=5):
time.sleep(3)
return x + y
以下6种，可以认为是同一种调用
print(1, add(4,5))
print(2, add(4))
print(3, add(y=5))
print(4, add(x=4,y=5))
print(5, add(y=5,x=4))
print(6, add())

'''


#################################################################################
# #第一步,先实现装饰器装饰原函数的功能
# from functools import wraps
#
# #定义一个缓存装饰器函数
# def cache(fn):
#     @wraps(fn)#把被装饰器装饰过的函数,属性都复制过来
#     def wrapper(*args,**kwargs):
#         result = fn(*args,**kwargs)
#         return result
#     return wrapper
#
# @cache
# def add(x=4,y=5):
#     return x+y
#
# print(add())
# print(add(2))
# print(add(2,6))

# ###############################################################################
# #第一步,先实现装饰器装饰原函数的功能
# #第二步,检查参数属性
# from functools import wraps
# from inspect import signature
# from time import sleep
#
# #定义一个缓存装饰器函数
# def cache(fn):
#     local_cache = {}
#     @wraps(fn)#把被装饰器装饰过的函数,属性都复制过来
#     def wrapper(*args,**kwargs):
#         sig = signature(fn) #获取参签名
#         params = sig.parameters #获取参数属性 #OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
#         # print(params)
#         target = {} #这个字典就是每次存入新的内容才会使用
#         # 解决关键字传参
#         target.update(zip(params.keys(),args),**kwargs)# 解决顺序传参的问题
#         # print(params.keys())
#         """
#         上面的也可以写成:
#         names = list(params.keys())
#         for i ,v in enumerate(args):
#             target[names[i]] = v
#         """
#
#         #解决缺省值问题
#         for k,v in params.items():
#             # print('*'*50,v.default)#4和5
#             # print('~'*50,params.keys())#odict_keys(['x', 'y'])
#             # print('~'*50,params.values())#odict_values([<Parameter "x=4">, <Parameter "y=5">])
#             if k not in target.keys():
#                 target[k]  = v.default #inspect._empty
#         #解决了传入参数的问题,下面就需要解决传入参数的排序问题,我们通过target的value来进行排序,从而达到目的
#         #应为用户传入的参数不一定都是x在前y在后的,这样排序之后,把这个列表转化为元组,来作为我们存入cache的key来进行保存
#         key = tuple(sorted(target.items()))
#         print(key)
#         print(local_cache.keys())
#         # print(target)
#
#         #如果key不存在那么,就返回原函数去计算,并把计算结果存入缓存中,然后把缓存中的结果直接给函数调用出来
#         if key not in local_cache.keys():
#             local_cache[key] = fn(**target)
#             # return  local_cache[key]
#         print('这里走了缓存了')
#         return local_cache[key]
#     print(local_cache)
#     return wrapper
#
# @cache
# def add(x=4,y=5):
#     sleep(2)
#     return x+y
#
# print(add())
# print('+'*60)
# print(add(y=5,x=4))


###############################################################################
#第一步,先实现装饰器装饰原函数的功能
#第二步,检查参数属性,存入缓存
#第三部,加入缓存过期时间,多个装饰器一起使用,并使用了带参装饰器
from functools import wraps
from inspect import signature
from time import sleep
from datetime import datetime

def logger(fn):

    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.now()
        result = fn(*args,**kwargs)
        delta = datetime.now() - start
        print('函数的运算时间',delta)
        return result
    return wrapper

#定义一个缓存装饰器函数
def cache(duration = 3):
    def _cache(fn):
        local_cache = {}
        @wraps(fn)#把被装饰器装饰过的函数,属性都复制过来
        def wrapper(*args,**kwargs):

            #先记录,再删除
            expire_keys = []
            start = datetime.now().timestamp()
            for k,(_,timstamp) in local_cache.items():
                if start - timstamp >duration:
                    expire_keys.append(k)
            for k in expire_keys:
                print('清除缓存')
                local_cache.pop(k)

            sig = signature(fn) #获取参签名
            params = sig.parameters #获取参数属性 #OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
            # print(params)
            target = {} #这个字典就是每次存入新的内容才会使用
            # 解决关键字传参
            target.update(zip(params.keys(),args),**kwargs)# 解决顺序传参的问题
            # print(params.keys())
            """
            上面的也可以写成:
            names = list(params.keys())
            for i ,v in enumerate(args):
                target[names[i]] = v
            """

            #解决缺省值问题
            #办法一.用循环
            # for k,v in params.items():
            #     # print('*'*50,v.default)#4和5
            #     # print('~'*50,params.keys())#odict_keys(['x', 'y'])
            #     # print('~'*50,params.values())#odict_values([<Parameter "x=4">, <Parameter "y=5">])
            #     if k not in target.keys():
            #         target[k]  = v.default #inspect._empty
            # 办法一.用循环,但是把循环简化了
            #上面的步骤可以合并为下面的这一步,给字典target传入一个键值对,并更新
            # target.update((k,v.default) for k,v in params.items() if k not in target.keys())
            #办法三.通过两个字典key的差集,来补充缓存字典的k,v
            target.update(((k,params[k].default) for k in (params.keys() - target.keys())))
            #解决了传入参数的问题,下面就需要解决传入参数的排序问题,我们通过target的value来进行排序,从而达到目的
            #应为用户传入的参数不一定都是x在前y在后的,这样排序之后,把这个列表转化为元组,来作为我们存入cache的key来进行保存
            key = tuple(sorted(target.items()))
            # print(key)
            # print(local_cache.keys())
            # print(target)

            #如果key不存在那么,就返回原函数去计算,并把计算结果存入缓存中,然后把缓存中的结果直接给函数调用出来
            if key not in local_cache.keys():
                print('存入缓存')
                local_cache[key] = fn(**target),start
            print('使用缓存')
            return local_cache[key]
        print(local_cache)
        return wrapper
    return _cache

#多个装饰器合并使用,使用顺序是由下而上
#我们也可以这样理解使用顺序,应为越是靠近函数的装饰器,就越早的能装饰原函数,这样他的上层装饰器才可以继续装饰原函数
@logger
@cache(3)
def add(x=4,y=5):
    sleep(2)
    return x+y

print(add())
print('+'*60)
print(add(y=5,x=4))
sleep(4)
print(add(y=5))
print('+'*60)
print(add(x=4))
