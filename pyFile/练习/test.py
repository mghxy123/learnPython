#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024


# def a():
#     l = []
#     l2 = []
#     for i in range(1,4):
#         def b():
#             return i**2
#         # print(b())
#         # print(l)
#         l.append(b())
#         l2.append(b)
#         print(l)
#         print(l2)
#     return l
#
# a()
# f1,f2,f3 = a()
# print(f1(),f2(),f3())
# print(a())
# print(a()[0]())
# print('*'*30)
# print(a()[1]())
# print('*'*30)
# print(a()[2]())


















# def a():
#     li = []
#     print(li)
#     for i in range(1,4):
#         def b():
#             print('*'*30,i)
#             return i**2
#         li.append(b)
#         print('~~~~')
#     return li
# a1,a2,a3 = a()
# 
# print(a1())
# print(a2())
# print(a3())


# list1 = []
# def aa():
#     for i in range(5):
#         list1.append(i)
#         return list1
#
# bb = aa
# print(bb())


# def aa():
#     for i in  range(5):
#         print(i)
#
# bb = aa
# bb()


#
# def func1(fn):
#     print('func1')
#     def inner(x):
#         return fn(x)
#     return inner
#
# def func2(fn):
#     print('func2')
#     def inner(x):
#         return fn(x)
#     return inner
#
# @func1
# @func2
# def add(x):
#     print('add')
#     return x
# add(5)



# def aa():
#     print('a1a')
#
# def a():
#     print('a')
#
# def b():
#     print('ab')
#
# dic = {'a':a,'b':b}
# dic.get('b','a')()


# def func(fn):
#     def inner(x,y):
#         return fn(x,y)
#     return inner
#
# @func
# def add(x,y):
#     return x+y
# print(add(2,3))

# def func(z=5):
#     def _func(fn):
#         def inner(x,y):
#             return fn(x,y,z)
#         return inner
#     return _func
# @func() #add = func(z=5)(_func(add)(inner(x,y)))--->return add(x,y,z)
# def add(x,y,z):
#     return x+y+z
# print(add(2,3))

# s2 = b'a'
#
# d = int.from_bytes(s2,'big')
#
# e = d & 63
# # d = bytearray(d)
# print(e)

# 01100001
# 00111111
# 00100001

# def _b64encode_str( s0, s1, s2 ):
#     """
#     s0、s1、s2 依次为第一、二、三个字符
#     """
#     d = s2 & 63
#     d = bytearray(d)
#     c1 = ( s1 & 15  ) << 2
#     c2 = ( s2 & 192 ) >> 6
#     c = c1 + c2
#     c = bytearray[ c ]
#     b1 = ( s0   & 3 ) << 4
#     b2 = ( s1 & 240 ) >> 4
#     b = b1 + b2
#     b = bytearray[ b ]
#     a = ( s0 & 252 ) >> 2
#     a = bytearray[ a ]
#     return ''.join( [ a, b, c, d ] )





# from os import path
# dir1 = '/a/b/c/d/e/f/g.txt'
# aa = ''
# # print(dir.count('/'))
# i = 0
# # dir_name = path.dirname(dir)
#
# def dir_name(dir):
#     pah = path.dirname(dir1)
#     print(pah)
#     return pah
# while i <= dir1.count('/'):
#     dir1 = dir_name(dir1)
#     i += 1


# from pathlib import Path
# import  os
# p = Path()
# p1 = Path.cwd()
# # print(p)
# # print(p1)
# print(str(p1))
# for i in p1.iterdir():
#     if i.is_dir():
#         print('%-20s is dir'%(i.name))
#     else:
#         print('%-20s is file' % (i.name))


#
# def ignoe(names):
#     r = set(filter(lambda x:x.startswith('b'),names))
#     return r
# print(ignoe(['a','b','c']))


# def aaa():
#     def wrapper():
#         print('aaa')
#     return wrapper
#
# a = aaa()
#
# stri = ''
# for i in range(16,-1,-8):
#     # print(i,bin(i)[2:])
#     # binn = bin(i)[2:]
#     # print(binn,type(binn))
#     l = bin(i)[2:].zfill(8)
#     stri += l
#     print(stri)
#     # print(length)
#     # if length <6:
#     #     n = 6-length
#     #     for i in n:
#     #         length +
#     #

# stri = '011000010110001001100011'
# print(stri)
# for i in range(16,-1,-8):
#
#     if i == 16:
#         l = stri[8:]
#         print(i,l)
#     elif i == 0:
#         l = stri[16:8]
#         print(i,l)
#     else:
#         l = stri[8:16]
#         print(i,l)

# for i in range(9):
#     for j in range(9):
#         print(j)
#         if j == 5:
#
#             break
#     print('i',i)


# import math
#
# #ceil 是向上取整
#
# print(math.ceil(2.0000))
# print(math.ceil(2.0001))
# print(math.ceil(2.1),math.ceil(2.4999),math.ceil(2.5000),math.ceil(2.6))
# print(math.ceil(-2.1),math.ceil(-2.4999),math.ceil(-2.5000),math.ceil(-2.6))
#
# #floor 是向下取整
# print('='*67)
# print(math.floor(2.0000))
# print(math.floor(2.0001))
# print(math.floor(2.1),math.floor(2.4999),math.floor(2.5000),math.floor(2.6))
# print(math.floor(-2.1),math.floor(-2.4999),math.floor(-2.5000),math.floor(-2.6))
#
# #除法取整属于向下取整
# print(1//2,-1//2,2//2,-2//2,3//2,-3//2)
#
# #round 是四舍六入,五取偶
# print('round')
# print(round(3.5),round(2.4999),round(2.5000),round(2.6))
# print(round(-3.5),round(-2.4999),round(-2.5000),round(-2.6))
#
# ###进制转换
# print(bin(10),oct(10),hex(10))#'这些转换过来的都是字符串'
#
# lo = 'asd'
# di = {
#     'a':'1',
#     'b':2
# }
# print(di.get('a',5))
# print(di.get('s',5))
# print(di.get('d',lambda x:x)(lo))
# print(di.get('a',lambda x:x)(lo))


# for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("%s * %s = %-5s"%(j,i ,i*j),end='')
# #     print()


# lit = [11,22,33,44,55,66,77,88,99]
# dit = {'a':1,'b':5,'c':3,'d':8}
# a = list(filter(lambda x:x%3==0,lit))
# b = list(map(lambda x:(x%3,x),lit))
# c = sorted(lit, key=lambda x:x>66,reverse=True)
# d = sorted(dit.items(),key=lambda x:x[1])
# print(a)
# print(b)
# print(c)
# print(d)

