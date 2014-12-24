import socket
import random
import os
from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from crawler import settings
import urllib2
from crawler.filter import TorManager

class ProxyMiddleware(object):
    socket.setdefaulttimeout(50)
    proxyList = [
                "111.197.160.96",
                "119.6.144.70:80",
                "119.6.144.74:80",
                "119.6.144.70:81",
                "203.144.144.162:8080",
                "77.120.102.5:8080",
                "85.104.56.185:8080",
                "202.29.97.5:3128",
                "88.255.148.24:8080"
    ]

    def process_request(self, request, spider):
        print ">>>Selecting proxy....."
        proxy = self.checkWorkingSingleProxy(self.proxyList)
        if proxy == None:
            proxy = self.checkWorkingSingleProxy(self.proxyList)
        request.meta['proxy'] = "http://"+proxy+"/"
        print ">>>Selected proxy: "+proxy

    def checkWorkingSingleProxy(self, proxyList):
        randomNumber = random.randint(0,len(proxyList)-1)
        item = proxyList[randomNumber]
        if self.is_bad_proxy(item):
            print "Bad Proxy", item
            item = self.checkWorkingSingleProxy(proxyList)
        else:
            return item

    def is_bad_proxy(self, pip):
        try:
            proxy_handler = urllib2.ProxyHandler({'http': pip})
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib2.install_opener(opener)
            req=urllib2.Request('http://tweakers.net/pricewatch/352536/kingston-kta-mb1600s-4g/specificaties/')  # change the url address here
            sock=urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print 'Error code: ', e.code
            return e.code
        except Exception, detail:
            print "ERROR:", detail
            return 1
        return 0

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)

class TorProxyMiddleware(object):
    torMan = TorManager.TorManager()
    if not(torMan.newId()):
        torMan.newId()
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.HTTP_PROXY

class RetryMiddlewareTor(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status in [str(403)]:
            print ">>>exec \'killall -HUP tor\'"
            os.system("killall -HUP tor")
        return response