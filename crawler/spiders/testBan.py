__author__ = 'j'
from scrapy.contrib.spiders import CrawlSpider
class testBan(CrawlSpider):
    name = "checkban"
    domain_name = "torproject.org"
    start_urls = ["http://tweakers.net/pricewatch/324186/samsung-se-208db-zwart/specificaties/"]

    def parse(self, response):
        print "#########################"
        print response.xpath('/html/body').extract()
        print "#########################"

