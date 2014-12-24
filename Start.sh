#!/bin/bash
echo "=== Starting the crawler ==="
echo "\tChmod +x to the executables"
chmod +x Refresh-Crawl-Links.sh
chmod +x Crawl-Specs.sh
chmod +x Update-Prices.sh
chmod +x createBaseDatabase.py
echo "\tDone chmod"
echo "\tCreating the base database... DATABASE WILL BE ERASED."
./createBaseDatabase.py delete
./createBaseDatabase.py create
echo "\tUpdating the links."
./Refresh-Crawl-Links.sh
echo "\tStaring the crawls."
sleep 10
./Crawl-Specs.sh
echo "Done"
echo "To update the prices please run Update-Prices.sh"
sleep 10
echo "=== Done ==="