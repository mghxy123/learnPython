#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2匹配ip.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/10 0010


s = '''
192.168.1.50
0.0.0.0
255.255.255.255
17.16.52.100
172.16.0.100
400.400.999.888
001.002.003.000
257.257.255.256
'''

import re

# regex = re.compile('[0-2]?[0-4]?[0-9].{3}([0-2][0-4][0-9])')
regex = re.compile(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)')
print(regex.findall(s))