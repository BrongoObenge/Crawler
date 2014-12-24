import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.dbmanager import MySqlManager
from crawler.filter import TorManager

class PriceSpider(scrapy.Spider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = " "                          #Name to craw, gets used to get the start_urls[]
    pathName = None                     #Used to get ConfigFile
    arrEanIdentifier = None             #Used to identify the EAN in the Config dict class
    relation = None                     #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = None
    filteredDict = {}
    arrEan = []
    y = -1                              #Used to iterate trough the arrEan[]
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        self.altParse(response)

    def altParse(self, response):
        '''
        Parses the crawled data.
        Gets data and puts them in the Databases with their relations.
        :param response: Response from Scrapy spider
        :return: None
        '''
        mysqlManager = MySqlManager.MySqlManager()                          #initiates connection
        db = mysqlManager.openDb()                                          #initiates connection

        timestamp = mysqlManager.getTimestamp()                             #Gets the timestamp
        self.y += 1                                                         #Needed to iterate trough the EAN array
        nodeDict = dict()                                                   #Makes a dictionary for the node

        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths

        for x in listCrawl:                                                             #Iterates through the Rows that are in the config and extracts data
            tempDict = configManager.getxPathPriceCrawler(x, self.path)
            nodeDict["xpathshopname"] = response.xpath(str(tempDict['xpathshopname']% x)).extract()
            nodeDict["xpathshopscore"] = response.xpath(str(tempDict['xpathshopscore']% x)).extract()
            nodeDict["xpathdelivery"] = response.xpath(str(tempDict['xpathdelivery']% x)).extract()
            nodeDict["xpathbareprice"] = response.xpath(str(tempDict['xpathbareprice']% x)).extract()
            nodeDict["xpathshopprice"] = response.xpath(str(tempDict['xpathshopprice']% x)).extract()
            nodeDict["xpathclickout"] = response.xpath(str(tempDict['xpathclickout']% x)).extract()
            nodeDict["EAN"] = self.arrEan[self.y]

            if filter.FilterDict().checkEmptyDicts(nodeDict) == True:
                pass
            else:
                self.filteredDict = filter.FilterDict().filterPriceDict(nodeDict)
                mysqlManager.insertPrice(db, str(self.filteredDict["EAN"]), str(self.filteredDict["xpathshopname"]), str(self.filteredDict["xpathdelivery"]), str(self.filteredDict["xpathbareprice"]), str(self.filteredDict["xpathshopprice"]), str(self.filteredDict["xpathclickout"]), timestamp)
        torMan = TorManager.TorManager()
        if not(torMan.newId()):
            torMan.newId()
        torMan.forceNewId()
        print str(self.y)+"/"+str(len(self.start_urls))+" Done."
