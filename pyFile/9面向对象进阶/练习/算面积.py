#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 算面积.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

# import pickle
# class Size:
#     def area(self):
#         raise NotImplementedError()
#
# class TriangleSize(Size):
#     def __init__(self,a:int,b:int,c:int):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         p = (self.a+self.b+self.c)/2
#         s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
#         return s
#
# class  RectangleSize(Size):
#     def __init__(self,b,c):
#         self.b = b
#         self.c = c
#
#     def area(self):
#         s = self.b*self.c
#         return s
#
# class Roundness(Size):
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         s = self.r*self.r*3.14
#         return  pickle.dumps(s)
#
# s = Roundness(5)
# print(pickle.loads(s.area()))
# s = RectangleSize(2,3)
# print(s.area())
# s = TriangleSize(3,4,5)
# print(s.area())


###########################################
import json
import msgpack

class Shape:
    def __init__(self):
        self._area = None# if self.area else self.area

    @property
    def area(self):
        raise NotImplementedError()

class TriangleSize(Shape):
    def __init__(self,a,b,c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self._p = (self.a+self.b+self.c)/2

    @property
    def area(self):
        p = self._p
        if self._area is None:
            self._area =(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return self._area
class  RectangleSize(Shape):
    def __init__(self,b,c):
        super().__init__()
        self.b = b
        self.c = c

    @property
    def area(self):
        if self._area is None:
            self._area =self.b*self.c
        return  self._area

class Roundness(Shape):
    def __init__(self,r):
        super().__init__()
        print(Roundness.__dict__)
        self.r = r

    @property
    def area(self):
        if self._area is None:
            self._area = self.r*self.r*3.14
        return  self._area

s = Roundness(5)
print(s.area)
s = RectangleSize(2,3)
print(s.area)
s = TriangleSize(3,4,5)
print(s.area)


class SerialzablenMixin:
    def dumps(self,t = 'json'):
        if t == 'json':
            return json.dumps(self.__dict__)
        elif t == 'msgpack':
            return msgpack.packb(self.__dict__)
        else:
            raise NotImplementedError('没有实现序列化')

class SerializableCircelMixin(SerialzablenMixin,Roundness):pass

smc = SerializableCircelMixin(4)
print(smc.area)
s = smc.dumps('msgpack')
print(s)

#########################################################################
# class Shape:
#
#     @property
#     def area(self):
#         raise NotImplementedError()
#
# class TriangleSize(Shape):
#     def __init__(self,a,b,c):
#         self._area = None if self._area else self.area
#         self.a = a
#         self.b = b
#         self.c = c
#         self._p = (self.a+self.b+self.c)/2
#
#     @property
#     def area(self):
#         p = self._p
#         if self._area is None:
#             self._area =(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
#         return self._area
#
# class  RectangleSize(Shape):
#     def __init__(self,b,c):
#         self._area = None if self._area else self.area
#         self.b = b
#         self.c = c
#
#     @property
#     def area(self):
#         if self._area is None:
#             self._area =self.b*self.c
#         return  self._area
#
# class Roundness(Shape):
#     def __init__(self,r):
#         self._area = None if self._area else self.area
#         self.r = r
#
#     @property
#     def area(self):
#         if self._area is None:
#             self._area = self.r*self.r*3.14
#         return  self._area
#
# try:
#     s = Roundness(5)
#     print(s.area)
# except Exception as e:
#     print(e)
# # s = RectangleSize(2,3)
# # print(s.area)
# # s = TriangleSize(3,4,5)
# print(s.area)