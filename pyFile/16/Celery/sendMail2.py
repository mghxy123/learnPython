#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : sendMail2.py
# Author: HuXianyong
# Date  : 2019/7/26 14:15


from lxml import etree

root = etree.Element('html')
print(root)
print(type(root))
print(root.tag)

body = etree.Element('body')
root.append(body)
print(etree.tostring(root))

etree.SubElement(body,'child1')
etree.SubElement(body,'child2').append(etree.Element('child20'))

print(etree.tostring(root))

print('2'*80)

text = etree.tostring(root,pretty_print=True).decode()
html = etree.HTML(text)
print(html.tag)

print(html)
x = html.xpath('//*[starts-with(local-name(), "child")]')
print(x)