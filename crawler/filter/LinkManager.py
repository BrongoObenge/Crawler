import ConfigParser
import json
import random
from lxml import html
import requests


class ParseLinks():

    parseLinksAmount = 1
    def __init__(self):
        pass

    def parseLinks(self, linkString):
        ''' Laat het de link crawlen en dan bepalen hoeveel links er zijn'''
        print ">>>Please wait while we get all the crawling links...."
        linkArray = []
        for x in range(1, self.getAmountPages(linkString)):
            parsedLink = linkString+ str(x)
            linkArray.append(parsedLink)
        return linkArray

    def getLinks(self, configPath):
        links = []
        conf = ConfigParser.ConfigParser()
        conf.read(configPath)
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    links.append(x)
        return links

    def getCrawlLinks(self, path):
        links = []
        f = open('crawler/configs/link-config/' + path, 'r')
        for line in f:
            links.append(line.strip("\n"))
        return links

    def printDebug(self, arr):
        for x in range(len(arr)):
            print arr[x]

    def getPriceConfigDict(self, path):
        json_data = open(path)
        a = json_data.readline()
        data = json.loads(a)
        json_data.close()
        return data

    def getPriceCrawlLinks(self, path):
        dict = self.getPriceConfigDict(path)
        LinksList = []
        for key, value in dict.iteritems():
            LinksList.append(str(key))
        return LinksList

    def getEANList(self, path):
        dict = self.getPriceConfigDict(path)
        EANList = []
        for key, value in dict.iteritems():
            EANList.append(str(value))
        return EANList

    def randomDelay(self, startvalue, endvalue):
        randomValue = random.randint(startvalue,endvalue)
        return randomValue

    def getAmountPages(self, linkString):
        pages = 0
        proxies = {'http' : 'http://127.0.0.1:8123'}
        response = html.fromstring(requests.get(linkString + "1", proxies=proxies).text)
        tempStr = str(response.xpath('//*[@id="compareProductListing"]/div[2]/div[2]/span/a[3]/text()')).replace("]", "").replace("[", "").replace("\'", "")
        if (len(tempStr) == 0):
            pages = 1
        else:
            pages = int(tempStr)
        return pages
