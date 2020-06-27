#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.使用call方法实现累加.py
# Author: HuXianyong
# Date  : 2019/5/25 21:39

#累加
class Adder:
    def __call__(self, *args, **kwargs):
        ret  = 0
        for x in args:
            ret +=x
        self.ret = ret
        return ret
adder = Adder()
print(adder(4,5,6))
print(adder.ret)