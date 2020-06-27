#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : __init__.py.py
# Author: HuXianyong
# Date  : 2019/8/17 14:43


from  flask import Flask,jsonify,Response,render_template
from .books import bpbooks

app = Flask('WEB')

app.register_blueprint(bpbooks, url_prefix='/books')

# 路由

@app.route('/')
def index():
    # return  Response('<h1>test page</h1>')
    # return  render_template('index.html',userlist=[1,2,3,4])
    return render_template('test.html')
@app.route('/json')
def jsontest():
    d = {
        'a': 10,
        'b': 'abc'
    }

    return jsonify(d)

