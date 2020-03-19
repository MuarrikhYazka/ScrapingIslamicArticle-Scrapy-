# -*- coding: utf-8 -*-
import scrapy
from scrapy import Field, Item, Request
from scrapy.spiders import CrawlSpider, Spider


class CrawlmuslimuzItem(Item):
    title = Field()
    teks = Field()
    kategori = Field()
    sumber = Field()


class AqidahrumayshoSpider(scrapy.Spider):
    name = 'fiqihrumaysho'
    allowed_domains = ['rumaysho.com']
    start_urls = ['https://rumaysho.com/category/hukum-islam']
    

    def start_requests(self):
        urls = ['https://rumaysho.com/category/hukum-islam']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(2,80):
            urls= response.css('.entry-title.td-module-title a ::attr("href")').extract()
            for url in urls:
                yield response.follow(url=url, callback=self.parse2)      
            next_page_url = 'https://rumaysho.com/category/hukum-islam/page/'
        
            next_page_url=response.urljoin(next_page_url+str(i))
            yield scrapy.Request(url=next_page_url, callback=self.parse)




    def parse2(self, response):
        item=CrawlmuslimuzItem()
        item['title'] = response.xpath(".//h1[contains(@class, 'entry-title')]/text()").extract()
        item['teks'] = response.xpath(".//div[contains(@class, 'pf-content')]//p/text()").extract()
        item['kategori'] = 'Fiqih'
        item['sumber'] = 'rumaysho.com'
       
        yield item
        #for item in zip(title,teks,kategori,sumber):
        #    scraped_info = {
        #        'title' : item[0],
        #        'teks' : item[1],
        #        'kategori' : item[2],
        #        'sumber' : item[3]
        #    }

        


