#!/bin/bash
echo "###########################################"
echo "Updating Prices"
echo "Crawling GPU"
sleep 1
	scrapy crawl GPUprice
echo "DONE CRAWLING GPU"
sleep 1
echo "Crawling CPU"
sleep 1
	 scrapy crawl PROCESSORprice
echo "DONE CRAWLING CPU"
sleep 1

echo "Crawling RAM"
sleep 1
	 scrapy crawl MEMORYprice
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling PSU"
sleep 1
	 scrapy crawl PSUprice
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling Motherboard"
sleep 1
	 scrapy crawl MOTHERBOARDprice
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling Case"
sleep 1
	 scrapy crawl CASEprice
echo "DONE CRAWLING Case"
sleep 1

echo "Crawling Soundcard"
sleep 1
	 scrapy crawl SOUNDCARDprice
echo "DONE CRAWLING SOUNDCARD"
sleep 1

echo "Crawling SSD"
sleep 1
	 scrapy crawl SSDprice
echo "DONE CRAWLING SSD"
sleep 1

echo "Crawling HDD"
sleep 1
	 scrapy crawl HDDprice
echo "DONE CRAWLING HDD"
sleep 1

echo "Crawling Optical Drive"
sleep 1
	 scrapy crawl OPTICALDRIVEprice
echo "DONE CRAWLING OPTICALDRIVE"
sleep 1

echo "FINISHED"
sleep 3

