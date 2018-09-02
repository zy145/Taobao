# -*- coding: utf-8 -*-

import time

from retrying import retry
from selenium import webdriver

from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def __init__(self):

        self.driver = webdriver.Chrome()


    @retry(stop_max_attempt_number=20, wait_fixed=200)
    def retry_load_page(self, reqeust, spider):
        try:
            # 如果这里出现异常则交给try捕获，那么retry则不会工作，所以在except需要主动raise 一个异常
            self.driver.find_element_by_xpath('//*[@id="J_topsearch"]/div/div/div[2]/span')
        except:
            spider.logger.info("Retry <{}> page ({} times)".format(reqeust.url, self.count))
            self.count += 1
            # 手动抛出异常交给retry捕获，如果retry重试20次后，则该异常交到上一级方法的try捕获
            raise Exception("<{}> page load failed".format(reqeust.url))

    def process_request(self, request, spider):
        #if "php" in reqeust.url:

        self.count = 1
        #driver = webdriver.Chrome()
        self.driver.get(request.url)

        try:
            #time.sleep(5)
            self.retry_load_page(request, spider)
            html = self.driver.page_source
            # 返回自定义的响应对象给引擎，引擎判断是一个response对象，交给spider解析处理。则request不再交给下载器。
            return HtmlResponse(url=self.driver.current_url, body=html.encode("utf-8"), encoding="utf-8", request=request)
        except Exception as e:
            spider.logger.error(e)


    def __del__(self):
        self.driver.quit()
