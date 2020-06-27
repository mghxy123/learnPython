#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test2.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

class Person:
    def get_score(self):
        # connect to mysql
        ret = {'English':78,'Chinse':86,'History':82}
        return ret
print(type(Person.get_score))