#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.实现温度处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

'''
4、实现温度处理
    实现花式温度和摄氏温度的转换
    摄氏度 = 5*（华氏温度 - 32）/9
    华氏温度 = 9*摄氏温度 + 32
'''

class temperature:
    def __init__(self):
        pass

    def celsius(self,temp):
        cel = 5*(temp-32)/9
        return cel

    def fahrenheit(self,temp):
        fah = 9*temp/5 +32
        return fah

    def kelvin(self,temp):
        kel = temp+273.15
        return kel

a = temperature()
print(a.celsius(50))
print(a.fahrenheit(50))
print(a.kelvin(50))