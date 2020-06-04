# -*- coding: utf-8 -*-

import json,re,scrapy
from scrapy.spiders import CrawlSpider
from weiboscrapy.items import WeiboscrapyItem

class WeibologSpider(CrawlSpider):
    name = 'Weibolog'
    aallowed_domains = ['weibo.com']
    offset = 0
    base_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=1760&page={0}&lefnav=0&cursor=&__rnd=1556799484815"
    start_urls = [base_url.format(offset)]

    def parse(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile(
                '<div.*?list_title_b.*?<a href="(.*?)".*?_blank">(.*?)</a>.*?subinfo S_txt2">(.*?)</span></a>.*?'
                + 'S_txt2">(.*?)</span>.*?praised S_ficon W_f16">ñ</em><em>(.*?)</em>.*?ficon_'
                + 'repeat S_ficon W_f16">.*?</em><em>(.*?)</em>.*?forward S_ficon W_f16.*?</em><em>'
                + '(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = WeiboscrapyItem()
                item['content'] = info[1]
                item['author'] = info[2]
                item['publishTime'] = info[3]
                item['repost'] = info[4]
                item['comment'] = info[5]
                item['approve'] = info[6]
                item['address'] = info[0]
                yield item

            if self.offset < 30:
                self.offset += 1
                url = self.base_url.format(self.offset)
                yield scrapy.Request(url, callback=self.parse)
