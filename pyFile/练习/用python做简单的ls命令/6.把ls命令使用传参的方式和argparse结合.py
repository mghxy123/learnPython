#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.把ls命令使用传参的方式和argparse结合.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/10 0010

import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog ='ls',description='list file',add_help=False)

parser.add_argument('path',nargs='?',default='.',help='path help')
parser.add_argument('-a','--all',action='store_true',help='show all files')
parser.add_argument('-l',action='store_true',help='use a long listing format')
parser.add_argument('-h','--human-readable',action='store_true',help='with -l',dest='human')#dest写成human感觉上好像是弄了个别名

parser.print_help()
args = parser.parse_args(['../','-lah'])

print('-'*30)
print(args.path,args.all,args.l,args.human)

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

modestr = 'rwxrwxrwx,'
def acquireAuthority(name:Path):
    mstr = ''
    m = name.stat().st_mode
    for i in range(8,-1, -1):
        mstr += modestr[8-i] if m >> i & 1 else '-'
    return mstr
def humanReadable(name:Path,human=False):
    size = name.stat().st_size
    if human :
        size_index = ' KMGTP'
        n = 0
        while size >1000:
            size = size //1000
            n += 1
        return str(size)+size_index[n]
    else:
        return size
def acquireMtime(name:Path):
    mtime = name.stat().st_mtime
    mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    return mtime
def acquireId(name:Path):
    gid = name.stat().st_gid
    uid = name.stat().st_uid
    return gid,uid

def lscommand(path,detail=False,all = False,human=False):
    p = Path(path)
    ret = []
    if not p.exists() or not p.is_dir():
        exit(1)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        if detail == True:
            file_type = _getfiletype(i)
            mtime = acquireMtime(i)
            gid,uid = acquireId(i)
            size = humanReadable(i,human)
            mode = acquireAuthority(i)
            ret.append((mode,file_type,uid,gid,mtime,size,i.name))
        else:
            ret.append(str(i.name))
    return ret
print(lscommand(args.path,args.all,args.l,args.human))