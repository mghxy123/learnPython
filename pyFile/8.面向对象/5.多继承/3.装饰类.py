#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.装饰类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

class Document:
    def __init__(self,content):
        self.content = content

def printable(cls):
    def _print(self):
        print(self.__class__)
        print(self.content)
    cls.print = _print
    print(cls.__dict__)
    return cls

@printable #Word = printable(Word)
class Word(Document):pass

@printable
class Pdf(Document):pass

w = Word('word')
p = Pdf('pdf')
w.print()
p.print()