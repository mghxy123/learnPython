# -*- coding: utf-8 -*-
import scrapy
# from
from scrapy.http import HtmlResponse


class BookSpider(scrapy.Spider):
    name = 'dbbook'
    allowed_domains = ['douban.com']
    url = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
    start_urls =[url]
    # https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=40&type=T
    def parse(self, response:HtmlResponse):
        print(type(response),'11111111111111111111')
        print(response.url)
        print(response.encoding)
        print(type(response.body))
        titles = response.css('li.subject-item')
        print(titles)
