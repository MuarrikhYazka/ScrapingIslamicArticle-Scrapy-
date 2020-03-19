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
    name = 'ekbissharia1'
    allowed_domains = ['sharianews.com']
    start_urls = ['https://sharianews.com/category/keuangan']
    

    def start_requests(self):
        urls = ['https://sharianews.com/category/keuangan']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(2,82):
            urls= response.css('.col-md-8 a ::attr("href")').extract()
            for url in urls:
                yield response.follow(url=url, callback=self.parse2)      
            next_page_url = 'https://sharianews.com/category/keuangan?page='
        
            next_page_url=response.urljoin(next_page_url+str(i))
            yield scrapy.Request(url=next_page_url, callback=self.parse)




    def parse2(self, response):
        item=CrawlmuslimuzItem()
        item['title'] = response.xpath(".//div[contains(@class, '__space')]/h2[contains(@class, '__head_title')]/a/text()").extract()
        item['teks'] = response.xpath(".//div[contains(@class, '__space')]/div[contains(@class, '__content')]//p/text()").extract()
        item['kategori'] = 'Ekonomi Bisnis'
        item['sumber'] = 'sharianews.com'

        #item['title'] = item['title'].replace('\t', '')
        #item['title'] = item['title'].replace('\n', '')
        #item['teks'] = item['teks'].replace('\t', '')
        #item['teks'] = item['teks'].replace('\n', '')
       
        yield item
        #for item in zip(title,teks,kategori,sumber):
        #    scraped_info = {
        #        'title' : item[0],
        #        'teks' : item[1],
        #        'kategori' : item[2],
        #        'sumber' : item[3]
        #    }

        


