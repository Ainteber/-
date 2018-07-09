# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsItem(scrapy.Item):
    collections = 'ca'

    car_spec = scrapy.Field()
    car_img = scrapy.Field()
    car_detail = scrapy.Field()
    car_payment = scrapy.Field()
    car_prices = scrapy.Field()
    area = scrapy.Field()
