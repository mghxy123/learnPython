#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.抽象类方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


#实例1 不合理设计
# class Document:
#     def __init__(self,content):
#         self.content  = content
#
#     def print(self):#抽象类方法
#         raise NotImplementedError()
# class Word(Document):pass
# class Pdf(Document):pass
#
# w = Word('this word')
# w.print()

# 实例2
class Document:
    def __init__(self,content):
        self.content  = content

class Word(Document):pass
class Pdf(Document):pass

class PrintableWord(Word):
    def print(self):#抽象类方法
        print(self.content)

print(PrintableWord.__dict__)
print(PrintableWord.mro())

pw = PrintableWord('this is test word')
pw.print()