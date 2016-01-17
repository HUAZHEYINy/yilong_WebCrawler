from scrapy.spider import Spider,Rule
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from yilong.items import hotelItem

class hotelSpider(Spider):
    name = "hotel"
    start_urls = ["http://hotel.elong.com/search/list_cn_0101.html?Keywords=%E4%BA%94%E6%98%9F%E7%BA%A7&KeywordsType=999&aioIndex=-1&aioVal=%E4%BA%94%E6%98%9F%E7%BA%A7"]

#    rules = (
#            Rule(SgmlLinkExtractor(restrict_xpaths=('/html/body/div[2]/div[5]/div[1]/div[5]/div/div[@class="h_item"]/div/div[2]/div[3]//p[@class="h_info_b1]'))
#                                   ,callback='parse_eachHotel')
#        )

    def __init__(self):
        self.browser = webdriver.Firefox()

    def __del__(self):
        self.browser.close()
    def parse(self,response):
        sel = Selector(response)
        datas = sel.xpath('/html/body/div[2]/div[5]/div[1]/div[5]/div/div[@class="h_item"]/div/div[2]/div[3]//p[@class="h_info_b1"]')
        prices = sel.xpath('/html/body/div[2]/div[5]/div[1]/div[5]/div/div[@class="h_item"]/div/div[2]/div[@class="h_info_pri"]/p/a')
        #price for each hotel they are located in different location,
        #we used another list -prices to store it and track it by count
        items = []
        
        count = 0
        for data in datas:
 #           item = hotelItem()
#            item["price"] = prices[count].xpath('span[2]/text()').extract()
#            item["name"] = data.xpath('a/text()').extract()            
            link = data.xpath('a/@href').extract()
#            item["link"] = link
#            items.append(item)
            print 'http://hotel.elong.com'+link[0],count
            #from there we extract all of the sublink from the start url
            #and pass it to a new parse function to extract the real data
            yield Request(url = 'http://hotel.elong.com'+link[0],callback= self.parse_eachHotel)
            count += 1
        #return items


            
    def parse_eachHotel(self,response):
        download_delay = 2
        self.browser.get(response.url)
        #let javascript load
  #      wait = WebDriverWait(self.browser,10)
#        wait.until(EC.presence_of_element_located(self.browser.find_element_by_class_name('htype_info_name')))
        sel = Selector(text=self.browser.page_source)
        print sel
        names = sel.xpath('/html/body/div[3]/div/div[1]/div[@class="hdetail_main hrela_name"]')
 #       names = sel.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[@class="t24 yahei c333 mb7"]')
        datas = sel.xpath('/html/body/div[4]/div/div[1]/div[4]/div/div/div[@class="htype_item on"]/div[@class="htype_info clearfix"]')
        items = []
        for data in datas:
            item = hotelItem()
 #           item["name"] = names[0].xpath('h1/text()').extract()
            item["name"] = names[0].xpath('div[1]/@title').extract()
            item["htype"] = data.xpath('div[@class="htype_info_nt"]/p[@class="htype_info_name"]/span/text()').extract()
 #           item["ht_name"]  
            item["price"] = data.xpath('div[@class="htype_info_pb right"]/p[@class="cf55"]/span[@class="htype_info_num"]/text()').extract()
            item["link"] = 1
            items.append(item)
           # print item["name"]
        return items
            
                          
