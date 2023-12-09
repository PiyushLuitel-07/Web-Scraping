import scrapy

# this class inherits from Spider class that inherits from scrapy class
class QuoteSpider(scrapy.Spider):
    # name of our spider
    name='quotes'
    # we can put mulitple website in this list below
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    def parse(self,response):
        # response contains the source code of the website https://quotes.toscrape.com/ in this case
        title=response.css('title::text').extract()
        yield {'titletext':title}

