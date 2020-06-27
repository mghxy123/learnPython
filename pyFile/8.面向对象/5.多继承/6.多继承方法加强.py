#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.多继承方法加强.py
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

class SuperPrintableMixin(PrintableMinxin):
    def print(self):
        print('~'*20) #打印增强
        super().print()
        print('*'*20) #打印增强

# PrintableMinxin 类的继承
class SuperPrintablePdf(SuperPrintableMixin,Pdf):pass

pdf = SuperPrintablePdf('pdf test strint')
pdf.print()
print(SuperPrintablePdf.mro())
print(SuperPrintablePdf.__dict__)