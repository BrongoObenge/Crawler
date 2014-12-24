__author__ = 'j'
import PriceSpider
import Config as config


class CPUCrawler(PriceSpider.PriceSpider):
    name = "CPUprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "CPUpath"        #Used to get ConfigFile
    arrEanIdentifier = "CPUEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    JSONpath = None
    JSONpathLocation = "CPUjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class GPUCrawler(PriceSpider.PriceSpider):
    name = "GPUprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "GPUpath"        #Used to get ConfigFile
    arrEanIdentifier = "GPUEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    JSONpath = None
    JSONpathLocation = "GPUjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class HDDCrawler(PriceSpider.PriceSpider):
    name = "HDDprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "HDDpath"        #Used to get ConfigFile
    arrEanIdentifier = "HDDEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "HDDjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class SSDCrawler(PriceSpider.PriceSpider):
    name = "SSDprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "SSDpath"        #Used to get ConfigFile
    arrEanIdentifier = "SSDEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "SSDjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class CaseCrawler(PriceSpider.PriceSpider):
    name = "CASEprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "CASEpath"        #Used to get ConfigFile
    arrEanIdentifier = "CASEEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "CASEjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class MemoryCrawler(PriceSpider.PriceSpider):
    name = "MEMORYprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "MEMORYpath"        #Used to get ConfigFile
    arrEanIdentifier = "MEMORYEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "MEMORYjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class SoundcardCrawler(PriceSpider.PriceSpider):
    name = "SOUNDCARDprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "SOUNDCARDpath"        #Used to get ConfigFile
    arrEanIdentifier = "SOUNDCARDEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "SOUNDCARDjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class OpticaldriveCrawler(PriceSpider.PriceSpider):
    name = "OPTICALDRIVEprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "OPTICALDRIVEpath"        #Used to get ConfigFile
    arrEanIdentifier = "OPTICALDRIVEEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "OPTICALDRIVEjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class MotherboardCrawler(PriceSpider.PriceSpider):
    name = "MOTHERBOARDprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "MOTHERBOARDpath"        #Used to get ConfigFile
    arrEanIdentifier = "MOTHERBOARDEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "MOTHERBOARDjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

class PSUCrawler(PriceSpider.PriceSpider):
    name = "PSUprice"           #Name to craw, gets used to get the start_urls[]
    pathName = "PSUpath"        #Used to get ConfigFile
    arrEanIdentifier = "PSUEAN"
    relation = "SELLS"                #Name of the relation between the BaseNode and Crawled Node

    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    JSONpath = None
    JSONpathLocation = "PSUjson"
    filteredDict = {}
    arrEan = []
    y = -1
    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
        JSONpath = config.price_configs[JSONpathLocation]
    else:
        print("ERROR: key does not exist in dictonairy")
    def parse(self, response):
        PriceSpider.PriceSpider.altParse(self, response)

