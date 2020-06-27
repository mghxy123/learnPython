#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.ini文件处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/4 0004

'''

[DEFAULT]
a = test

[mysql]
default-character-set=utf8

[mysqld]
datadir =/dbserver/data
port = 33060
character-set-server=utf8
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

'''

'''
ini 文件中括号里面的部分称为section.译为,区,节,段
每一个section都是由一个key=value形成的键值对,key称为option选项
注意.这里的DEFAULT是缺省值section的,名字,所以必须大写

'''

import configparser
cfg = configparser.ConfigParser()
read_ok = cfg.read(['mysql.ini','php.ini','test.ini'])
#这里的read的实现原理是通过isinstance来判断文件类型,如果文件不存在自然就不存在文件类型了 ,就会直接跳过了
print(read_ok)

print(cfg.sections(),cfg.default_section)

print(cfg._sections)
#得出所有的section

for k,v in cfg.items():
    print(type(k),k,type(v),v)
print('-'*30)
for k,v in cfg.items('mysqld'):
    print(type(k),k,type(v),v)

print('-'*30)
x = cfg.get('mysqld','a') #获取a 的值
print(type(x),x)

print('-'*30)
cfg.set('mysqld','c','True')
x = cfg.get('mysqld','c') #写入c的值,这里写入的只是内存,没有写入源文件
print(type(x),x)
print('-'*30)

#写入文件,这样就可以写入文件了
with open('test.ini','w') as f:
    cfg.write(f)

print('-'*30)
#使用字典的方法去查询结果
print(cfg['mysqld'])
print(cfg['mysqld']['port'])


# print('-'*30)
# #给文件新增加一个section
# cfg.add_section('test')
# with open('test.ini','w') as f:
#     cfg.write(f)

print('-'*30) #这样就能写入新的section和值了
if cfg.has_section('test'):
    cfg.remove_section('test')
cfg['test'] = {'test1':299}
cfg['test']['test2'] = '1235'
with open('test.ini','w') as f:
    cfg.write(f)
print('-'*30)

if cfg.has_option('test','test2'):#删除option
    cfg.remove_option('test','test2')
with open('test.ini','w') as f:
    cfg.write(f)
print('-'*30)