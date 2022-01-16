import scrapy
from scrapy.spiders import SitemapSpider,CrawlSpider
from form_scraper.items import NewsArticle

class CnnsitemapspiderSpider(scrapy.Spider):
    name = 'cnnsitemapspider'
    allowed_domains = ['edition.cnn.com']
    # start_urls = ['https://edition.cnn.com/2022/01/15/asia/tsunami-warning-tonga-volcano-intl-hnk/index.html']
    start_urls=['https://edition.cnn.com/2019/10/11/sport/gallery/simone-biles/index.html']
    # sitemap_urls=['https://edition.cnn.com/sitemaps/cnn/index.xml']
    custom_settings={
        'FEED_URI':'cnnarticles3.json',
        'FEED_FORMAT':'json',
        'CLOSESPIDER_PAGECOUNT':100
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
