# -*- coding: utf-8 -*-
import scrapy
import json
import os
import codecs
from AnimeSpider.items import AnimespiderItem

class AinmeSpider(scrapy.Spider):
    name = 'Ainme'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://bilibili.com/']

    def start_requests(self):
        jsonpath = os.path.dirname(__file__) + '/output'
        jsonfile = codecs.open('%s/AinmeLinkList_items.json' % jsonpath, 'r', encoding='utf-8')
        for line in jsonfile:
            ainme = json.loads(line)
            url = ainme["info_link"].replace("//", "https://")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.body)
        item = AnimespiderItem()
        item["name"] = response.css(".media-info-title-t::text").get()
        item["play_num"] = response.css(".media-info-count-item-play").xpath('em/text()').get()
        item["fans_num"] = response.css(".media-info-count-item-fans").xpath('em/text()').get()
        item["review_num"] = response.css(".media-info-count-item-review").xpath('em/text()').get()
        item["start_time"] = response.css(".media-info-time").xpath('span[1]/text()').get()
        item["pub_info"] = response.css(".media-info-time").xpath('span[2]/text()').get()
        item["score"] = response.css(".media-info-score-content::text").get()
        item["score_num"] = response.css(".media-info-review-times::text").get()
        yield item
