#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/8/10 16:35

# r模式
f = open('test') # 默认是只读打开文件
f.read()
# f.write('this is test file') # 默认是只读的，无法写入文件
f.close()

f = open('test', 'r') # 只读
# f.write('abc') # 只读无法写入文件
f.close()

# f = open('test1', 'r') #文件不存在会报错


# w模式
f = open('test', 'w') # 只写打开
f.write('this is test file')
# f.read() # 只写模式无法读取数据
f.close()

print('*'*60)
f = open('test') # 查看文件内容
content = f.read()
print(content)
f.close()

f = open('test', 'w') # 用写方式打开文件没有追加内容会清空文件
f.close()

f = open('test') # 查看文件内容,文件为空
content = f.read()
print(content)
f.close()