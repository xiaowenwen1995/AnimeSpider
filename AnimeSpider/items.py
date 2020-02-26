# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()         # 番剧名
    follow_num = scrapy.Field()   # 追番人数
    pub_info = scrapy.Field()     # 话
    link = scrapy.Field()         # 番剧链接
    info_link = scrapy.Field()    # 番剧简介链接
    play_num = scrapy.Field()     # 播放数
    fans_num = scrapy.Field()     # 追番人数
    review_num = scrapy.Field()   # 弹幕数量
    start_time = scrapy.Field()   # 播放时间
    score = scrapy.Field()        # 评分
    score_num = scrapy.Field()    # 评分人数
