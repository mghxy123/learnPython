#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.正则匹配日志.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/12 0012

import re

logstr = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
"GET / HTTP/1.1" 200 8642 "-" \
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'''

pattern = '''([\d.]{7,}) - - \[(.+)\] "(.+) (.+) (.+)" (\d{3}) (\d+) "-" "(.+) \((.+); \+(.+)"'''

regex = re.compile(pattern)

result  = regex.match(logstr)
print(result.groups())

