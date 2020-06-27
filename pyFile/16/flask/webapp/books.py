#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : books.py
# Author: HuXianyong
# Date  : 2019/8/17 14:58


from flask import Blueprint,jsonify

bpbooks = Blueprint('booksapp',__name__,url_prefix='/sss')

@bpbooks.route('/', methods = ['GET', 'POST'])
def getall():
    books = [
        (1,'java',20),
        (2,'linux',30),
        (3,'python',40)
    ]
    return jsonify(books)

print('-'*60)

for x in bpbooks.__dict__.items():
    print(x)