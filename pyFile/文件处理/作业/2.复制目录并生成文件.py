# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # File  : 2.复制目录并生成文件.py
# # Author: HuXianyong
# # Mail: mghxy123@163.com
# # Date  : 2019/4/30 0030
#
# '''
# 2.复制目录
# ①/选择一个已存在的目录作为当前的工作目录,在其下创建a/b/c/d这样的子目录结构,
# 并在这些子目录的不同层级生成50个普通文件,要求这些文件名由随机4个字母构成.
# ②/将a目录下所有内容复制到当前工作目录dst目录下去,要求复制普通文件
# 名必须是x,y,z开头.
#
# 举例,假设工作目录是/tmo ,构建的目录结构是/tmp/a/b/c/d,在abcd目录中
# 放入随机生成的文件,这些文件的名称也是随机生成,.最终把a目录下的susoyou目录
# 也就是b,c,d目录,和文件名开头是x,y,x开头的文件
# '''
#
# '''
# 思路:
#     首先随机创建4-10层的目录结构
#     然后通过Path.parents()来选择进入的目录层去创建随机名的文件,
#     将a目录下的所有文件通过startwith过滤出xyz开头的文件,将他们组成一个列表
#     之后就依次把这个列表通过copytree全都拷贝到dst下面
#
#     生成文件路径一个函数,
#     随机创建文件一个函数
#     随机创建4个随机字符串一个函数
#     生成随机进入文件夹的数字一个函数
#
# '''

from random import randrange,randint,choices
from string import ascii_letters,ascii_lowercase
from os import path
import  os,glob
from pathlib import Path
from shutil import copy


base_string = ascii_letters[:26]#s生成所有的小写字母
deeps = randint(4, 10)

def random_name(): #生产四个数的文件名
    name = ''
    n = 0
    while n<4:
        letter = randint(0,25)
        # print(letter)
        name += base_string[letter]
        n += 1
    # print(name)

    #也可以使用choises来做
    # name = choices(ascii_lowercase,4)
    return name


def make_file(base_dir): #创建新文件
    file_num = 0
    asb_path = os.path.abspath(base_dir)
    print(asb_path)
    path_dir = random_dir(base_dir)
    while file_num<50: #循环50次生成文件
        name = random_name()+'.txt'
        layer = randint(0,deeps-3)
        path_deep = Path(path_dir).parents[layer]
        # print(path_deep,layer,'/'*50)
        os.chdir(path_deep)
        # print(os.getcwd())
        with open(name,'w') as f:
            f.write(name)
            # print(name)
        file_num += 1
    copy_file(asb_path)

def random_dir(base_dir): #创建文件夹
    if not path.isdir(base_dir):
        return '%s not dir'%base_dir
    path_dir = base_dir
    for deep in range(deeps): #生成目录层出
        path_dir += '/'+base_string[deep]#拼接目录
    # print(path_dir)
    Path(path_dir+'/test').parent.mkdir(parents = True,exist_ok = True)
    return  os.path.abspath(path_dir)

def copy_file(base_dir):  # 拷贝文件
    copy_list = choise_file(base_dir)
    if copy_list == []:
        exit()
    make_dir = max((len(x), x) for x in copy_list)[1]

    mpath = make_dir.replace('/a/b/', '/dst/b/')
    Path(mpath).parent.mkdir(parents=True, exist_ok=True)  # 创建新的文件夹
    # 疑惑,这里为什么不要用dirname?,用了dirname就不能创建最后一层目录

    for sfile in copy_list:
        dfile = sfile.replace('/a/b/', '/dst/b/')
        # print(dfile)
        # dst_dir = os.path.dirname(dfile)
        # print(dst_dir)
        try:
            copy(sfile, dfile)
        except Exception as f:
            print(f)

def choise_file(base_dir):  # 筛选需要拷贝的文件
    copy_list = []
    code_dir = os.path.abspath(base_dir)
    print(code_dir)
    check_dir = code_dir + '/**/*.txt'
    os.chdir(base_dir)
    print('choise',os.getcwd())
    file_list = glob.glob(check_dir, recursive=True)
    # print(file_list)
    for i in file_list:
        base_name = os.path.basename(i)
        for j in 'xyz':
            if base_name.startswith(j):
                copy_list.append(i.replace('\\', '/'))
    return copy_list



make_file('../test_dir')
#我这里吧copy_file合到了make_file里面就不会拷贝,单独执行就没问题,不知道为什么
#那是因为copy_file的时候文件目录改变了,直接传入绝对路径就好了