import scrapy


def generateStartUrls():
    names=["Rama","Sita","Lakshmana"]
    quests=["To learn","To serve","To help"]
    colors=["blue","white","black"]
    return ["https://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color={}".format(name,quest,color) for name in names for quest in quests for color in colors]

class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generateStartUrls();

    def parse(self, response):
        return {'text' : response.xpath('//div[@class="wrapper"]/text()').get()};
