#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/7/17 11:04
import base64

import jwt
import simplejson
from jwt.algorithms import  get_default_algorithms

SECRET_KEY = 'ytry98y89p]-0_)'

paylod = {
    'user':'hxy',
    'school':'magedu'
}
enc = jwt.encode(paylod,SECRET_KEY,algorithm='HS256')
print(enc)
header, pd, sid = enc.split(b'.')

print(header, pd, sid,sep='\n')

def addeq(b:bytes):
    l = len(b)
    r = 4-l %4
    return b + b'=' *r

'''
前两部分,显示转为byte,然后使用base64转码得出的结果输出
signature,是header和payload的HS256加密后的输出
所以payload(既是key)很重要要保存好
这jwt叫做防篡改,前面任意两个改了,就会导致签名的改变,签名就对不上了所以有防篡改功能
虽然别人知道这个是前面两个加密出的,而且还知道了加密的算法,但是它没有key也无法算出加密的签名
signature每次都是计算得出的,而不是去查表,没有存储压力
'''

print('header =',base64.urlsafe_b64decode(header))
print('payload =',base64.urlsafe_b64decode(addeq(pd)))
# print('payload =',base64.urlsafe_b64decode(pd))
newpd = base64.urlsafe_b64decode(addeq(pd))
print(simplejson.loads(newpd))

print('sid = ', base64.urlsafe_b64decode(addeq(sid)))

siginput,_,_ = enc.rpartition(b'.')
print('siginput',siginput.decode())
print(enc.decode())
print('-'*40)

alg = get_default_algorithms()['HS256']
newkey = alg.prepare_key((SECRET_KEY))
signature =alg.sign(siginput,newkey)

print(signature)

print(base64.urlsafe_b64encode(signature))
print(sid)
# jwt只是加密了签名,jwt是明文发送,jwt是防篡改的,不适合敏感信息发送
# jwt只是签名加密,但是其他的数据都是明文的

jwt.decode(enc,SECRET_KEY,)