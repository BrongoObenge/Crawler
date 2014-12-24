__author__ = 'j'
from scrapy.contrib.spiders import CrawlSpider, Rule

class CheckIp(CrawlSpider):
    name = "checkip"
    domain_name = "myip.nl"
    start_urls = ["http://myip.nl/"]

    def parse(self, response):
        print "#########################"
        print response.xpath('//*[@id="ja-content"]/table/tr[4]/td[2]/strong/text()').extract()
        print "#########################"
