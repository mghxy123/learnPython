#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.编写ls基本命令.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/9 0009

from pathlib import Path

def _getfiletype(name:Path):
    if name.is_dir():
        return 's'
    elif name.is_char_device():
        return 'c'
    elif name.is_block_device():
        return 'b'
    elif name.is_symlink():
        return 'l'
    elif name.is_socket():
        return 's'
    else:
        return '-'


def lscommand(path):
    p = Path(path)
    ret = []
    if not p.exists() or not p.is_dir():
        exit(1)
    for i in p.iterdir():
        # print(i,type(i))
        file_type = _getfiletype(i)
        print(file_type)
        # print(i.stat())
        ret.append(str(i.name))
    return ret
print(lscommand('.'))