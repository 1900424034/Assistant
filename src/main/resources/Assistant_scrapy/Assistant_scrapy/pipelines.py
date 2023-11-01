# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AssistantScrapyPipeline(object):
    def process_item(self, item, spider):
        host = '127.0.0.1'
        port = 27017
        db_name = 'test_1'
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        collections = db['collage']
        collections.insert_one(dict(item))
        return item

# class CollegePipeline:
#     def process_item(self, item, spider):
#         host = '127.0.0.1'
#         port = 27017
#         db_name = 'test_1'
#         client = pymongo.MongoClient(host=host, port=port)
#         db = client[db_name]
#         collections = db['collage']
#         collections.insert_one(dict(item))
#         return item