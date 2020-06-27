#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.编写ls的属性输出功能.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/9 0009


from pathlib import Path
from datetime import datetime

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
    ''' 取出modestr形式的字符串,把权限数字33206改为9位二进制数字然后循环,每三位是1就就分别对应了是421也就是权限rwx,拼接字符串,得到我们想要的结果
    有四种方法:
    方法一:把类型直接转为二进制,然后取后九位,也就是去掉0b来进行遍历,但是可能给的整数出现给的太小不够9位可能就会出现问题,比如权限是001(--------x)的文件,这样的取值就会出问题的
        authority = bin(m)[-9:] #
        for i,s in enumerate(authority):
            # print(type(s))
            mstr += modestr[i] if s == '1' else '-'
            # print(mstr, s, i)
    方法二:为了避免出现上面的问题,我们需要把转成二进制的字符串补全为9位然后在进行遍历就没问题了,使用zfill向前填充到9个零
            authority = bin(m)[2:][-9:].zfill(9)
            for i, s in enumerate(authority):
                mstr += modestr[i] if s == '1' else '-'
    #方法三:使用format填充到9个零
    print("{:9b}".format(m)[-9:])
    for i,s in enumerate('{:9b}'.format(m)[-9:]):
        mstr +=  modestr[i] if s== '1' else '-' 

    '''
    #方法四使用移位的办法,使m向右移位,然后和1与,的结果再去判断得出结果
    #推展,什么进制的数都可以做移位运算的,不管是什么进制的数要做移位运算,都需要把他变成二进制之后在进行移位运算的
    #十进制的131 >> 1 十进制的131向右移位运算,其实就是10000011 向右移动一位,放弃最右边的一位数1然后变成了
    #1000001它转化成十进制就是65了

    #所以当我们使用移位运算的时候,就可以不考虑是什么进制的而直接使用了,二进制的与&和或|运算也是可以直接在其他进制使用的
    #结果也是转化为二进制在运算出结果的

    #移位计算是计算机中速度最快的
    for i in range(8,-1, -1):
        mstr += modestr[8-i] if m >> i & 1 else '-'
        #m >> i 在和1进行& 运算结果就是0或者1

    return mstr
def acquireSize(name:Path):
    size = name.stat().st_size
    size_index = ' KMGTP'
    n = 0
    while size >1000:
        size = size //1000
        n += 1
    return str(size)+size_index[n]
def acquireMtime(name:Path):
    mtime = name.stat().st_mtime
    mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    return mtime
def acquireId(name:Path):
    gid = name.stat().st_gid
    uid = name.stat().st_uid
    return gid,uid
#增加详情显示,ls 和 ls -l的区别
def lscommand(path,detail=False):
    p = Path(path)
    ret = []
    if not p.exists() or not p.is_dir():
        exit(1)
    for i in p.iterdir():
        # print(i,type(i))

        if detail == True:
            file_type = _getfiletype(i)
            mtime = acquireMtime(i)
            gid,uid = acquireId(i)
            size = acquireSize(i)
            mode = acquireAuthority(i)

            ret.append((mode,file_type,uid,gid,mtime,size,i.name))
        # print(file_type)
        # print(i.stat())
        else:
            ret.append(str(i.name))
    return ret
print(lscommand('.',detail=True))