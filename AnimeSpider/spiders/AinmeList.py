# -*- coding: utf-8 -*-
import scrapy

from AnimeSpider.items import AnimespiderItem

MAX_PAGE = 152

class AinmeListSpider(scrapy.Spider):
    name = 'AinmeList'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/anime/index/#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1']

    def start_requests(self):
        for url in self.start_urls:
            for page in range(1, MAX_PAGE + 1):
                yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        animelists = response.css(".bangumi-item")
        for animelist in animelists:
            # print(animelist.get())
            item = AnimespiderItem()
            item["name"] = animelist.css(".bangumi-title::text").get()
            item["follow_num"] = animelist.css(".shadow::text").get()
            item["pub_info"] = animelist.css(".pub-info::text").get()
            item["link"] = animelist.css(".bangumi-title").xpath('@href').get()
            yield item

