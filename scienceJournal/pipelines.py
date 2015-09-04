# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import codecs
import json


class SciencejournalPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        #self.file = codecs.open('data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + '\n'
        # print line
        #self.file.write(line.decode("unicode_escape"))
        #return item
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            #self.collection.insert(dict(item))
            self.collection.update({'title': item['title']}, dict(item), upsert=True)
            log.msg("Meizi added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
