# -*- coding: utf-8 -*-
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

    #we can input what kind of hotel you like for searching
    searchItem = raw_input("Please input what you want to search?")
 #   searchItem = "五星级"
    print searchItem
    
    name = "hotel"
    start_urls = ["http://hotel.elong.com/search/list_cn_0101.html?Keywords="+searchItem+"&KeywordsType=999&aioIndex=-1&aioVal="+searchItem]
                
#    rules = (
#            Rule(SgmlLinkExtractor(restrict_xpaths=('/html/body/div[2]/div[5]/div[1]/div[5]/div/div[@class="h_item"]/div/div[2]/div[3]//p[@class="h_info_b1]'))
#                                   ,callback='parse_eachHotel')
#        )

    #initialize once the spider start.
    def __init__(self):
        self.browser = webdriver.Firefox()

    #done once the spider finished.
    def __del__(self):
        self.browser.close()

    #after __init__(), the spider goes from here.
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


    #the request from the parse(), will call this function.
    def parse_eachHotel(self,response):
        download_delay = 2
        #let javascript load
        self.browser.get(response.url)
        wait = WebDriverWait(self.browser,10)
 #       sel.browser.get("http://www.baidu.com")
#        wait.until(EC.presence_of_element_located(self.browser.find_element_by_class_name('htype_info_name')))
        sel = Selector(text=self.browser.page_source)
        print sel

        #since there are two different xpath for webpage.
        #so we check the first extraction from xpath
        #default is that the name in the top
        names = sel.xpath('/html/body/div[3]/div/div[1]/div[@class="hdetail_main hrela_name"]')
        data_1 = sel.xpath('/html/body/div[4]/div/div[1]/div[4]/div/div/div[@class="htype_item on"]')
        hdata_1 = sel.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div/div[@class="htype_list"]/div[@class="htype_item on"]/div[@class="htype_info_list btddd"]')
        
        #if the extraction is empty;
        if not names:
            #we used the other xpath for extracting data.
            #name in the side
           namesNew = sel.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div[@class="hrela_name left"]/div[1]')                              
           name = namesNew[0].xpath('h1/text()').extract()
           data_2 = sel.xpath('/html/body/div[4]/div/div[1]/div[1]/div[3]/div/div[@class="htype_list"]/div[@class="htype_item on"]')
           hdata_2 = sel.xpath('/html/body/div[4]/div/div[1]/div[1]/div[3]/div/div[@class="htype_list"]/div[@class="htype_item on"]/div[@class="htype_info_list"]')
           datas =  data_2
           hdatas = hdata_2
        else:
           name = names[0].xpath('div[@class="t24 yahei"]/@title').extract()
           datas = data_1
           hdatas = hdata_1
           
        items = []
        count = 0
        for data in datas:
            item = hotelItem()
            
            htype = data.xpath('div[@class="htype_info clearfix"]/div[@class="htype_info_nt"]/p[@class="htype_info_name"]/span/text()').extract()
            hprice = data.xpath('div[@class="htype_info clearfix"]/div[@class="htype_info_pb right"]/p[@class="cf55"]/span[@class="htype_info_num"]/text()').extract()
            ht_name = hdatas[count].xpath('table[@class="htype-table"]/tbody/tr/td[@class="ht_name"]/span/text()').extract()
            ht_price = hdatas[count].xpath('table[@class="htype-table"]/tbody/tr/td[@class="ht_pri"]/span[@class="ht_pri_h cur"]/span[@class="ht_pri_num"]/text()').extract()

            item["ht_name"] = ht_name
            item["ht_price"] = ht_price
            item["name"] = name
            item["htype"] = htype
            item["hprice"] = hprice
            item["link"] = 1

            count += 1
            items.append(item)
        return items
            
                          
