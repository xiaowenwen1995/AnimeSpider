# -*- coding: utf-8 -*- 
"""
@project: AnimeSpider
@Author: xiaowenwen 
@time: 2020/2/26 17:02
@desc:
"""

from scrapy import cmdline

cmdline.execute(["scrapy", "crawl", "AinmeList"])      # 获取番剧列表
cmdline.execute(["scrapy", "crawl", "AinmeLinkList"])  # 获取番剧介绍页链接
cmdline.execute(["scrapy", "crawl", "Ainme"])          # 获取番剧详细信息
