#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.多线程出错代码.py
# Author: HuXianyong
# Date  : 2019/7/7 10:58

import threading
import time
import random
import logging
FROMAT = '%(asctime)s %(name)s [%(message)s]'
logging.basicConfig(level=logging.INFO, format=FROMAT)

global_dict = {}

def additem(d:dict):
    count = 1
    while True:
        d[count] = random.randint(10,20) # kv一直增加
        count += 1
        time.sleep(0.001)

def iterdict(d:dict):
    while True:
        for k,v in d.items(): #遍历
            logging.info(k,v)
            d[k] = random.randint(1,10)

a = threading.Thread(target=additem,args=(global_dict,),daemon=True)
i = threading.Thread(target=iterdict,args=(global_dict,),daemon=True)

a.start()
i.start()
while True:
    time.sleep(1)
    logging.info(threading.enumerate())

    if threading.active_count() < 3:
        keys = list(global_dict.keys())
        logging.info(keys)
        print('============end=============')

        break

