#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 求两个字串的公共子串.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008


# '''
# 思路:
#     先把两个字符串转化为列表
#
# '''
# str1 = 'abfghplf'
# str2 = 'abfgfghp'
# a = set('p')
#
# com1 = [i for i in str1 if i in str2]
# # print(str1[1:8])
# # for i,s in enumerate(str1):
# #     print(i,str1[i])
# # print(com)
# com = set()
# def string(str1:str,str2:str):
#     for i,s in enumerate(str1):
#         if s in str2:
#             for j in range(2,len(str1)):
#                 if str1[i:i+j] == str2[i:i+j]:
#                     print(i,str1[i:i+j])
#                     return string(str1[i:i+j],str2[i:i+j])
#                 else:
#                     com.add(str1[i:j-1])
#                     break
#
#         print('*'*30)
#     return com
# if len(com1) > 1:
#     print(1111,string(str1,str2))
# elif len(com1) == 1:
#     print('公共子串为: %s'%com1)
# else:
#     print('没有公共子串')
# # print(com)



##############################################################
'''
    思路2;
        首先循环str1的长度的次数,一次去str2里面去找是否有匹配的字符串,
        有就继续往深了判断,一直到没不同的时候为止
        没有就继续往下依次循环,直至结束
s1 = 'abcdeg'
s2 = 'strabcabcdgj'

s1依次循环的好处在于可以防止出现后面的匹配长度比后面的长的情况发生,如
abcdedfg
cabcdddddabcdedf
后面的匹配长度比后面的长的情况发生


s1[0:1] != s2[0:1] go on
s1[0:1] != s2[1:2] go on 
s1[0:1] != s2[2:3] go on 
s1[0:1] == s2[3:4] s1[0:2] == s2[3:5]  s1[0:3] == s2[3:6] s1[0:4] != s2[3:6] list.append(s1[0:5])
s1[1:2] != s2[0:1]
.
.
.
s1[5:6] != s2[]
'''
#
# s1 = 'abcdeg'
# s2 = 'strabcabcdgj'
#
# for i,s in enumerate(s1):
#     for j,k in enumerate(s2):
#         n=j
#         # print(i, j, n)
#         while True :
#             n +=1
#             # print('i',i, n)
#             if s1[i:n] == s2[j:n]:
#                 # k=1
#                 print(s1[i-1:n],s2[i-1:n])
#                 print(s1[i:n] , s2[j:n])
#             else:
#                 break
#     print('*'*30)

# ##########################################################################
#
# # s1 = 'abcdeg'
# s2 = 'cdgj'
# s1 = 'strabcabcdgj'
# end = 0
# start = 0
# for i,s in enumerate(s1):
#     for j,k in enumerate(s2):
#         if s1[i] == s2[j] :
#             n = 0
#             while s1[i+n] == s2[j+n] :
#                 n += 1
#                 if n > end:
#                     end = n
#                     start = i
#
#                 else:
#                     break
# print(s1[start:end])
#
#     # print('*'*30)

#################################################################################
#用最笨的一个办法,把短的字符串随机排列组合后最为一个列表,去到唱长字符串里面去比较,在字符串里面的加入列表,求列表里面最长的一个字符串既是结果了

# s1 = 'abcdeg'
s2 = 'cdgj'
s1 = 'strabcabcdgj'


def compare(s1,s2):
    strlist = set()
    for i,k in  enumerate(s1):
        strlist.add(s1[:i+1])
        strlist.add(s1[-i-1:])
    return strlist

def comstr(s1,s2):
    if len(s1) >= len(s2):
        s1,s2=s2,s1
    comset = set()
    string = compare(s1,s2)

    for str in string:
        if str in s2:
            comset.add(str)

    # print(comset)
    maxcom = sorted(comset,key=lambda x:len(x),reverse=True)[:1]
    return maxcom



print(comstr(s1,s2))