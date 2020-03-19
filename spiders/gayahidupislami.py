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
    name = 'gayahidupislami'
    allowed_domains = ['islami.co']
    start_urls = ['https://islami.co/category/budaya/']
    

    def start_requests(self):
        urls = ['https://islami.co/category/budaya/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(2,14):
            urls= response.css('.entry-title a ::attr("href")').extract()
            for url in urls:
                yield response.follow(url=url, callback=self.parse2)      
            next_page_url = 'https://islami.co/category/budaya/'
        
            next_page_url=response.urljoin(next_page_url+str(i))
            yield scrapy.Request(url=next_page_url, callback=self.parse)




    def parse2(self, response):
        item=CrawlmuslimuzItem()
        item['title'] = response.xpath(".//h1[contains(@class, 'entry-title')]/text()").extract()
        item['teks'] = response.xpath(".//div[contains(@class, 'entry-content')]//text()").extract()
        item['kategori'] = 'Gaya Hidup'
        item['sumber'] = 'islami.co'
       
        yield item
        #for item in zip(title,teks,kategori,sumber):
        #    scraped_info = {
        #        'title' : item[0],
        #        'teks' : item[1],
        #        'kategori' : item[2],
        #        'sumber' : item[3]
        #    }

        


