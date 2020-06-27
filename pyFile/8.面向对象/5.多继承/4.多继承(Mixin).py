#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.多继承(Mixin).py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


class Document:#第三方库不允许修改
    def __init__(self,content):
        self.content = content

class Word(Document):pass #第三方库不允许修改
class Pdf(Document):pass #第三方库不允许修改

class PrintableMinxin:
    def print(self):
        print(self.content,'Mixin')

class PrintableWord(PrintableMinxin,Word):pass

pwx = PrintableWord('word test strint')
pwx.print()
print(PrintableWord.mro())
print(PrintableWord.__dict__)

#装饰器

def printable(cls):
    def _print(self):
        print(self.content)
    cls.print = _print
    print(cls.__dict__)
    return cls

@printable #Word = printable(Word)
class PrintablePdf(Document):pass
pdf = PrintablePdf('pdf test strint')
pdf.print()
print(PrintablePdf.mro())
print(PrintablePdf.__dict__)