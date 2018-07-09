# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request
from cars import items

class CarSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['www.renrenche.com']
    start_url = 'https://www.renrenche.com/cd/ershouche/p{page}'

    def start_requests(self):
        for i in range(1, 51):
            yield Request(self.start_url.format(page=i))


    def parse(self, response):
        # print(response.body.decode('utf-8'))
        sel = Selector(response)

        #  //*[@id="search_list_wrapper"]/div/div
        lis = sel.xpath('//*[@id="search_list_wrapper"]/div/div/div[1]/ul')
        for li in lis:
            item = items.CarsItem()
            item['car_spec'] = li.xpath('//a[@class="thumbnail"]/h3/text()').extract()
            if li.xpath('//a[@class="thumbnail"]/div/img/@src').extract():
                item['car_img'] = li.xpath('//a[@class="thumbnail"]/div/img/@src').extract()
            item['car_detail'] = li.xpath('//a[@class="thumbnail"]/div[2]/span/text()').extract()
            car_price = li.xpath('//a[@class="thumbnail"]/div[4]/div/text()').extract()
            item['car_payment'] = li.xpath('//a[@class="thumbnail"]/div[4]/div/div/div/text()').extract()
            price = [i.strip()for i in car_price]
            item['car_prices'] = []
            for i in price:
                if i > '0':
                    item['car_prices'].append(i)
            item['area'] = '成都'
            yield item

            # print(car_spec, car_img, car_detail, car_prices, car_payment)

