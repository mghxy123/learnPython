#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/7/27 14:29
from lxml import etree
import requests

url = "https://movie.douban.com/"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

response = requests.get(url=url,headers=head)

with response:
    if response.status_code == 200:
        text = response.text
        html = etree.HTML(text)
        print(html.tag)

        x = html.xpath('//div[@class="billboard-bd"]//a/text()')
        for i in x :
            print(i)