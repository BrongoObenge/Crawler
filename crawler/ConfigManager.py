__author__ = 'j'
import ConfigParser


class ParseConfig:
    config = ConfigParser.ConfigParser()
    def __init__(self):
        pass

    def sumSection(self, filePath):
        '''
        Counts the row amounts in the config file.
        :param file: path to the file.
        :return: Int with the amount of rows in a config file.
        '''
        conf = self.config
        conf.read(filePath)
        sumCrawl = 0
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    sumCrawl += 1
        return sumCrawl

    def getCrawlList(self, filePath):
        '''
        Gives the List back of the Sections (TableRows) that needs to be crawled.
        :param filePath: Path to the config file.
        :return: Array with the rows.
        '''
        try:
            self.config.read(filePath)
        except:
            "CrawlList wrong"
        listCrawl = []
        for x in range(1,100):
            a = "ROW"+str(x)
            if self.config.has_section(a):
                crawl = self.config.get(a, 'crawl')
                if crawl == "1":
                    listCrawl.append(x)
        return listCrawl

    def getValuexPath(self, int, filePath):
        file = filePath
        self.config.read(file)
        if self.config.has_option("ROW"+str(int), "xpathvalue"):
            customPath = self.config.get("ROW"+str(int), "xpathvalue")
        else:
            customPath = self.config.get("DEFAULT", "xpathvalue")
        return customPath

    def getKeyxPath(self, int, filePath):
        file = filePath
        self.config.read(file)
        if self.config.has_option("ROW"+str(int), "xpathkey"):
            customPath = self.config.get("ROW"+str(int), "xpathkey")
        else:
            customPath = self.config.get("DEFAULT", "xpathkey")
        return customPath

    def getxPathPriceCrawler(self, int, filePath):
        '''
        Gets the xpaths in the config of the price crawler.
        :param int: The row number.
        :param filePath:Path to the config file.
        :return: Dict with the xpaths.
        '''
        file = filePath
        self.config.read(file)
        pathDict = {
            'xpathshopname':None,
            'xpathshopscore':None,
            'xpathdelivery':None,
            'xpathbareprice':None,
            'xpathshopprice':None,
            'xpathclickout':None,
            }
        #####
        if self.config.has_option("ROW"+str(int), "xpathshopname"):
            pathDict['xpathshopname'] = self.config.get("ROW"+str(int), "xpathshopname")
        else:
            pathDict['xpathshopname'] = self.config.get("DEFAULT", "xpathshopname")
        #####
        if self.config.has_option("ROW"+str(int), "xpathshopscore"):
            pathDict['xpathshopscore'] = self.config.get("ROW"+str(int), "xpathshopscore")
        else:
            pathDict['xpathshopscore'] = self.config.get("DEFAULT", "xpathshopscore")
        #####
        if self.config.has_option("ROW"+str(int), "xpathdelivery"):
            pathDict['xpathdelivery'] = self.config.get("ROW"+str(int), "xpathdelivery")
        else:
            pathDict['xpathdelivery'] = self.config.get("DEFAULT", "xpathdelivery")
        #####
        if self.config.has_option("ROW"+str(int), "xpathbareprice"):
            pathDict['xpathbareprice'] = self.config.get("ROW"+str(int), "xpathbareprice")
        else:
            pathDict['xpathbareprice'] = self.config.get("DEFAULT", "xpathbareprice")
        #####
        if self.config.has_option("ROW"+str(int), "xpathshopprice"):
            pathDict['xpathshopprice'] = self.config.get("ROW"+str(int), "xpathshopprice")
        else:
            pathDict['xpathshopprice'] = self.config.get("DEFAULT", "xpathshopprice")
        #####
        if self.config.has_option("ROW"+str(int), "xpathclickout"):
            pathDict['xpathclickout'] = self.config.get("ROW"+str(int), "xpathclickout")
        else:
            pathDict['xpathclickout'] = self.config.get("DEFAULT", "xpathclickout")
        #####
        return pathDict