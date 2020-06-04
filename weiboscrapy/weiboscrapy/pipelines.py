# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 项目管道(Pipeline):
# 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。
# 当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

from scrapy.exceptions import DropItem

class WeiboscrapyPipeline(object):

    def __init__(self):
        self.address_seen = set()

    def process_item(self, item, spider):
        # 重复过滤
        if item['address'] in self.address_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.address_seen.add(item['address'])

        # 使用save把item存入到了数据库
        item.save()
        return item
