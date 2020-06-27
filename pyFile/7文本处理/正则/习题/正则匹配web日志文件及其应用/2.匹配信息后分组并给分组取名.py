#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.匹配信息后分组并给分组取名.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/12 0012

import re

logstr = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
"GET / HTTP/1.1" 200 8642 "-" \
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>.+)\] \
"(?P<method>.+) (?P<url>.+) (?P<protocol>.+)" (?P<status>\d{3}) (?P<size>\d+) \
"-" "(?P<useragent>.+)"'''

regex = re.compile(pattern)

result  = regex.match(logstr)
print(result.groups())
