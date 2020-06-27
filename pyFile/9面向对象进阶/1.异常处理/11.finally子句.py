#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 11.finally子句.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

# f = None
# # try:
# #     f = open('test.txt')
# # except FileNotFoundError as e:
# #     print('{}'.format(e))
# # finally:
# #     print('清理工作')
# #     try:
# #         f.close()
# #     except Exception as e:
# #         print(e)

# finally的执行时机

#测试
def foo():
    try:
        print('try')
        return 3
    except:
        print('except')
        return 2
    finally:
        print('finally')
        return 1
    print('==')
print(foo())