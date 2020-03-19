# -*- coding: utf-8 -*-
import scrapy
from scrapy import Field, Item, Request
from scrapy.spiders import CrawlSpider, Spider


class CrawlmuslimuzItem(Item):
    title = Field()
    teks = Field()
    kategori = Field()
    sumber = Field()


class EkbisnuSpider(scrapy.Spider):
    name = 'ekbisnu'
    allowed_domains = ['nu.or.id']
    start_urls = ['http://www.nu.or.id/indeks/ekonomi-syariah/']
    

    def start_requests(self):
        urls = ['http://www.nu.or.id/indeks/ekonomi-syariah/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls= response.css('.post-item-2.border-bottom-dot a ::attr("href")').extract()
        for url in urls:
            yield response.follow(url=start_urls+url, callback=self.parse2)      
        next_page_url = response.css('.page-nav.td-pb-padding-side a ::attr("href")').extract()
        if next_page_url is not None:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)




    def parse2(self, response):
        item=CrawlmuslimuzItem()
        item['title'] = response.xpath(".//h1[contains(@class, 'entry-title')]/text()").extract()
        item['teks'] = response.xpath(".//div[contains(@class, 'pf-content')]//text()").extract()
        item['kategori'] = 'Aqidah'
        item['sumber'] = 'rumaysho.com'
       
        yield item
        #for item in zip(title,teks,kategori,sumber):
        #    scraped_info = {
        #        'title' : item[0],
        #        'teks' : item[1],
        #        'kategori' : item[2],
        #        'sumber' : item[3]
        #    }

        


