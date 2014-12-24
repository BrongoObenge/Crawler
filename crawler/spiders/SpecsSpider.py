import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.dbmanager import Neo4jDatabaseManager
from py2neo import rel, node
import json
from crawler.dbmanager.MongoDbManager import MongoDbManager
from crawler.filter import TorManager

class SpecsSpider(scrapy.Spider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = None           #Name to craw, gets used to get the start_urls[]
    label = None          #Name of the Label that needs to be added to the Crawled Node
    pathName = None       #Used to get ConfigFile
    relation = None       #Name of the relation between the BaseNode and Crawled Node

    urlEanDict = {}

    countUrl = -1
    JSONfilename = None

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    filteredDict = {}

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
        self.parseSource(response, self.JSONfilename, "hardware")

    def parseSource(self, response, JSONfilename, hardwareSort):
        print response
        print "\033[95m     == Initializing =="
        self.countUrl += 1
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()               #initiates connection
        graph_db = conn.openDb()                                            #initiates connection

        nodeDict = dict()                                                   #Makes a dictionary for the node

        baseNode = conn.getNode(graph_db, self.label)                       #Gets the BaseNode from the database
        baseNode.get_properties()                                           #Need to ask for properties to use the BaseNode (Workaround)
        baseNode.get_labels()                                               #Need to ask for labels to use the BaseNode (Workaround)

        print "\tParsing config"
        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths


        for x in listCrawl:
            key = response.xpath(configManager.getKeyxPath(x, self.path) % x).extract()         #Gets the key from the source. xPath is from the config.
            value= response.xpath(configManager.getValuexPath(x, self.path) % x ).extract()     #Gets the value from the source. xPath is from the config.
            nodeDict.update({str(key): str(value)})                                             #Adds Key:Value to the dict.
            if len(listCrawl) == x:
                nodeDict.update({"url":str(self.start_urls[self.countUrl]).replace("specificaties/","")})
        print "\tDone parsing config"

        print "\tParsing Dict"
        self.filteredDict = filter.FilterDict().filterDictionary(nodeDict)          #Filters the dict on empty values, '/xa0s' values and unicode.
        print "\tDone Parsing Dict"

        print "\033[95m     == Adding Node to database =="
        print "             \tReading the config: %s" % conn.isRead
        print "             \tDatabase connection: %s" % conn.isConnect

        eanInDict = None
        eanNumber = None
        if "EAN" in self.filteredDict:    #If the EAN does not exist in Dict, it returns 0
            eanInDict = True
            eanNumber = self.filteredDict['EAN']
        else:                                       #If EAN exists it goes into this thing
            print "!!\tEAN not found in Dict\t!!"
            eanInDict = False

        if conn.findNodeByEAN(graph_db, eanNumber) == False and eanInDict == True:    #Checks if EAN is in Dict and if EAN does not exist in DB
            print "Creating node"
            crawlNode, = graph_db.create(self.filteredDict)                         #Creates Node.
            crawlNode.add_labels(str(self.label))                                   #Adds label to the Node.
            graph_db.create(rel(crawlNode, self.relation, baseNode))                #Creates Relationship.
        else:
            print "!!\tNode exists, skipping\t!!"
        print "Adding dict to mongoDb=========="

        mongodbManager = MongoDbManager()
        mongoDbClient = mongodbManager.openDb()
        db = mongoDbClient['Hardware']
        collection = db[hardwareSort]
        collection.insert(self.filteredDict)

        print "Adding dict to mongoDb========="
        try :
            self.urlEanDict[str(self.start_urls[self.countUrl]).replace("specificaties/", "")] =  self.filteredDict['EAN'] #Adds the url:EAN to dict, COUNTURL HAS TO BE 0
        except:
            print "Failed to add EAN to new Dict"

        print '\033[31m', self.countUrl,"/",len(self.start_urls), '\033[30m'
        if len(self.start_urls) - 1 == self.countUrl:                                 #at the end of the crawling process writes to file
            with open(str('crawler/price-config/'+JSONfilename+'.json'), 'wb') as fp:
                json.dump(self.urlEanDict, fp)

        TorManager.TorManager().forceNewId()
        print "\033[95m   == Done :) =="



