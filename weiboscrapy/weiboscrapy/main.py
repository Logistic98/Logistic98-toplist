"""定时执行Scrapy爬虫"""

import time
import os

while True:
    os.system("scrapy crawl Weibolog")
    time.sleep(86400)  #每隔一天运行一次 24*60*60=86400s

