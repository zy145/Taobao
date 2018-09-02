# -*- coding: utf-8 -*-
import scrapy

from Taobao.items import TaobaoItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']

    base_url = 'https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.2.8f1829b4HVmVmv&refpid=mm_26632258_3504122_32538762&keyword=女装&page={}'
    start_urls = [base_url.format(i) for i in range(1, 101)]

    def parse(self, response):
        node_list = response.xpath('//div[@class="item"]/a')
        for node in node_list:
            item = TaobaoItem()

            item['price'] = node.xpath('//p[@class="price"]/span[1]/strong/text()').extract_first().strip()
            item['title'] = node.xpath('//div[@class="item"]/a/div[2]/span/text()').extract_first()

            yield item

