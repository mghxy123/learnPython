#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : animal.py
# Author: HuXianyong
# Date  : 2019/5/25 10:14

class Animal:
    x= 123
    def __init__(self,name):
        self._name = name
        self.__age = 10
        self.weight = 20

print('animal Module\'s names = {}'.format(dir())) #模块的属性

'''
这里的dir什么都不加默认就是尽可能的收集当前的属性和方法,Animal没有的就从object集成过来
'''
# print(dir())