import LinkSpider
from crawler.filter.LinkManager import ParseLinks
class CaseLinks(LinkSpider.LinkSpider):
    name = "CASElinks"
    linksConf = "CASELink"
    linkString = 'http://tweakers.net/categorie/61/behuizingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class MotherboardLinks(LinkSpider.LinkSpider):
    name = "MOTHERBOARDlinks"
    linksConf = "MOTHERBOARDLink"
    linkString = 'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class MemoryLinks(LinkSpider.LinkSpider):
    name = "MEMORYlinks"
    linksConf = "MEMORYLink"
    linkString ='http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class GrapihcsCardLinks(LinkSpider.LinkSpider):
    name = "GPUlinks"
    linksConf = "GPULink"
    linkString ='http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class ProcessorLinks(LinkSpider.LinkSpider):
    name = "CPUlinks"
    linksConf = "CPULink"
    linkString =  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class PowerSupplyLinks(LinkSpider.LinkSpider):
    name = "POWERUNITlinks"
    linksConf = "PSULink"
    linkString = 'http://tweakers.net/categorie/664/voedingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class HDDLinks(LinkSpider.LinkSpider):
    name = "HDDlinks"
    linksConf = "HDDLink"
    linkString = 'http://tweakers.net/categorie/50/interne-harde-schijven/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)
class SSDLinks(LinkSpider.LinkSpider):
    name = "SSDlinks"
    linksConf = "SSDLink"
    linkString = 'http://tweakers.net/categorie/674/solid-state-drives/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)
class SoundCardLinks(LinkSpider.LinkSpider):
    name = "SOUNDCARDlinks"
    linksConf = "SOUNDCARDLink"
    linkString = 'http://tweakers.net/categorie/53/geluidskaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)
class OpticalDriveLinks(LinkSpider.LinkSpider):
    name = "OPTICALDRIVElinks"
    linksConf = "OPTICALDRIVELink"
    linkString = 'http://tweakers.net/categorie/634/optische-drives/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)
