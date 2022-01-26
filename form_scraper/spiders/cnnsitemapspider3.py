import scrapy
from form_scraper.items import NewsArticleMeta,NewsArticle
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule,SitemapSpider


def generateStartUrls():
    years=['2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010']
    months=['01','02','03','04','05','06','07','08','09','10','11','12']
    return ["https://www.edition.cnn.com/sitemaps/article-{}-{}.xml".format(year,month) for year in years for month in months]

class Cnnsitemapspider3Spider(SitemapSpider):
    name = 'cnnsitemapspider3'
    allowed_domains = ['cnn.com',"edition.cnn.com"]
    sitemap_urls = generateStartUrls()
    custom_settings={
        'FEED_URI':'cnnarticlesfromsitemaps2.json',
        'FEED_FORMAT':'json',
        'ITEM_PIPELINES' : {
           'form_scraper.pipelines.FormScraperPipeline': 300,
           'form_scraper.pipelines.MongoDBEntryPipeline': 600
        },
        # 'CLOSESPIDER_PAGECOUNT':10
    }

    def parse(self, response):
        newsArticle=NewsArticle()
        newsArticle["title"]=response.xpath('//h1[@class="pg-headline"]/text()').get()
        newsArticle["author"]=response.xpath("//span[@class='metadata__byline__author']/a/text()").get()
        newsArticle["time"]=response.xpath('//p[@class="update-time"]/text()').get()
        newsArticle["description"]=response.xpath('//meta[@name="description"]/@content').get()
        # Read about AND Operator in xpath tutorial for more info on below xpath query here(https://www.w3schools.com/xml/xpath_syntax.asp)
        newsArticle["content"]=response.xpath('//div[@itemprop="articleBody"]/section/div[@class="l-container"]/div[@class="zn-body__paragraph"]/text()|//div[@class="zn-body__paragraph"]/a/text()|//div[@class="zn-body__paragraph"]/text()|//p[contains(@class,"zn-body__paragraph")]/text()|//p[contains(@class,"zn-body__paragraph")]/a/text()').getall()
        newsArticle["url"]=response.url
        newsArticle["site"]="cnn"
        return newsArticle
