#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.拷贝文件.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/6 0006

fn1 = 'test'
fn2 = 'test2'

with open(fn1,'w') as f :
    f.writelines('\n'.join(['abc','123','forward']))

#复制
def copy(src,dst):
    with open(src,'rb') as  f1:
        with open(dst,'wb') as f2:
            length = 16* 1024
            while True:
                buff = f1.read(length)
                if not buff:
                    break
                f2.write(buff)

copy(fn1,fn2)
