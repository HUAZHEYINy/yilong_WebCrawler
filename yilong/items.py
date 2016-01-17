# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import scrapy


class YilongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class hotelItem(Item):
    name = Field()
    htype = Field()
 #   ht_name = Field()
    price = Field()
    link = Field()
