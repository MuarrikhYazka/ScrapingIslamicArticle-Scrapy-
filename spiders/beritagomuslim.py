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
    name = 'beritagomuslim'
    allowed_domains = ['gomuslim.co.id']
    start_urls = ['https://www.gomuslim.co.id/news']
    

    def start_requests(self):
        urls = ['https://www.gomuslim.co.id/news']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(2,857):
            urls= response.css('.entry-title > a ::attr("href")').extract()
            for url in urls:
                yield response.follow(url=url, callback=self.parse2)      
            next_page_url = 'https://www.gomuslim.co.id/news/'
        
            next_page_url=response.urljoin(next_page_url+str(i))
            yield scrapy.Request(url=next_page_url, callback=self.parse)




    def parse2(self, response):
        item=CrawlmuslimuzItem()
        item['title'] = response.xpath(".//div[contains(@class, 'details-news')]/div[contains(@class, 'post')]/div[contains(@class, 'post-content')]/h2[contains(@class, 'entry-title')]/p[1]/text()").extract()
        response.css(".details-news > .post > .post-content > .entry-title > p::text")
        item['teks'] = response.xpath(".//div[contains(@class, 'entry-content')][1]/text()").extract()
        item['kategori'] = 'Berita'
        item['sumber'] = 'gomuslim.co.id'

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

        


