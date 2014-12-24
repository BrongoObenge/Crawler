__author__ = 'j'
from scrapy.contrib.spiders import CrawlSpider

class CheckTor(CrawlSpider):
    name = "checktor"
    domain_name = "torproject.org"
    start_urls = ["https://check.torproject.org/"]

    def parse(self, response):
        print "#########################"
        print response.xpath('/html/body/div[2]/h1/text()').extract()
        print response.xpath('/html/body/div[2]/p[1]').extract()
        print "#########################"
