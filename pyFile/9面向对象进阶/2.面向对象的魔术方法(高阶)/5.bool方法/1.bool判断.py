#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.bool判断.py
# Author: HuXianyong
# Date  : 2019/5/25 16:53


class A:pass

print(bool(A))
print(bool(A()))
# 都是True

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

