import scrapy
from ..items import QuotetutorialItem

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
        # title=response.css('title::text').extract()
        # yield {'titletext':title}

        items=QuotetutorialItem()
        all_div_quotes=response.css("div.quote")

        for quotes in all_div_quotes:
            title=quotes.css("span.text::text").extract()
            author=quotes.css(".author::text").extract()
            tag=quotes.css(".tag::text").extract()

            yield{
                'title':title,
                'author':author,
                'tag':tag
            }