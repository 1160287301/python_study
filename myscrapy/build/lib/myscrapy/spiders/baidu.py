# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import PropertiesItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    # def parse(self, response):
    #     """ This function parses a property page.
    #         @url http://web:9312/properties/property_000000.html
    #         @returns items 1
    #         @scrapes title price description address image_URL
    #         @scrapes url project spider server date
    #         """
    #     l = ItemLoader(item=PropertiesItem(), response=response)
    #     l.add_xpath('title', '//*[@itemprop="name"][1]/text()')
    #     l.add_xpath('price', './/*[@itemprop="price"]'
    #                          '[1]/text()', re='[,.0-9]+')
    #     l.add_xpath('description', '//*[@itemprop="description"]'
    #                                '[1]/text()')
    #     l.add_xpath('address', '//*[@itemtype='
    #                            '"http://schema.org/Place"][1]/text()')
    #     l.add_xpath('image_URL', '//*[@itemprop="image"][1]/@src')
    #     return l.load_item()
    def parse(self, response):
        return response.body
