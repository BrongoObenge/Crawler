import crawler.filter.LinkManager as man
# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
#DOWNLOAD_DELAY = man.ParseLinks().randomDelay(1,15)          #Proxy delay is already 3 seconds, not needed
COOKIES_ENABLED = False

# Retry many times since proxies often fail
RETRY_TIMES = 350
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 404, 403, 408]

#LOG_LEVEL = "INFO"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'




##########TEST#############
# DOWNLOADER_MIDDLEWARE = {
#                          'crawler.middlewares.RetryChangeProxyMiddleware': 600,
#                          }
#



##TOR##
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
HTTP_PROXY = 'http://127.0.0.1:8123'
DOWNLOADER_MIDDLEWARES = {
         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
         'crawler.middlewares.RetryMiddlewareTor': 100,
         'crawler.middlewares.RandomUserAgentMiddleware': 200,
         'crawler.middlewares.TorProxyMiddleware': 300,



    # Disable compression middleware, so the actual HTML pages are cached
}

##########TEST#############
##Proxy##
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'crawler.middlewares.ProxyMiddleware': 100,
# }
