# -*- coding: utf-8 -*-
import scrapy
import json
import os
import codecs
from AnimeSpider.items import AnimespiderItem


class AinmelinklistSpider(scrapy.Spider):
    name = 'AinmeLinkList'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://bilibili.com/']

    def start_requests(self):
        jsonpath = os.path.dirname(__file__) + '/output'
        jsonfile = codecs.open('%s/AinmeList_items.json' % jsonpath, 'r', encoding='utf-8')
        for line in jsonfile:
            ainme = json.loads(line)
            ainmename = ainme["name"]
            url = ainme["link"].replace("//", "https://")
            yield scrapy.Request(url=url, callback=self.parse, meta={'ainmename': ainmename})

    def parse(self, response):
        item = AnimespiderItem()
        item["info_link"] = response.css(".media-title").xpath('@href').get()
        yield item
