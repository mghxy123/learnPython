# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookItem

class DbbookSpider(CrawlSpider):
    name = 'dbbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B']

    # url 提取, 生成request对象,start_url不作处理,只提取allow的url,然后调用回调函数parse_item函数,开始处理
    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print('parse_item++++++++++++++++++')
        subjects = response.xpath('//li[@class="subject-item"]')

        for subject in subjects:
            # title = subject.xpath('.//h2/a/text()').getall()
            # title = subject.xpath('.//h2/a/text()').extract()
            title = subject.xpath('.//h2/a/text()').get()
            print(title)
            rate = subject.xpath('.//span[@class="rating_nums"]/text()').get()
            print(rate if rate else '0')

            item = BookItem()
            item['title'] = title.strip() if title else title
            item['rate'] = rate if rate else '0'
            yield item