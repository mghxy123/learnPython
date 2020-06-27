#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.复制目录.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/6 0006

import shutil
from pathlib import Path
from string import ascii_letters
import random

#当前工作目录
basedir = Path('.')
sub = Path('a/b/c/d')
dirs = [sub] + list(sub.parents)[:-1]
print(dirs)

#创建所有目录
(basedir /  sub).mkdir(parents=True,exist_ok=True)

#生成随机文件名
filenames = (''.join(random.choices(ascii_letters,k=4))for i in range(50))
# print(list(filenames)) #如果这里的print打印出来,就会导致下面的for循环为空

#拼接路径生成文件
for name in filenames:
    (basedir / random.choice(dirs) / name).touch()

#名称开头
headers = set('xyz')
print(headers)

def ignore_files(src,names):
#    return {name for name in names if name[0] not in headers and Path(src,name).is_file()}
    return set(filter(lambda name: name[0] not in headers and Path(src,name).is_file(),names))

shutil.copytree(str(basedir / 'a'),str(basedir / 'dst'),ignore=ignore_files)

#遍历所有文件
print('-'*30)
for f in basedir.rglob('*'):
    print(f)