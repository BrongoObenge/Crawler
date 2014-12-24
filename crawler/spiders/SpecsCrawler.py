__author__ = 'j'
import Config as config
import SpecsSpider

class GraphicsCardSpider(SpecsSpider.SpecsSpider):
    name = "GPUcrawl"           #name to craw, gets used to get the start_urls[]
    label = "GRAPHICSCARD"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "GPUpath"        #Used to get ConfigFile
    relation = "GRAPHICSCARD"   #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "GPU"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class ProcessorSpider(SpecsSpider.SpecsSpider):
    name = "PROCESSORcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "PROCESSOR"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "PROCESSORpath"        #Used to get ConfigFile
    relation = "PROCESSOR"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "CPU"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class MemorySpider(SpecsSpider.SpecsSpider):
    name = "MEMORYcrawl"            #Name to craw, gets used to get the start_urls[]
    label = "MEMORY"                #Name of the Label that needs to be added to the Crawled Node
    pathName = "MEMORYpath"         #Used to get ConfigFile
    relation = "MEMORY"             #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "MEMORY"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class PSUSpider(SpecsSpider.SpecsSpider):
    name = "PSUcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "PSU"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "PSUpath"        #Used to get ConfigFile
    relation = "PSU"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "PSU"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class MotherboardSpider(SpecsSpider.SpecsSpider):
    name = "MOTHERBOARDcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "MOTHERBOARD"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "MOTHERBOARDpath"        #Used to get ConfigFile
    relation = "MOTHERBOARD"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "MOTHERBOARD"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class CaseSpider(SpecsSpider.SpecsSpider):
    name = "CASEcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "CASE"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "CASEpath"        #Used to get ConfigFile
    relation = "CASE"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "CASE"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class SoundcardSpider(SpecsSpider.SpecsSpider):
    name = "SOUNDCARDcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "SOUNDCARD"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "SOUNDCARDpath"        #Used to get ConfigFile
    relation = "SOUNDCARD"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "SOUNDCARD"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class SSDSpider(SpecsSpider.SpecsSpider):
    name = "SSDcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "SSD"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "SSDpath"        #Used to get ConfigFile
    relation = "SSD"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "SSD"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class HDDSpider(SpecsSpider.SpecsSpider):
    name = "HDDcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "HDD"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "HDDpath"        #Used to get ConfigFile
    relation = "HDD"            #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "HDD"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)
class OpticalDriveSpider(SpecsSpider.SpecsSpider):
    name = "OPTICALDRIVEcrawl"           #Name to craw, gets used to get the start_urls[]
    label = "OPTICALDRIVE"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "OPTICALDRIVEpath"       #Used to get ConfigFile
    relation = "OPTICALDRIVE"           #Name of the relation between the BaseNode and Crawled Node
    JSONfilename = "OPTICALDRIVE"
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response, self.JSONfilename, self.label)