#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.bool方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

# class A:pass
#
# print(bool(A))
# print(bool(A()))
#都是True

################################################

# class B:
#     def __bool__(self):
#         print('in bool')
#         return bool(1)
#
# print(bool(B))
# print(bool(B()))
#
# if bool(B()):
#     print('b','-'*40)

####################################################
# class B:
#     def __bool__(self):
#         print('in bool')
#         return False
#
# print(bool(B))
# print(bool(B()))
#
# if bool(B()):
#     print('b','-'*40)

##########################################################
# class B:
#     def __bool__(self):
#         print('in bool')
#         return bool(self)
#
# print(bool(B))
# print(bool(B()))
#
# if bool(B()):
#     print('b','-'*40)

#这样就会无线递归


#############################################################

class C:
    def __len__(self):
        return 0
print(bool(C))
print(bool(C()))

class D:
    def __len__(self):
        return 1
print(bool(D))
print(bool(D()))

#类再算布尔值的时候,有bool先算bool,没有bool就看len