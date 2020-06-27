#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.csv文件处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/4 0004

'''
换行符为\r\n ,最后一行没有换行符
列分隔符为都好或制表符
每一列成为一条记录

字段可以使用双引号括起来,也可以不使用,如果字段中出现了双引号,都好,换行符号,必须使用双引号
扩起来,如果字段的值是双引号,使用两个双引号表示一个转移.
'''

from pathlib import Path

##################################################################
#1.手动方法写入csv文件
p1 = Path('test_dir/my.csv')

parent = p1.parent
if not parent.exists():
    parent.mkdir(parents=True)

csv_body = '''
id,name,age,comment
1,tom,20,"i am 20"
2,forand,18,"(""123"")"
3,ben,28,"这是
一   段
中文"
'''

with p1.open('w+') as f:
    f.write(csv_body)

##################################################################
#2.使用csv模块读取csv文件
import csv
p2 = Path('test_dir/my.csv')
with p2.open() as f :
    body = csv.reader(f)
    for line in body:
        print(line)

'''得出的结果如下:
['id', 'name', 'age', 'comment']
['1', 'tom', '20', 'i am 20']
['2', 'forand', '18', '("123")']
['3', 'ben', '28', '这是\n一   段\n中文']

'''

##################################################################
#3.使用csv模块写入csv文件
p3 = Path('test_dir/my.csv')
rows =[
['4', 'tom', '20', 'i am 20'],
['5', 'forand', '18', '(( ),"1  23","abc")'],
['6', 'ben', '28', '这是\t\n一   段\n中文']
        ]

with p3.open('a',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
