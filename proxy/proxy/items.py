# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #爬虫十分简单，要ip+端口，所以一个字段就够用了
    ip = scrapy.Field()
    addr = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    protocol = scrapy.Field()
    source = scrapy.Field()
