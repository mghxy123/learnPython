#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.序列化 与反序列化.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/4 0004

'''序列化的定义:
    serialization序列化
    将内存中的对象存储下来,把它变成一个个字节,->二进制
    deserialization反序列化
    将文件的一个个字节回复成内存中的对象
    序列化保存 到文件就是持久化
    可以将数据序列化后持久化,或者网络传输,也可以将从文件中或者网络接受到的字节序列反序列化
    python提供可序列化的库pickle
    dump 序列化为字节对象
    load 反序列

'''
###########################################################
# import  pickle
#
# filename = 'serialization.txt'
# #对变量 序列化
# #查看下序列化后得到什么
#
# i = 99
# c = 'c'
# l = list('123')
# d = {'a':1,'b':'bcd',c:'[1,2,3]'}
# #序列化,序列化的东西都存入了文件内
# with open(filename,'wb') as f:
#     pickle.dump(i,f)
#     pickle.dump(c,f)
#     pickle.dump(l,f)
#     pickle.dump(d,f)
#
# #反序列化
# with open(filename,'rb') as f:
#     print(f.read(),f.seek(0))
#     for i in range(4):
#         x = pickle.load(f)
#         print(x,type(x))


#######################################################################
#对对象序列化
import pickle
class AAA:
    tttt = 'ABC'
    def show(self):
        print('abc')

a1 = AAA() #创建AAA类的对象

#序列化
ser = pickle.dumps(a1)
print('ser={}'.format(ser))

#反序列化
a2 = pickle.loads(ser)
print(a2.tttt)
a2.show()