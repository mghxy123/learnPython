#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : auth认证.py
# Author: HuXianyong
# Date  : 2019/7/19 16:34

from django.http  import HttpRequest,HttpResponse
import jwt
from .user.models import User
from blog import settings

AUTH_HEADER='aaaa'

# 认证装饰器 传入一个视图函数
def authenticate(viewfunc):
    def wrapper(request:HttpRequest):
        # Code to executed for each request befor
        # the view (and later middlewar) are called
        print(1,'-'*40)
        # 认证,越早越好
        jwtheader = request.META.get(AUTH_HEADER,'')
        print(jwtheader)
        if not jwtheader:
            return HttpResponse(status=401)
        print(jwtheader)

        try:
            payload = jwt.decode(jwtheader,settings.SECRET_KEY,algorithms=['HS256'])
            print(payload)
        except Exception as e:
            print(e)
            return HttpResponse({'error':e},status=401)

        print('-'*40)
        try:
            user_id = payload.get('user_id',0)
            if user_id == 0:
                return HttpResponse(status=401)
            user = User.objects.get(pk=user_id)
            request.user = user
        except Exception as e:
            print(e)
            return HttpResponse(status=401)

        response = viewfunc(request)
        return response
    return wrapper