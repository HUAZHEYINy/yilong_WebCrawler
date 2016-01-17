# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class YilongPipeline(object):
    def __init__(self):
        #open a new file, store the chinese into the new file.
        self.file = codecs.open('resultFinal.json','wb',encoding='utf-8')
        
    def process_item(self, hotelItem, hotelSpider):
        line = json.dumps(dict(hotelItem)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return hotelItem
