#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/2 0002


from random import randrange,randint
from string import ascii_letters
from os import path
import  os,glob
from pathlib import Path
from shutil import copy

def copy_file(base_dir):  # 拷贝文件
    copy_list = choise_file(base_dir)
    make_dir = max((len(x),x) for x in copy_list)[1]
    print(os.path.dirname(make_dir))
    mpath = make_dir.replace('/a/b/', '/dst/b/')
    Path(mpath).parent.mkdir(parents=True, exist_ok=True)# 创建新的文件夹
    #疑惑,这里为什么不要用dirname?,用了dirname就不能创建最后一层目录

    for sfile in copy_list:
        dfile = sfile.replace('/a/b/', '/dst/b/')
        print(dfile)
        dst_dir = os.path.dirname(dfile)
        print(dst_dir)
        try:
            copy(sfile, dfile)
        except Exception as f:
            print(f)


def choise_file(base_dir):  # 筛选需要拷贝的文件
    copy_list = []
    code_dir = os.path.abspath(base_dir)
    check_dir = code_dir + '/**/*.txt'
    print(os.getcwd())
    file_list = glob.glob(check_dir, recursive=True)
    for i in file_list:
        base_name = os.path.basename(i)
        for j in 'xyz':
            if base_name.startswith(j):
                copy_list.append(i.replace('\\', '/'))
    return copy_list
copy_file('../test_dir')


# copy('C:/Users/Administrator/Desktop/马哥/文件处理/test_dir/a/b/xnby.txt', 'C:/Users/Administrator/Desktop/马哥/文件处理/test_dir/dst/b/xnby.txt')

# Path('C:/Users/Administrator/Desktop/马哥/文件处理/test_dir/dst/b/c/d/e/f/g/h/i').mkdir(parents=True,exist_ok=True)