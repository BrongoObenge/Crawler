__author__ = 'j'
import MySQLdb
import datetime
from time import  strftime

class MySqlManager:
    host = "localhost"
    user = "user1"
    passwd = "user1"
    db = "hardwareprice"
    DATABASE_NAME = "hardwareprice"
    TABLE_PRICE = "hardwareprice"
    TABLE_PRICE_EAN = "ean"
    TABLE_PRICE_SHOPNAME = "shopname"
    TABLE_PRICE_DELIVERY = "delivery"
    TABLE_PRICE_PRICEEX = "priceex"
    TABLE_PRICE_PRICEINC = "priceinc"
    TABLE_PRICE_LINKSHOP = "linkshop"
    TABLE_PRICE_TIMESTAMP = "timestamp"

    def __init__(self):
        pass
    def openDb(self):
        db = MySQLdb.connect(host= self.host, # your host, usually localhost
                      user= self.user, # your username
                      passwd= self.passwd, # your password
                      db= self.db) # name of the data base
        return db

    def insertPrice(self, db, EAN, shopname, delivery, priceex, priceinc, linkshop, timestamp):
        isExecuted = False
        try:
            a = MySqlManager()
            cursor = db.cursor()

            query = "INSERT INTO " \
                    +a.TABLE_PRICE+" ("+a.TABLE_PRICE_EAN+", "+a.TABLE_PRICE_SHOPNAME+", "+a.TABLE_PRICE_DELIVERY+", "+a.TABLE_PRICE_PRICEEX+", "+a.TABLE_PRICE_PRICEINC+", "+a.TABLE_PRICE_LINKSHOP+", "+a.TABLE_PRICE_TIMESTAMP+") " \
                                "VALUES ('"+str(EAN)+"', '"+str(shopname)+"', '"+str(delivery)+"', '"+str(priceex)+"', '"+str(priceinc)+"', '"+str(linkshop)+"', '"+str(timestamp)+"')"
            cursor.execute(query)
            db.commit()
            isExecuted = True
        except:
            print "!! Error while executing SQL query, check the query. Problem might be in the priceex and priceinc !!"
        return isExecuted

    def getTimestamp(self):
        timestamp = strftime("%Y-%m-%d %H:%M:%S")
        return timestamp
