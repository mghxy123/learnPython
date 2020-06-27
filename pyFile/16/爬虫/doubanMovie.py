#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : doubanMovie.py
# Author: HuXianyong
# Date  : 2019/7/28 9:36

import  requests
import simplejson
import jsonpath
#热门电影
url= 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
response = requests.get(url=url,headers=head)

with response:
    text = response.text
    # print(text)
    data = simplejson.loads(text)
    print(data)
    print('#'*60)