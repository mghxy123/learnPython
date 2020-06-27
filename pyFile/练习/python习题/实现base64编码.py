#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 实现base64编码.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/27 0027


'''
Base64是一种用64个字符来表示任意二进制数据的方法;
是把三个字符变成四个字符的
        ~         ~           ~
        126         126        126
转换前 111111  10 1111 1110 11 111110 （二进制） ascii

转换后 111111  101111  111011  111110 （二进制） base64
        63      47      59      62
        /      v       x       +

转换后 00111111  00101111  00111011  00111110  base64补齐为8位

如上面的例子所示,我们要把三个漂号~转化为base64,对应的编码为/vx+


如果我们只是一个ascII码的话需要在后面补两个零,我们在ascII补了几个零,就在对应的base64补上几个等号
        ~       0           0
转换前 111111 10 0000  0000 00 000000
转换后 111111 100000   000000  000000
        /       g       =       =


如果我们只是一个ascII码的话需要在后面补两个零,我们在ascII补了几个零,就在对应的base64补上几个等号
        ~       !           0
转换前 111111 10 1111  1110 00 000000
转换后 111111 101111   111000  000000
        /       v       4       =


baseString=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
'''
# baseString= ''
# for i in range(65,91):
#     baseString +=chr(i)
# for i in range(97,123):
#     baseString +=chr(i)
# for i in range(48,58):
#     baseString +=chr(i)
#
# baseString += '+/'
# print(baseString)


'''
核心编码思想:
每三个字节断开,就拿出3按个字节,没留个bit断开成四段.
应为每个字节其实只占用了6位,2的六次方就是64,这就是base64的由来
每一段当做一个8bit看他的值,这个只就是base64的编码表的索引,找到对应的字符
'''
baseString=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
baseString1='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# src = 'abcd'
src = 'asdfghjkl'

def base64(src:str):
    ret = bytearray()
    aa = []
    if isinstance(src,str): #判断输入的是否是字符串
        _src = src.encode() #对字符串进行解码,默认是unicode
    else:
        return #如果不是就退出程序

    length = len(_src)

    for offset in range(0,length,3):#每次取字符串的三个字节
        triple = _src[offset:offset+3] #切片可超界
        # print(triple)

        last_length = 3- len(triple) #每次切片都判断是否是最后满足,不满足的在末尾加上0补全三位,这样便于计算
        if last_length:
            triple +=b'\x00' * last_length
        # print(triple)
        b = int.from_bytes(triple,'big')
        # print(b,hex(b),type(b))
        for i in range(18,-1,-6):
            '''
                向右移几位,右边的几位全部放弃,
                然后末6位与63进行与运算,所谓的与运算就是,真假为假,真真位真,假假为假,得出我们需要的末六位数
                abc 向右移6位,和63进行与运算得出我们想要的结果 
                63对应的16进制是0x3F
                011000  01 0110  0010 01  100011 >>6 & 0x3F == 9
                011000  01 0110  0010 01 变成了这样,然后进行与运算
                000000  00 0000  1111 11 == 000000 000000 001001 == 9
                剩下的几位也是如此运算的
            '''
            index = b >> i if i == 18 else b >> i & 0x3F
            # aa.append(baseString1[index])
            # print(index,aa)
            ret.append(baseString[index])
        if last_length:
            ret[-last_length:] = b'=' *last_length #ASCII补了几个零,这里就要加上几个等号
    return bytes(ret)
print(base64(src))
