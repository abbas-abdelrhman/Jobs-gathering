import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "joby"
    # allowed_domains = ['https://wuzzuf.net']
    start_urls = ['http://wuzzuf.net/search/jobs/?q=python&a=hpb']

    rules = [
        Rule(LinkExtractor(allow=r'wuzzuf/((?!:).)*$'), callback='parse', follow=True)
    ]

    def parse(self, response):
        for job in response.css('div.css-pkv5jc'):
            yield {
                'JOB-TITLE': job.css('h2.css-m604qf a.css-o171kl::text').get(),
                'COMPANY': job.css('div.css-d7j1kk a.css-17s97q8::text').get(),
                'LOCATION': job.css('div.css-d7j1kk span.css-5wys0k::text').get(),
                'LINK': job.css('a.css-o171kl::attr(href)').get(),

            }

