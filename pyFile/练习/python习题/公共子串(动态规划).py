# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # File  : 公共子串(动态规划).py
# # Author: HuXianyong
# # Date  : 2019/7/11 0:00
#
#
#
# str1=  'abcdefgasdabcdaxyz'
# str2 = 'bcdxyz'
# lss = {}
# def commStr(str1:str, str2:str):
#     len1 = len(str1)
#     len2 = len(str2)
#
#     rmax = 0 #这个是为了得到公共子串的长度,
#     rindex = 0
#
#     arr = [[0] * len1 for _ in range(len2)] # str2为列数,str1为列长度
#     # print(*arr,sep='\n') # 解构打印,看成方阵
#     # print(len1,len2)
#
#     for i,x in enumerate(str2): # 把str2的每一个分解出来, #列数,所以是str2
#         for j,y in enumerate(str1): # 把str1的每一个也分解出来 # 列长度所以是str1
#             if x == y: # 当分解出来的元素相等时自动加1
#                 # print(i,j)
#                 if i == 0 or j == 0: # 当i或者j等于0的时候,就是出于边界,只能是1,所以直接置为1
#                     arr[i][j] = 1
#                 else:
#                     arr[i][j] = arr[i-1][j-1] +1 # 否则在原有基础上加1,既是是第一次也是加1  0+1还是1
#                     if arr[i][j] >= rmax:
#                         rmax = arr[i][j]
#                         rindex = j
#                         print(rmax)
#                         '''
#                         这里由于我们需要取出来的是最长公共子串,所以我们只能在长度的一列上面取值
#                         rmax和rindex都是str1上面的,所以我们接下载的操作就是,截取str1的字符串
#
#                         '''
#     # print(rmax,rindex)
#     # print(str1[rindex - rmax +1:rindex+1])
#     # 这里为什么是(rindex - rmax +1) 呢? 因为rindex记录的是str的下标,rmax是最大长度,用最大下标减去最大长度就得到了公共子串了,但是len()函数的数字要比下标大一位,所以前后都需要加1
#     # print(lss)
#     return str1[rindex - rmax +1:rindex+1]
#
# print(commStr(str1,str2),sep='\n')
# # 但是这样求的话会出现一个bug,也就是长度同为3个但是不一样的,它就显示了第一个公共子串,第二个就不显示了,先睡觉明天解决


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 公共子串(动态规划).py
# Author: HuXianyong
# Date  : 2019/7/11 0:00


str1 = 'abcdefgasdabcdaxyz'
str2 = 'bcdxyz'
lss = {}


def commStr(str1: str, str2: str):
    len1 = len(str1)
    len2 = len(str2)

    rmax = 0  # 这个是为了得到公共子串的长度,
    rindex = 0

    arr = [[0] * len1 for _ in range(len2)]  # str2为列数,str1为列长度
    # print(*arr,sep='\n') # 解构打印,看成方阵
    # print(len1,len2)

    for i, x in enumerate(str2):  # 把str2的每一个分解出来, #列数,所以是str2
        for j, y in enumerate(str1):  # 把str1的每一个也分解出来 # 列长度所以是str1
            if x == y:  # 当分解出来的元素相等时自动加1
                # print(i,j)
                if i == 0 or j == 0:  # 当i或者j等于0的时候,就是出于边界,只能是1,所以直接置为1
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j - 1] + 1  # 否则在原有基础上加1,既是是第一次也是加1  0+1还是1
                    if arr[i][j] >= rmax:
                        rmax = arr[i][j]
                        rindex = j
                        print(rmax)
                        '''
                        这里由于我们需要取出来的是最长公共子串,所以我们只能在长度的一列上面取值
                        rmax和rindex都是str1上面的,所以我们接下载的操作就是,截取str1的字符串

                        '''
    # print(rmax,rindex)
    # print(str1[rindex - rmax +1:rindex+1])
    # 这里为什么是(rindex - rmax +1) 呢? 因为rindex记录的是str的下标,rmax是最大长度,用最大下标减去最大长度就得到了公共子串了,但是len()函数的数字要比下标大一位,所以前后都需要加1
    # print(lss)
    return str1[rindex - rmax + 1:rindex + 1]


print(commStr(str1, str2), sep='\n')
# 但是这样求的话会出现一个bug,也就是长度同为3个但是不一样的,它就显示了第一个公共子串,第二个就不显示了,先睡觉明天解决