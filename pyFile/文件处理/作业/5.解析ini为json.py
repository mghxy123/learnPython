#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.解析ini为json.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/4 0004

'''
将ini文件解析为json

'''

import json
from pathlib import Path
from configparser import ConfigParser

cfg = ConfigParser()
read_ok = cfg.read('mysql.ini')
# print(read_ok)
# print(cfg.sections(),cfg.default_section)
# print(cfg._sections)
mysql_dict = {}
for k,v in cfg.items():
    mysql_dict[k] = {}
    for j,h in v.items():
        mysql_dict[k][j] = h
        print(k,j,h)

print(mysql_dict)

js = json.dumps(mysql_dict)
print(js)

