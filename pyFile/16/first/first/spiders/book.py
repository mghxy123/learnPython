#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : book.py
# Author: HuXianyong
# Date  : 2019/8/17 9:25


import scrapy
from ..items import BookItem

from scrapy.http.response.html import HtmlResponse

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    def parse(self, response:HtmlResponse):
        print('-'*60)
        print(response.url)

        with open('test.html','w',encoding='utf-8') as f :
            f.write(response.text)

        # items = []
        #
        #
        #
        # custom_settings = {
        #     'filename': 'book.json'
        # }
        # subjects = response.text('//li[@class="subject-item"]')

        # for subject in subjects:
        #     # title = subject.xpath('.//h2/a/text()').getall()
        #     # title = subject.xpath('.//h2/a/text()').extract()
        #     title = subject.xpath('.//h2/a/text()').get()
        #     print(title)
        #     rate = subject.xpath('.//span[@class="rating_nums"]/text()').get()
        #     print(rate if rate else '0')
        #
        #     item = BookItem()
        #     item['title'] = title.strip() if title else title
        #     item['rate'] = rate if rate else '0'
        #     items.append(item)
        #     yield item
        # #
        # print('+'*60)
        # print(items)
        # return items