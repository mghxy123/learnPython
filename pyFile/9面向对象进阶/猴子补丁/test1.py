#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test1.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

from test2 import Person
from test3 import get_score


def monkeypatch4Person():
    Person.get_score = get_score

monkeypatch4Person()#打补丁

if __name__ == '__main__':
    print(Person().get_score())
