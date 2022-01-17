import scrapy
from scrapy.spiders import SitemapSpider,CrawlSpider,Rule

class LoginscraperSpider(scrapy.Spider):
    name = 'loginScraper'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/cookies/profile.php']
    # start_url="https://pythonscraping.com/linkedin/cookies/profile.php"

    #We are overriding the default make_requests_from_url method of scrapy which would be used to create the requests
    def make_requests_from_url(self, url):
        request = super(LoginscraperSpider, self).make_requests_from_url(url)
        request.cookies['username'] = 'Sai'
        request.cookies['loggedin'] = "1"
        return request

    def parse(self, response):
        return { 'text': response.body }
