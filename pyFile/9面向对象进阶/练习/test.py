#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020


# class Document:
#     def __init__(self,content):
#         self.content = content
#
# def printing(cls):
#     def printt(self):
#         print(self.content)
#     cls.print = printt
#
#     return cls
#
# @printing #Word = printint(Word('aaa'))
# class Word(Document):pass
#
#
# a = Word('aaa')
# a.print()


###################################

#################################################################
# class A:
#     def __init__(self,a):
#         self.a = a
#
# class B(A):
#     def __init__(self,b,c):
#         super(B, self).__init__(5)
#         self.b = b
#         self.c = c
#
#     def sum(self):
#         size = self.a*self.b*self.c
#         return size
#
# b = B(3,4)
# print(b.sum())

def foo():
    try:
        1/0
    except IndexError as e:
        print(e)
    finally:
        print('finally')
        return 'finally'

try:
    foo()
except Exception as e:
    print('111')
finally:
    print('2222')
