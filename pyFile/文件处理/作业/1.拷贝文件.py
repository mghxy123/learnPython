#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.拷贝文件.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/30 0030

'''

1.制定一个源文件,实现copy到目标目录
例如把/tmp/test.txt 拷贝到/tmp/test1.txt
'''

from pathlib import Path
from os import path
import os
from shutil import copy

def copy_file(src_file,dst_file):
    dst_dir = path.dirname(path.abspath(dst_file))
    if not os.path.isdir(dst_dir):
        Path(dst_file).parent.mkdir(parents=True,exist_ok=True)

    # with open(src_file,'rb') as fs:
    #     with open(dst_file,'rb') as fd:
    #         length = 16*1024
    #         while True:
    #             buf = fs.read(length)
    #             if not buf:
    #                 break
    #             fd.write(buf)
    copy(src_file,dst_file)

copy_file('../test_dir/test','../test_dir/aa/bb/cc/test1')
