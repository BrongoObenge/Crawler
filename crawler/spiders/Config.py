import crawler.filter.LinkManager as linkMan
'''
Contains all the configs to crawl
    -   Paths
    -   links
    -   Dict



'''
linkManager = linkMan.ParseLinks()
#Db config path
db_path = "configs/db_config.conf"

#CPU
cpu_urls = linkManager.getCrawlLinks("CPULink")
cpu_path = "crawler/configs/specs/CPU.conf"

#GPU
gpu_urls = linkManager.getCrawlLinks("GPULink")
gpu_path = "crawler/configs/specs/GPU.conf"

#MOBO
mobo_urls = linkManager.getCrawlLinks("MOTHERBOARDLink")
mobo_path = "crawler/configs/specs/MOTHERBOARD.conf"

#MEMORY
mem_urls = linkManager.getCrawlLinks("MEMORYLink")
mem_path = "crawler/configs/specs/MEMORY.conf"

#PSU
psu_urls = linkManager.getCrawlLinks("PSULink")
psu_path = "crawler/configs/specs/PSU.conf"

#CASE
case_urls = linkManager.getCrawlLinks("CASELink")
case_path = "crawler/configs/specs/CASE.conf"

#HDD
hdd_urls = linkManager.getCrawlLinks("HDDLink")
hdd_path = "crawler/configs/specs/HDD.conf"

#SOUNDCARD
soundcard_urls = linkManager.getCrawlLinks("SOUNDCARDLink")
soundcard_path = "crawler/configs/specs/SOUNDCARD.conf"

#OPTICALDRIVE
opticaldrive_urls = linkManager.getCrawlLinks("OPTICALDRIVELink")
opticaldrive_path = "crawler/configs/specs/OPTICALDRIVE.conf"

#SSD
ssd_urls = linkManager.getCrawlLinks("SSDLink")
ssd_path = "crawler/configs/specs/SSD.conf"

#TEST
test_urls = linkManager.getCrawlLinks("TESTLink")
test_path = "crawler/configs/TEST.conf"



componentList = {"PROCESSORcrawl":cpu_urls, "PROCESSORpath": cpu_path,                          #CPU
                 "GPUpath":gpu_path, "GPUcrawl":gpu_urls,                                       #GPU
                 "MEMORYcrawl":mem_urls, "MEMORYpath":mem_path,                                 #MEMORY
                 "PSUcrawl":psu_urls ,"PSUpath":psu_path,                                       #PSU
                 "MOTHERBOARDcrawl":mobo_urls,"MOTHERBOARDpath":mobo_path,                      #MOTHERBOARD
                 "CASEcrawl":case_urls,"CASEpath":case_path,                                    #CASE
                 "HDDcrawl":hdd_urls, "HDDpath":hdd_path,                                       #HDD
                 "SOUNDCARDcrawl":soundcard_urls,"SOUNDCARDpath":soundcard_path,                #SOUNDCARD
                 "OPTICALDRIVEcrawl":opticaldrive_urls, "OPTICALDRIVEpath":opticaldrive_path,   #OPTICALDRIVE
                 "SSDcrawl":ssd_urls, "SSDpath":ssd_path,                                       #SSD
                 "TESTcrawl":test_urls, "TESTpath":test_path                                    #TEST
                 }

databaseConfig = {"db_path":db_path}
#########################

#SOUNDCARD
soundcard_path_price = "crawler/configs/price/SOUNDCARD.conf"
soundcard_json_price = "crawler/configs/price-config/SOUNDCARD.json"
soundcard_urls_price = linkManager.getPriceCrawlLinks(soundcard_json_price)
soundcard_EAN_price = linkManager.getEANList(soundcard_json_price)

#GPU
GPU_path_price = "crawler/configs/price/GPU.conf"
GPU_json_price = "crawler/configs/price-config/GPU.json"
GPU_urls_price = linkManager.getPriceCrawlLinks(GPU_json_price)
GPU_EAN_price = linkManager.getEANList(GPU_json_price)

#CPU
CPU_path_price = "crawler/configs/price/CPU.conf"
CPU_json_price = "crawler/configs/price-config/CPU.json"
CPU_urls_price = linkManager.getPriceCrawlLinks(CPU_json_price)
CPU_EAN_price = linkManager.getEANList(CPU_json_price)

#HDD
HDD_path_price = "crawler/configs/price/HDD.conf"
HDD_json_price = "crawler/configs/price-config/HDD.json"
HDD_urls_price = linkManager.getPriceCrawlLinks(HDD_json_price)
HDD_EAN_price = linkManager.getEANList(HDD_json_price)

#SSD
SSD_path_price = "crawler/configs/price/SSD.conf"
SSD_json_price = "crawler/configs/price-config/SSD.json"
SSD_urls_price = linkManager.getPriceCrawlLinks(SSD_json_price)
SSD_EAN_price = linkManager.getEANList(SSD_json_price)

#CASE
CASE_path_price = "crawler/configs/price/CASE.conf"
CASE_json_price = "crawler/configs/price-config/CASE.json"
CASE_urls_price = linkManager.getPriceCrawlLinks(CASE_json_price)
CASE_EAN_price = linkManager.getEANList(CASE_json_price)

#OPTICALDRIVE
OPTICALDRIVE_path_price = "crawler/configs/price/OPTICALDRIVE.conf"
OPTICALDRIVE_json_price = "crawler/configs/price-config/OPTICALDRIVE.json"
OPTICALDRIVE_urls_price = linkManager.getPriceCrawlLinks(OPTICALDRIVE_json_price)
OPTICALDRIVE_EAN_price = linkManager.getEANList(OPTICALDRIVE_json_price)

#MEMORY
MEMORY_path_price = "crawler/configs/price/MEMORY.conf"
MEMORY_json_price = "crawler/configs/price-config/MEMORY.json"
MEMORY_urls_price = linkManager.getPriceCrawlLinks(MEMORY_json_price)
MEMORY_EAN_price = linkManager.getEANList(MEMORY_json_price)

#PSU
PSU_path_price = "crawler/configs/price/PSU.conf"
PSU_json_price = "crawler/configs/price-config/PSU.json"
PSU_urls_price = linkManager.getPriceCrawlLinks(PSU_json_price)
PSU_EAN_price = linkManager.getEANList(PSU_json_price)

#MOTHERBOARD
MOTHERBOARD_path_price = "crawler/configs/price/MOTHERBOARD.conf"
MOTHERBOARD_json_price = "crawler/configs/price-config/MOTHERBOARD.json"
MOTHERBOARD_urls_price = linkManager.getPriceCrawlLinks(MOTHERBOARD_json_price)
MOTHERBOARD_EAN_price = linkManager.getEANList(MOTHERBOARD_json_price)



price_configs = {
    "SOUNDCARDpath":soundcard_path_price, "SOUNDCARDprice":soundcard_urls_price, "SOUNDCARDEAN":soundcard_EAN_price, "SOUNDCARDjson":soundcard_json_price,
    "GPUpath":GPU_path_price, "GPUprice":GPU_urls_price, "GPUEAN":GPU_EAN_price, "GPUjson":GPU_json_price,
    "CPUpath":CPU_path_price, "CPUprice":CPU_urls_price, "CPUEAN":CPU_EAN_price, "CPUjson":CPU_json_price,
    "HDDpath":HDD_path_price, "HDDprice":HDD_urls_price, "HDDEAN":HDD_EAN_price, "HDDjson":HDD_json_price,
    "SSDpath":SSD_path_price, "SSDprice":SSD_urls_price, "SSDEAN":SSD_EAN_price, "SSDjson":SSD_json_price,
    "CASEpath":CASE_path_price, "CASEprice":CASE_urls_price, "CASEEAN":CASE_EAN_price, "CASEjson":CASE_json_price,
    "OPTICALDRIVEpath":OPTICALDRIVE_path_price, "OPTICALDRIVEprice":OPTICALDRIVE_urls_price, "OPTICALDRIVEEAN":OPTICALDRIVE_EAN_price, "OPTICALDRIVEjson":OPTICALDRIVE_json_price,
    "MEMORYpath":MEMORY_path_price, "MEMORYprice":MEMORY_urls_price, "MEMORYEAN":MEMORY_EAN_price, "MEMORYjson":MEMORY_json_price,
    "PSUpath":PSU_path_price, "PSUprice":PSU_urls_price, "PSUEAN":PSU_EAN_price, "PSUjson":PSU_json_price,
    "MOTHERBOARDpath":MOTHERBOARD_path_price, "MOTHERBOARDprice":MOTHERBOARD_urls_price, "MOTHERBOARDEAN":MOTHERBOARD_EAN_price, "MOTHERBOARDjson":MOTHERBOARD_json_price,

}