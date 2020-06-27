#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : aa.py
# Author: HuXianyong
# Date  : 2019/8/17 9:39

from scrapy.http.response.html import HtmlResponse
response = HtmlResponse('', encoding='utf-8')

with open('../test.html',encoding='utf-8') as f:
    response._set_body(f.read())


    # xpath
    subjects = response.xpath('//li[@class="subject-item"]')
    for subject in subjects:
        # title = subject.xpath('.//h2/a/text()').getall()
        # title = subject.xpath('.//h2/a/text()').extract()
        title = subject.xpath('.//h2/a/text()').get()
        print(title.strip())
        rate = subject.xpath('.//span[@class="rating_nums"]/text()').get()
        print(rate)
    # CSS
    # subjects = response.css('li.subject-item')
    # for subject in subjects:
    #     title = subject.css('h2 a::text').get()
    #     print(title)
    #     # rate = subject.css('span.rating_nums::text').get()
    #     rate = subject.css('span.rating_nums::text').re(r'^9\.\d+')
    #     print(rate)