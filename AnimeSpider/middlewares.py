# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time


class AnimespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AnimespiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware(object):
    """
        下载器中间件
    """
    def __init__(self, timeout=50):
        self.browser = webdriver.Chrome()
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        if spider.name == "AinmeList":
            page = request.meta.get('page', 1)
            self.browser.get(request.url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.custompage')))
                input.clear()
                input.send_keys(str(page)+"\n")
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a.p.active'), str(page)))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.bangumi-title')))
            time.sleep(5)
            url = self.browser.current_url
            body = self.browser.page_source
            return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)
        elif spider.name == "AinmeLinkList":
            ainmename = request.meta.get('ainmename', 1)
            self.browser.get(request.url)
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a.media-title'), ainmename))
            time.sleep(5)
            url = self.browser.current_url
            body = self.browser.page_source
            return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)
        elif spider.name == "Ainme":
            self.browser.get(request.url)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.media-info-title-t')))
            time.sleep(5)
            url = self.browser.current_url
            body = self.browser.page_source
            return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)

