#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 实现base64解码.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008


'''
思路:
    先把base64码,先把字符串中的等号全都替换掉,
    再全都给转成二进制字符串,
    然后再切掉二进制的ob
    组成24位长的字符串,
    字符串注分成三分,
    分别将三分字符串转成十进制
    将十进制转成字符,给函数返回
'''
import re
baseString=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
baseString1=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

string = 'YWJjZA=='
# string = 'b2lqa2w=' #'oijkl'
# string = 'YXNkZmdoamts' #'asdfghjkl'
str1 = ''

def unbase64(string:str):
    str1 = ''
    _string = string.encode()
    length = len(_string)
    # print(length,_string)
    #判断字符串长度不是4的倍数就退出,base64 一定是4的倍数
    if type(string) is not str and length % 4 != 0:
        exit(1)
    #把base64分成4的倍数份,每一份都是3个字符的ascii
    for offset in range(0,length,4):
        triple = _string[offset:offset+4]
        # print(offset,triple)

        if b'=' in  triple:
            # print(triple)
            triple = re.sub(b'=',b'A',triple)
        stri = ''
        # 循环3次分三份,组成24位二进制
        for i in triple:
            num = baseString1.index(i)
            l = bin(num)[2:].zfill(6)
            # print(num,l)
            stri += l
            # print(stri)
        for i in range(16, -1, -8):
            # print(stri)

            if i == 16:#第一刀
                l = stri[:8]
                # print(i, l)
            elif i == 0:#第三刀
                l = stri[16:]
                # print(i, l)
            else: #第二刀
                l = stri[8:16]
                # print(i, l)
            # print(l,chr(int(l,base=2)))
            str1 += str(chr(int(l,base=2)))
        # print('='*60)
    return str1

print(unbase64(string))
