#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.as子句.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

#raise 能抛出什么样的异常?

# class A:pass
#
# try:
#     #1/0
#     raise 1
#     # raise 'abc'
#     # raise {}
#     # raise A
#     # raise A()
# except:
#     print('catch the exception')
##############################################################

# class MyException(Exception):
#     def __init__(self,code,message):
#         self.code = code
#         self.message = message
#
# try:
#     raise MyException
# except MyException as e:
#     print('catch my exception')
# except:
#     print('catch other ~~~')
#
# #运行结果是什么?为什么?

# ##############################################################
# class MyException(Exception):
#     def __init__(self,code,message):
#         self.code = code
#         self.message = message
#
# try:
#     raise MyException
# except MyException as e:
#     print('catch my exception')
# except Exception as e:
#     print(e)
##############################################################
#传入参数
class MyException(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message

try:
    raise MyException(200,'error')
except MyException as e:
    print('catch my exception')
except Exception as e:
    print(e)
