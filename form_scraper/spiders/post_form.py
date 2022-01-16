import scrapy
from scrapy.http import FormRequest

class PostFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names=["Rama","Sita","Lakshmana"]
        quests=["To learn","To serve","To help"]
        colors=["blue","white","black"]
        return [FormRequest("https://pythonscraping.com/linkedin/formAction2.php",callback=self.parse,formdata={'name':name,"quest":quest,"color":color}) for name in names for quest in quests for color in colors]

    def parse(self, response):
        return {'text' : response.xpath('//div[@class="wrapper"]/text()').get()};
