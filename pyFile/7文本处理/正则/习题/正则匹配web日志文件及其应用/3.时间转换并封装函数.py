#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.时间转换.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/12 0012

import re,datetime

logstr = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
"GET / HTTP/1.1" 200 8642 "-" \
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datestr>.+)\] \
"(?P<method>.+) (?P<url>.+) (?P<protocol>.+)" (?P<status>\d{3}) (?P<size>\d+) \
"-" "(?P<useragent>.+)"'''

regex = re.compile(pattern)
# result  = regex.match(logstr)
# print(result.groups())
# print(result.groupdict())

# def conversion_timr(datestr:str):
#     return datetime.datetime.strptime(datestr,"%d/%b/%Y:%H:%M:%S %z")
#
# print(conversion_timr(result.groupdict()['datestr']))

# 1.######################################
# #如果我们需要把匹配到的结果都存入自字典内的话,就需要把匹配到的结果都遍历一遍
# conversion = {
#     'datestr': conversion_timr(result.groupdict()['datestr']),
#     'ststus': int,
#     'size': int
# }
# # print(conversion)
# if result:
#     d = {}
#     for k,v in result.groupdict().items():
#         if k in conversion:
#             d[k] = conversion[k]
#         else:
#             d[k] = v
#     #上面的是一个字典,我们可以把它写成字典解析式
#     # d2 = {k:conversion[k](v) if k in conversion else v for k,v in result.groupdict().items()}
#     print(d)
#     # print(d2)
# 2.######################################

#这样虽然也能得出结果,但是我们却可以把上面的conversion使用lambda函数进行优化进行优化,不再调用conversion_time函数取获得结果了
# conversion = {
#     'datestr': lambda datestr:datetime.datetime.strptime(datestr,"%d/%b/%Y:%H:%M:%S %z"),
#     'ststus': int,
#     'size': int
# }
# if result:
#     d2 = {k:conversion[k](v) if k in conversion else v for k,v in result.groupdict().items()}
#     print(d2)
#     #这样得到的结果和上面得到的结果一样,但是我们少写了很多的代码,效率也高了很多
#
#     #上面虽然也能拿到结果,但是当我们没有时间的时候就会报错,所以我们需要使用get来获取值
#     #并且如果没有取到值的时候就给他传去一个字符串,增加保险
#     d3 = {k:conversion.get(k,str)(v) for k,v in result.groupdict().items()}
#     print(d3)
#
#     #对于上面的代码,我们还可以以另一种形式来写,使用lambda就显得更加的高大上了
#     d4 = {k:conversion.get(k,lambda x:x)(v) for k,v in result.groupdict().items()}
#     print(d4)
# 3.######################################
# 我们依旧还可以进一步的优化,并且使用函数对他进行封装
conversion = {
    'datestr': lambda datestr:datetime.datetime.strptime(datestr,"%d/%b/%Y:%H:%M:%S %z"),
    'ststus': int,
    'size': int
}
def extract(line:str):
    result = regex.match(logstr)
    if result:
        return {k:conversion.get(k,lambda x:x)(v) for k,v in result.groupdict().items()}
    else:#如果日志格式有问题,这里就可以加上个异常处理
        pass