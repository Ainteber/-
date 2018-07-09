# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from cars import settings
from cars.items import CarsItem

class CarsPipeline(object):

    def process_item(self, item, spider):
        return item

class PymongoCarsPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(host=settings.MONGODB_HOST,
                                         port=settings.MONGODB_PORT)
        db = connection[settings.MONGODB_DB]
        self.collection = db[CarsItem.collections]

    def process_item(self, item, spider):
        if isinstance(item, CarsItem):
            self.collection.insert(dict(item))
            return item
