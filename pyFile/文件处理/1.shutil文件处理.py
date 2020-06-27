#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.shutil文件处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/29 0029

'''
shutil中的sh是shell的意思,util是工具的意思

'''

#####################################################################################
# #1.使用with  open 来实现文件复制(指针问题)
######################################################################################
# with open('test_dir/test','w+') as f:
#     f.write('abcd 1234')
#     f.flush()
#     print('这个是test文件的内容',f.read())
#     with open('test_dir/test2','w+') as f2:
#         f2.write(f.read())
#         print('这个是test2文件的内容',f.read())
#
# '''输出结果为:
# 这个是test文件的内容
# 这个是test2文件的内容
# '''

# '''这里代码执行结束之后为什么文件test有数据,但是test2没有?
#     那是因为:我们在给问价test写入数据的时候指针指向了最后的结束符号EOF
#     当我们去读取test文件的时候就是空文件,所以导致了test2文件写入的是空数据
#     因此test2没有数据,而不是因为没有flush数据到test2的原因,我们可以用下面的例子来证明
# '''
####################################################################################
# #1.使用with  open 来实现文件复制(指针问题)
# with open('test_dir/test','w+') as f:
#     f.write('abcd 1234')
#     f.flush()
#     f.seek(0)
#     print('这个是test文件的内容',f.read())
#     f.seek(0) #这里再次把指针指向了开头,每次读取文件指针都会变化,不然同样test2没数据
#     with open('test_dir/test2','w+') as f2:
#         f2.write(f.read())
#         f2.flush()
#         f2.seek(0)
#         print('这个是test2文件的内容',f2.read())
#
# '''输出结果为:
# 这个是test文件的内容 abcd 1234
# 这个是test2文件的内容 abcd 1234
# # '''
#这样当我们再次执行代码的时候,test2就有了

#######################################################################################
# #2.使用shutil.copyfileobj来实现文件复制
# # 但是我们的第一种方法二第二种方法都不能考本文件的属性一类的东西,我们只能
# # 拷贝 文件的数据,其他的都不行
# #####################################################################################
# from shutil import copyfileobj
# with open('test_dir/test','r+') as f:
#     f.write('hello python !')
#     f.flush()
#     f.seek(0)
#     print('这个是test文件的内容',f.read())
#     f.seek(0)
#     with open('test_dir/test2','w+') as f2:
#         copyfileobj(f,f2)
#         print('这个是test2文件的内容',f2.read())
#
# '''输出结果为:
# 这个是test文件的内容 hello python !
# 这个是test2文件的内容
#
# '''
#
# '''
# 在这里我们也遇到了1同样的问题,我们在拷贝文件对象的时候也没有把
# 文件内容给复制到test2的文件上,
# 原因同样是指针的问题,下面的代码加上指针就知道了
# '''
# from shutil import copyfileobj
# with open('test_dir/test','r+') as f:
#     f.write('hello python !')
#     f.flush()
#     f.seek(0)
#     print('这个是test文件的内容',f.read())
#     f.seek(0)
#     with open('test_dir/test2','w+') as f2:
#         copyfileobj(f,f2)
#         f2.seek(0)
#         print('这个是test2文件的内容',f2.read())

# '''输出结果为:
# 这个是test文件的内容 hello python !
# 这个是test2文件的内容 hello python !
# '''

#######################################################################################
# .查看shutil.copyfileobj的源代码
# '''
# 这个copyfileobj源码实现拷贝的原理很简单,就是把源文件对象和目标文件对象传入函数copyfileobj函数
# 默认的二进制拷贝长度为16*1024(这里最好是1024的整数倍,这样便于二进制数据的存储),每次拷贝16*1024
# 的字节长度,直到数据拷贝完了,退出循环,
# 由此也可以看出了我们之前的copyfile为什么没有拷贝到数据了,那是因为指针在写入或者读取文件的时候
# 会指向数据的末尾,故此没有数据存入文件,
# '''
# def copyfileobj(fsrc, fdst, length=16*1024):
#     """copy data from file-like object fsrc to file-like object fdst"""
#     while 1:
#         buf = fsrc.read(length)
#         if not buf:
#             break
#         fdst.write(buf)

#######################################################################################
# 查看shutil.copyfile的源代码
######################################################################################
# '''
# 这个copyfile的文件拷贝原理就如同我们第一步所写的那样,打开,读取,写入,完成,但是加上了属性拷贝,
# copyfile的src和dst都是字符串
# '''
# def copyfile(src, dst, *, follow_symlinks=True):
#     """Copy data from src to dst.
#
#     If follow_symlinks is not set and src is a symbolic link, a new
#     symlink will be created instead of copying the file it points to.
#
#     """
#     if _samefile(src, dst): #检查拷贝的源和目标是否是同一个文件,是同一个文件就无法拷贝自己来覆盖自己,直接抛出异常
#         raise SameFileError("{!r} and {!r} are the same file".format(src, dst))
#     for fn in [src, dst]:
#         try:
#             st = os.stat(fn) #判断文件是否存在,文件不存在,报异常退出
#         except OSError:
#             # File most likely does not exist
#             pass
#         else:
#             # XXX What about other special files? (sockets, devices...)
#             if stat.S_ISFIFO(st.st_mode):
#                 raise SpecialFileError("`%s` is a named pipe" % fn)
#
#     if not follow_symlinks and os.path.islink(src):#如果不拷贝连接文件的属性,并且源文件是一个链接文件,就直接拷贝连接文件
#         os.symlink(os.readlink(src), dst)
#     else:
#         with open(src, 'rb') as fsrc: #打开文件
#             with open(dst, 'wb') as fdst:
#                 copyfileobj(fsrc, fdst) #复制文件
#     return dst #返回目标文件
#######################################################################################
# 其中调用了samefile检查,我们查看下samefile源码
# normcase 忽略大小写
#os.path.normcase 这个模块

# '''
# _samefile这个函数的实现过程是如果是mac和linux系统的话就直接调用os.path.samefile模块来判断
# 而samefile函数的最终比较方法是利用stat来验证两个文件是否属性相等来比较的
# 如果不是的话就需要利用os.path.normcase模块来判断
# # normcase 忽略大小写
# #os.path.normcase 这个模块
# '''
#
# def _samefile(src, dst):
#     # Macintosh, Unix.
#     if hasattr(os.path, 'samefile'):
#         try:
#             return os.path.samefile(src, dst)
#         except OSError:
#             return False
#
#     # All other platforms: check for same pathname.
#     return (os.path.normcase(os.path.abspath(src)) ==
#             os.path.normcase(os.path.abspath(dst)))

#######################################################################################
#查看其中normcase的源代码
#normcase的实现原理就是,把目标路径实例化为bytes,
# 并把/替换为\\ 做lower处理把目录的字母都变成小写
# def normcase(s):
#     """Normalize case of pathname.
#
#     Makes all characters lowercase and all slashes into backslashes."""
#     s = os.fspath(s)
#     try:
#         if isinstance(s, bytes):
#             return s.replace(b'/', b'\\').lower()
#         else:
#             return s.replace('/', '\\').lower()
#     except (TypeError, AttributeError):
#         if not isinstance(s, (bytes, str)):
#             raise TypeError("normcase() argument must be str or bytes, "
#                             "not %r" % s.__class__.__name__) from None
#         raise


#######################################################################################
# #3.利用shutil.copymode和copystat来拷贝文件的权限,但是这个只能在linux下面使用
# 这个就只能从linux下面复制过来了
######################################################################################
# #查看 fopymode的源码
# '''
# 他的实现原理就是把元和目标文件的属性船体给chmod_func函数,通过这个函数
# 把源函数的属性赋给目标文件
# '''
# def copymode(src, dst, *, follow_symlinks=True):
#     if not follow_symlinks and os.path.islink(src) and os.path.islink(dst):
#         if hasattr(os, 'lchmod'):
#             stat_func, chmod_func = os.lstat, os.lchmod
#         else:
#             return
#     elif hasattr(os, 'chmod'):
#         stat_func, chmod_func = os.stat, os.chmod
#     else:
#         return
#
#     st = stat_func(src)
#     chmod_func(dst, stat.S_IMODE(st.st_mode))

'''
In [1]: from os import stat

In [2]: from shutil import copystat,copymode

In [3]: ls
a.sh  test*  test2*

In [4]: #查看当前文件属性

In [5]: ls -l
total 0
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test*
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test2*

In [6]: chmod 600 test2
  File "<ipython-input-6-4d4bbf067866>", line 1
    chmod 600 test2
            ^
SyntaxError: invalid syntax


In [7]: !chmod 600 test2

In [8]: ls -l
total 0
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test*
-rw-------. 1 root root 0 Apr 28 20:09 test2

In [9]: #利用copymode 修改文件属性

In [10]: copymode('test','test2')

In [11]: ls -l
total 0
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test*
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test2*

In [12]: #文件权限已经被修改了

In [13]: #利用copystat修改文件属性,但在这之前我们先删除test2文件,然后
    ...: 在做比较

In [14]: !rm  -rf test2

In [15]: !touch test2

In [16]: ls -l
total 0
-rwxrwxrwx. 1 root root 0 Apr 28 20:09 test*
-rw-r--r--. 1 root root 0 Apr 30 10:47 test2

In [17]: !stat test test2 
  File: `test'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 915715      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-28 20:09:13.189010717 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:24:26.384580870 +0800
  File: `test2'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 920966      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-30 10:47:16.584580594 +0800
Modify: 2019-04-30 10:47:16.584580594 +0800
Change: 2019-04-30 10:47:16.584580594 +0800

In [18]: #这两个文件的属性完全不相同,我们利用copystat修拷贝属性

In [19]: copystat('test','test2')

In [20]: !stat test test2 
  File: `test'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 915715      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-28 20:09:13.189010717 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:24:26.384580870 +0800
  File: `test2'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 920966      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-28 20:09:13.189010717 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:48:44.100581925 +0800

In [21]: #现在再来查看文件的所有属性都一样了(出了change这个属性我们无法改变,
应为我们每次改变这个文件的时候,这个属性都会改变,所以这个属性改变不了)

'''

#######################################################################################
# #3.利用shutil.copy和copy2来拷贝文件
######################################################################################
#查看copy的源码
# def copy(src, dst, *, follow_symlinks=True):
#     if os.path.isdir(dst):
#         dst = os.path.join(dst, os.path.basename(src))
#     copyfile(src, dst, follow_symlinks=follow_symlinks)
#     copymode(src, dst, follow_symlinks=follow_symlinks)
#     return dst
#copy的源码就是调用了copyfile和copymode这两个函数来实现文件拷贝的功能 ,
#这里的copy就只是拷贝了文件的内容和文件的权限
#在此之前我们就已经应用了copyfile和copymode这两个模块了,这里就不再解释了
##############################################
#查看copy2的源码
# def copy2(src, dst, *, follow_symlinks=True):
#     if os.path.isdir(dst):
#         dst = os.path.join(dst, os.path.basename(src))
#     copyfile(src, dst, follow_symlinks=follow_symlinks)
#     copystat(src, dst, follow_symlinks=follow_symlinks)
#     return dst

#这两个copy源码的对比我们就知道他们的差异在哪里了,
#copy2是吧文件的所有内容和所有属性都拷贝,但是copy就只是拷贝了文件的内容和权限

#使用copy拷贝文件
'''
In [23]: from shutil import copy,copy2

In [24]: copy('test','test3')
Out[24]: 'test3'

In [25]: ll
total 0
-rwxrwxrwx. 1 root 0 Apr 28 20:09 test*
-rwxrwxrwx. 1 root 0 Apr 28 20:09 test2*
-rwxrwxrwx. 1 root 0 Apr 30 10:57 test3*

In [27]: !stat test test3
  File: `test'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 915715      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-30 10:57:52.370580956 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:24:26.384580870 +0800
  File: `test3'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 922999      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-30 10:57:52.370580956 +0800
Modify: 2019-04-30 10:57:52.370580956 +0800
Change: 2019-04-30 10:57:52.370580956 +0800

'''
#使用copy2拷贝文件
'''
In [28]: copy2('test','test4')
Out[28]: 'test4'

In [29]: ll
total 0
-rwxrwxrwx. 1 root 0 Apr 28 20:09 test*
-rwxrwxrwx. 1 root 0 Apr 28 20:09 test2*
-rwxrwxrwx. 1 root 0 Apr 30 10:57 test3*
-rwxrwxrwx. 1 root 0 Apr 28 20:09 test4*

In [30]: !stat test test4
  File: `test'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 915715      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-30 10:57:52.370580956 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:24:26.384580870 +0800
  File: `test4'
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 803h/2051d	Inode: 925954      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-04-30 10:57:52.370580956 +0800
Modify: 2019-04-28 20:09:13.189010717 +0800
Change: 2019-04-30 10:59:39.923579535 +0800

'''
#这里的出的结论就和我们在上面得出的结果一般无二


#######################################################################################
# #4.利用shutil.copytree来实现多层级的拷贝文件
######################################################################################
# 查看copytree 研究他的实现原理
# names = os.listdir(src) #把源路劲下面的文件和文件下组成一个列表,给names
# if ignore is not None:
#     ignored_names = ignore(src, names) #把ignored_name变成一个可迭代对象,方便下面的遍历
                    #ignore是一个函数,需要自己编写的
# else:
#     ignored_names = set() #如果没有要被忽略的,就直接往下走
#
# os.makedirs(dst) #调用系统os.mkdirs来创建目录
# errors = []
# for name in names:
#     if name in ignored_names: #如果是忽略的文件就直接跳过
#         continue
#     srcname = os.path.join(src, name) #组成源文件的绝对路径
#     dstname = os.path.join(dst, name) #组成目标文件的绝对路径
#     try:
#         if os.path.islink(srcname): #如果源文件是一个链接文件,就读取连接的源文件做一次连接
#             linkto = os.readlink(srcname)
#             if symlinks:
#                 os.symlink(linkto, dstname) #拷贝连接文件
#                 copystat(srcname, dstname, follow_symlinks=not symlinks)
#             else:
#                 if not os.path.exists(linkto) and ignore_dangling_symlinks:
#                     continue
#                 if os.path.isdir(srcname):#如果连接文件的源文件是一个目录,就利用copy来做递归拷贝
#                     copytree(srcname, dstname, symlinks, ignore,
#                              copy_function)
#                 else:#如果不是连接的目录,也不是目录,就直接拷贝
#                     copy_function(srcname, dstname)
#         elif os.path.isdir(srcname):
#             copytree(srcname, dstname, symlinks, ignore, copy_function)
#         else:
#             copy_function(srcname, dstname)
#     except Error as err:
#         errors.extend(err.args[0])
#     except OSError as why:
#         errors.append((srcname, dstname, str(why)))
# try:
#     copystat(src, dst) #然后拷贝文件的属性
# except OSError as why:
#     # Copying file access times may fail on Windows
#     if getattr(why, 'winerror', None) is None:
#         errors.append((src, dst, str(why)))
# if errors:
#     raise Error(errors)
# return dst

# #编写ignore函数
# def ignore(src,names):
#     #忽略e开头的文件 或者其他什么条件需要我们自己去添加,自己去写条件,类似这样的函数
# #    return set(filter(lambda x:x.startwith('e'),names))
#     return {name for name in names if name.startwith('e')}


'''
In [31]: from pathlib import Path 

In [32]: p1 = Path('/data/test/a/b/c/d/e/f/e.txt')

In [33]: #创建一个目录,在目录最深处创建一个文件夹

In [35]: p1.parent.mkdir(parents = True,exist_ok = True)

In [36]: #parents = True 如果父目录不存在就创建父目录,

In [37]: #exist_ok = True 如果文件夹存在也不要给我报异常

In [38]: #下面创建文件

In [39]: with p1.open('w+') as f:
    ...:     f.write('Hello Python !')
    ...:     

In [40]: from shutil import copytree

In [41]: #测试一下copy的用法

In [42]: copytree('/data/test/a','/data/test/src')
Out[42]: '/data/test/src'

In [43]: copytree('/data/test/a','/data/src')
----------------------------------------------------------------------
FileExistsError                      Traceback (most recent call last)
<ipython-input-43-65ad5ec650bc> in <module>()
----> 1 copytree('/data/test/a','/data/src')

/usr/local/python3/lib/python3.6/shutil.py in copytree(src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks)
    313         ignored_names = set()
    314 
--> 315     os.makedirs(dst)
    316     errors = []
    317     for name in names:

/usr/local/python3/lib/python3.6/os.py in makedirs(name, mode, exist_ok)
    218             return
    219     try:
--> 220         mkdir(name, mode)
    221     except OSError:
    222         # Cannot rely on checking for EEXIST, since the operating system

FileExistsError: [Errno 17] File exists: '/data/src'

In [44]: #当我们的目标存在的时候无法使用copytree来进行拷贝


'''
#######################################################################################
# #5.利用shutil.rmtree来实现多层级的删除
######################################################################################
'''
In [46]: from shutil import rmtree

In [47]: rmtree('/data/src')

'''


















































