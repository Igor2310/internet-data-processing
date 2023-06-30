# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies0107

    def process_item(self, item, spider):
        item['_id']=re.split("/vacancy/|[?]", item['url'])[1]
        item['salary']=[i.replace(u'\xa0', '') for i in item['salary'] if i != ' ']

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
