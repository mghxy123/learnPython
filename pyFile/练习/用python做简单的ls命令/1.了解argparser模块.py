#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.了解argparser模块.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/9 0009

import argparse
parser = argparse.ArgumentParser(description='argparser test')
parser.add_argument('a',nargs='?',default='.',help='path help')
parser.add_argument('-b')


args = parser.parse_args()
parser.print_help()
print(args)
print(args.a,args.b)


'''
description,是为了给这个文件加描述,加深使用人对这个命令的了解的
default 是为了给必须传入参数时候却没有传入时,使用默认值当做参数的
help 是为了给参数的作用加以解释
action 是为了给一些必须传入参数后面做判断使用的,如果不使用action 就会导致这个参数的返回值一直都是none,无法给后面做有效的判断

目前我们所使用的的这些选项暂时已经足够我们来编写ls的基本命令了

    运行的结果为:
        usage: 1.了解argparser模块.py [-h] [-b B] [a]
        
        argparser test
        
        positional arguments: #位置参数,也是必传参数,为了防止用户不传参数而不至于体验不好,我么可以加上默认参数,我们上面就加上了default
          a           path help
        
        optional arguments: #选项参数,既是可加,可不加的参数,其中,位置参数又分为长位置参数和短位置参数,长位置参数的末位可能后面还需要接参数,好像tar的-f一样
          -h, --help  show this help message and exit
          -b B
------------------------------------以上全是parser.print()打印出来的          
        Namespace(a='.', b=None)
        .
         
         上面中 Namespace是args
         b就是我们想要的默认参数了


'''