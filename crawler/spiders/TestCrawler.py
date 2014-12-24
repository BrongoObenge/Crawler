__author__ = 'j'
import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.dbmanager import Neo4jDatabaseManager
from py2neo import rel, node
import time
import json


class TestSpider(scrapy.Spider):
    '''
    Class is used to test features

    Match the EAN ->   MATCH (n) WHERE n.EAN =~ ".*0672042093809(EAN NUMBER).*" RETURN n;
    '''
    name = "TESTcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "PERIPHERALS"        #Name of the Label that needs to be added to the Crawled Node
    label2 = "TEST"        #Name of the Label that needs to be added to the Crawled Node

    pathName = "TESTpath"        #Used to get ConfigFile
    relation = "TEST"            #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    filteredDict = {}

    countUrl = 0
    urlEanDict = {}

    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        '''
        Parses the crawled data.
        Puts data in a Dict. Filters Dict. Creates Node. Adds label. Creates Relationships.
        :param response: Response from Scrapy spider
        :return: None
        '''
        self.parseSource(response)

    def parseSource(self, response):
        print "== Initializing =="
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()               #initiates connection
        graph_db = conn.openDb()                                            #initiates connection

        nodeDict = dict()                                                   #Makes a dictionary for the node

        baseNode = conn.getNode(graph_db, self.label)                       #Gets the BaseNode from the database
        baseNode.get_properties()                                           #Need to ask for properties to use the BaseNode (Workaround)
        baseNode.get_labels()                                               #Need to ask for labels to use the BaseNode (Workaround)

        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths
                #Shows how many Sections are found in the Config.

        for x in listCrawl:
            key = response.xpath(configManager.getKeyxPath(x, self.path) % x).extract()         #Gets the key from the source. xPath is from the config.
            value= response.xpath(configManager.getValuexPath(x, self.path) % x ).extract()     #Gets the value from the source. xPath is from the config.
            nodeDict.update({str(key): str(value)})                                             #Adds Key:Value to the dict.
        self.filteredDict = filter.FilterDict().filterDictionary(nodeDict)                      #Filters the dict on empty values, '/xa0s' values and unicode.


        print "================================"

        '''
        Checks if EAN exists
        '''
        eanInDict = False
        TestEan = None
        if self.filteredDict.get("EAN", 0) == 0:    #If the EAN does not exist in Dict, it returns 0
            print "NO EAN"
            eanInDict = False
        else:                                       #If EAN exists it goes into this thing
            eanInDict = True
            TestEan = self.filteredDict['EAN']
            print conn.findNodeByEAN(graph_db, TestEan)

        if conn.findNodeByEAN(graph_db, TestEan) == False and eanInDict == True:    #Checks if EAN is in Dict and if EAN does not exist in DB
            print "Creating node"
            crawlNode, = graph_db.create(self.filteredDict)                         #Creates Node.
            crawlNode.add_labels(str(self.label))                                   #Adds label to the Node.
            graph_db.create(rel(crawlNode, self.relation, baseNode))                #Creates Relationship.
        else:
            print "Node exists, skipping"
        print "================================"

        self.urlEanDict[self.start_urls[self.countUrl]] =  self.filteredDict['EAN'] #adds stuff to dict
        self.countUrl += 1
        if len(self.start_urls)-1 == self.countUrl:                                 #at the end of the crawling process writes to file
            with open('crawler/price-config/'+self.label2+'.json', 'wb') as fp:
                json.dump(self.urlEanDict, fp)
                print "\tWritten to Json"
        print 'crawler/price-config/'+self.label2+'.json'
        print "== Done :) =="



