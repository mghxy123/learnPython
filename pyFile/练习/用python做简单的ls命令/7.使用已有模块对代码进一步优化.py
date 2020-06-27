#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.使用已有模块对代码进一步优化.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/10 0010

import stat #减少操作
import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog ='ls',description='list file',add_help=False)

parser.add_argument('path',nargs='?',default='.',help='path help')
parser.add_argument('-a','--all',action='store_true',help='show all files')
parser.add_argument('-l',action='store_true',help='use a long listing format')
parser.add_argument('-h','--human-readable',action='store_true',help='with -l',dest='human')#dest写成human感觉上好像是弄了个别名


def listdir(path,all = False,detail=False,human=False):
    def _humanReadable(name:Path,human=False):
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

    def _lscommand(path,detail,all,human):
        p = Path(path)
        if not p.exists() or not p.is_dir():
            exit(1)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                continue
            if not detail:
                yield str(i.name)
            else:
                st = i.stat()
                mtime = datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                size = _humanReadable(i,human)
                mode = stat.filemode(i.stat().st_mode)
                yield (mode,st.st_uid,st.st_gid,mtime,size,i.name)

    filelist = _lscommand(path,detail,all ,human)
    yield from sorted(filelist,key=lambda x:x[-1])


args = parser.parse_args(['-a'])
# args = parser.parse_args(['../','-lah'])
# print(args.path,args.all,args.l,args.human)
list1 = listdir(args.path,args.all,args.l,args.human)
for i in list1:
    print(i)
