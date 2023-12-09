import scrapy

# this class inherits from Spider class that inherits from scrapy class
class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_url=[
        'https://quotes.toscrape.com/'
    ]