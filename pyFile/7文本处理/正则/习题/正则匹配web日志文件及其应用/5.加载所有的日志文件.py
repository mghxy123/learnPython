#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.加载所有的日志文件.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/12 0012

import re,datetime
from pathlib import Path

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datestr>.+)\] \
"(?P<method>.+) (?P<url>.+) (?P<protocol>.+)" (?P<status>\d{3}) (?P<size>\d+) \
"-" "(?P<useragent>.+)"'''

regex = re.compile(pattern)

conversion = {
    'datestr': lambda datestr:datetime.datetime.strptime(datestr,"%d/%b/%Y:%H:%M:%S %z"),
    'ststus': int,
    'size': int
}
def extract(line:str):
    result = regex.match(line)
    if result:
        return {k:conversion.get(k,lambda x:x)(v) for k,v in result.groupdict().items()}
    else:#如果日志格式有问题,这里就可以加上个异常处理
        pass

#对日志文件进行处理,
def loadfiles(filename:str,encoding= 'utf8'):
    with open(filename,encoding=encoding) as f:
        for line in f:
            fields = extract(line)
            if fields:
                print(fields)
            else:
                print('xxxxx{}'.format(line))
# loadfiles('access.log')

def load(*paths,ext='*.log'):
    for x in paths:
        p = Path(x)
        if p.is_dir():
            pass
        else:
            pass