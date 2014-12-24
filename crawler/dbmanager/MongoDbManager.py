__author__ = 'j'
import pymongo
from pymongo import MongoClient
class MongoDbManager:
    MONGODB_CONNECTION_URI = "mongodb://localhost:27017/"

    def __init__(self):
        pass

    def openDb(self):
        client = MongoClient(self.MONGODB_CONNECTION_URI)

        return client

    def createNodeFromDict(self, MongoDbClient, nodeDict):
        pass