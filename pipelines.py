# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class QuotettutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb://SALT:Salt1234@cluster0-shard-00-00-s8mjc.azure.mongodb.net:27017,cluster0-shard-00-01-s8mjc.azure.mongodb.net:27017,cluster0-shard-00-02-s8mjc.azure.mongodb.net:27017/Salt_words?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
        db = self.conn['myquote']
        self.collection = db['quote_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item