# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re
from pymongo import MongoClient
import urllib as url
from scrapy.utils.project import get_project_settings

settings= get_project_settings()

#We clean the data in this pipeline by removing unwanted entries and by making the content array to a plain string which comprises of whole content
class FormScraperPipeline:
    def process_item(self,newsArticle,spider):
        if not newsArticle["author"]:
            raise DropItem("Missing author info...")
        if not newsArticle["content"]:
            raise DropItem("Missing content...")
        if not newsArticle["description"]:
            raise DropItem("Missing description...")
        newsArticle["description"]=newsArticle["description"].replace('"','')
        newsArticle["description"]=newsArticle["description"].strip()
        newsArticle["description"]=re.sub(' +',' ',newsArticle["description"])
        contentString=""
        for text in newsArticle["content"]:
            contentString+=text.replace('"','')
        newsArticle["content"]=contentString.strip()
        newsArticle["content"]=re.sub(' +',' ',newsArticle["content"])
        return newsArticle

#We use this pipeline to enter the processed details from above pipeline to our MongoDB
class MongoDBEntryPipeline:
    def __init__(self):
        conn = MongoClient(
            settings.get('MONGO_HOST'),
            settings.get('MONGO_PORT')
        )
        db = conn[settings.get('MONGO_DB_NAME')]
        self.collection = db[settings['MONGO_COLLECTION_NAME']]

    def process_item(self,newsArticle,spider):
        self.collection.insert_one(dict(newsArticle))
        return newsArticle
