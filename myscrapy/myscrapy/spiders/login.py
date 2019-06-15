# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['ww']
    start_urls = ['http://ww/']

    def start_requests(self):
        return [
    FormRequest(
      "http://web:9312/dynamic/login",
      formdata={"user": "user", "pass": "pass"}
         )]

    def parse(self, response):
        pass
