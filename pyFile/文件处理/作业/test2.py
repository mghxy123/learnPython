#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test2.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/2 0002


import re
s = '''
os.path.lexists(path) 
Return True if path refers to an existing path. Returns True for broken symbolic links. Equivalent to exists() on platforms lacking os.lstat().
'''

print(re.split('\W+',s))
print(re.split('[^a-z,A-Z0-9]+',s))
print(re.split('[.()\n,\s]+',s))
print(re.split('\.|\(|\)| |\n|,',s))