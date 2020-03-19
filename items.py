# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlmuslimuzItem(scrapy.Item):
    title = Field()
    teks = Field()
    kategori = Field()
    sumber = Field()
