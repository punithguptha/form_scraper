import scrapy
from form_scraper.items import NewsArticleMeta
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

def generateStartUrls():
    years=['2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010']
    months=['01','02','03','04','05','06','07','08','09','10','11','12']
    return ["https://www.cnn.com/sitemaps/article-{}-{}.xml".format(year,month) for year in years for month in months]


class Cnnsitemapspider2Spider(scrapy.Spider):
    name = 'cnnsitemapspider2'
    allowed_domains = ['cnn.com']
    start_urls = generateStartUrls()
    custom_settings={
        'FEED_URI':'cnnarticlecount.csv',
        'FEED_FORMAT':'csv'
    }

    def parse(self, response):
        newsArticleMeta=NewsArticleMeta()
        newsArticleMeta["url"]=response.url
        newsArticleMeta["count"]=response.text.count('<url>')
        return newsArticleMeta
