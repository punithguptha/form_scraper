# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FormScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsArticle(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    time=scrapy.Field()
    description=scrapy.Field()
    content=scrapy.Field()
    url=scrapy.Field()
    site=scrapy.Field()

class NewsArticleMeta(scrapy.Item):
    url=scrapy.Field()
    count=scrapy.Field()
