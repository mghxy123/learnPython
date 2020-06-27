#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : __init__.py.py
# Author: HuXianyong
# Date  : 2019/7/19 21:20


def jsonify(instance, allow=None, exclude = []):
    # all优先,如果有,就使用allow指定的字段,这时候exclude无效
    # allow如果为空,那就是全体,但是要看看exclude重要排除的
    modelcls = type(instance)
    print('+'*100)
    if allow:
        fn = (lambda x: x.name in allow)
    else:
        fn = (lambda x: x.name not in exclude)

    print({k.name:getattr(instance, k.name) for k in filter(fn, modelcls._meta.fields)})

    return {k.name:getattr(instance, k.name) for k in filter(fn, modelcls._meta.fields)}
