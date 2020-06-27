#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 命令分发器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/26 0026

'''
程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数
如果此命令没有对应的注册函数，执行默认函数
用户输入用input(">>")

'''

#1/.#这是一个最简单的通过输入特定值然后输出函数内的东西的方式
# def func1():
#     print('this  is func1')
#
# def func2():
#     print('this  is func2')
#
# def default():
#     print('this is default')
#
# def dispatcher():
#     choise = input('''
#     请输入你的命令 >>
#     ''')
#     if choise == "ls":
#         func1()
#     elif choise == "pwd":
#         func1()
#     else:
#         default()
# dispatcher()


#####################################################################
#2.通过装饰器写一个命令分发器
#
# def dispatcher(fn):
#     def wrapper(name):
#         print('show command {}'.format(name))
#         return fn(name)
#     return wrapper
#
# @dispatcher
# def command1(name):
#     print('i im print command1')
#     return name
#
# @dispatcher
# def command2(name):
#     print('i am print command2')
#     return name
#
# print(command1('ls'))
# print('#'*50)
# print(command2('pwd'))

####################################################################
# #3.利用字典把命令和函数对应起来,输入命令调用函数,通过字典的key运行函数
#
# command_dict = {}
# #编写装饰器,并把命令和函数对象存入字典
# def register(command):
#     def wrapper(func):
#         command_dict[command] = func
#         return func
#     return wrapper
#
# #编写用户输入命令,并查找字典
# def dispatcher():
#     while True:
#         cmd = input('''
#         请输入你的命令!
#         ''')
#         if cmd == "":
#             break
#         print(command_dict)
#         command_dict.get(cmd,default)()#同时get两个key是或的关系
#         # #上面的语句可以写为:
#         # if cmd in command_dict:
#         #     command_dict.get(cmd)()
#         # else:
#         #     default()
#         '''
#         这里字典的get的key可以不在字典里面,这里get两个是或的关系,get(cmd)或get(default)
#         虽然default不在dict里面但是属于他可调用的变量内,就没问题了
#         '''
# #编写命令对应函数
# @register('ls')
# def command_ls():
#     print('ls')
#
# @register('pwd')
# def command_pwd():
#     print('pwd')
#
# def default():
#     print('unkown command!')
#
# dispatcher()


#############################################################################
#4.封装上面的命令分发器
#由于函数的调用可能会很多,变量名可能会重复,所以最好不要把变量名写为全局变量,因此对上面的函数做封装
def new_dispatcher():
    command_dict = {}
    #编写装饰器,并把命令和函数对象存入字典
    def register(command):
        def wrapper(func):
            command_dict[command] = func
            return func
        return wrapper

    #编写用户输入命令,并查找字典
    def dispatcher():
        while True:
            cmd = input('''
            请输入你的命令!
            ''')
            if cmd == "":
                break
            print(command_dict)
            command_dict.get(cmd,default)()#同时get两个key是或的关系
            # #上面的语句可以写为:
            # if cmd in command_dict:
            #     command_dict.get(cmd)()
            # else:
            #     default()
            '''
            这里字典的get的key可以不在字典里面,这里get两个是或的关系,get(cmd)或get(default)
            虽然default不在dict里面但是属于他可调用的变量内,就没问题了
            '''
    return register,dispatcher
register,dispatcher = new_dispatcher()
#编写命令对应函数
@register('ls')
def command_ls():
    print('ls')

@register('pwd')
def command_pwd():
    print('pwd')

def default():
    print('unkown command!')
dispatcher()