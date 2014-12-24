__author__ = 'j'
from py2neo import neo4j, cypher
import py2neo
from py2neo import node
from ConfigParser import SafeConfigParser


class DatabaseConnectionNeo4j:
    '''
    Copied from github.com/Jiar/Neo4joctolove repo
    Configure database. Add Delete Modify

    '''
    url = None
    username = None
    password = None
    isRead = False
    isConnect = False
    db_path = "db_path"

#Get Data from db_config.conf
    parser = SafeConfigParser()
    try:
        parser.read('crawler/configs/db_config.conf')   #Defines Path
    except:
        print "Cannot open file \"db_config.conf\". Probably wrong path."
    url = parser.get('DATABASE', 'url')
    username = parser.get('DATABASE', 'username')
    password = parser.get('DATABASE', 'password')
    isRead = True

    def __init__(self):
        pass

    def openDb(self):
        graph_db = neo4j.GraphDatabaseService(self.url)
        self.isConnect = True
        return graph_db

    def closeDb(self):
        pass

    def getSomeData(self, graph_db):
        print graph_db.get_node(0)

    def getCountNodes(self, graph_db):
        print graph_db.get_node_count()

    def createNodeFromDict(self, graph_db, dict):
        isCreated = False
        graph_db.create(dict)
        isCreated = True
        return isCreated

    def getNode(self, graph_db, label): #Gets node from database. label = the Label of the Hardware, always include this in self
        node = None
        tempNode = None
        result = neo4j.CypherQuery(graph_db, "MATCH (n) WHERE n.Label = \""+ str(label)+"\" RETURN n").execute()
        for r in result:
            tempNode = r[0]
        uri = 'http://localhost:7474/db/data/node/' + str(tempNode._id)
        node = py2neo.neo4j.Node(uri)
        return node

    def findNodeByEAN(self, graph_db, EAN):
        '''
        Checks if node exists by EAN number
        :param graph_db:The graph_db service
        :param EAN: The EAN number in dictionary
        :return:Boolean if the Node exists
        '''
        found = None
        tempNode = None
        result = neo4j.CypherQuery(graph_db, "MATCH (n) WHERE n.EAN = \""+ str(EAN)+"\" RETURN n").execute()
        for r in result:
            tempNode = r[0]
        try:
            uri = 'http://localhost:7474/db/data/node/' + str(tempNode._id) #Node does exist, dont create node
            node = py2neo.neo4j.Node(uri)
            found = True
        except:
            #Exception is given when the EAN does not exist
            found = False                                   #Node does not exist, try to create it
        return found

    def getNodeByEAN(self, graph_db, EAN):
        '''
        Finds node by EAN number
        :param graph_db:The graph_db service
        :param EAN: The EAN number in dictionary
        :return:Node
        '''
        tempNode = None
        node = None
        result = neo4j.CypherQuery(graph_db, "MATCH (n) WHERE n.EAN = \""+ str(EAN)+"\" RETURN n").execute()
        for r in result:
            tempNode = r[0]
        try:
            uri = 'http://localhost:7474/db/data/node/' + str(tempNode._id) #Node does exist, dont create node
            node = py2neo.neo4j.Node(uri)
        except:
            #Exception is given when the EAN does not exist
            print "EAN not found!"
        return node

    def getNodeByName(self, graph_db, name):
        '''
        Finds node by EAN number
        :param graph_db:The graph_db service
        :param EAN: The EAN number in dictionary
        :return:Node
        '''
        tempNode = None
        node = None
        result = neo4j.CypherQuery(graph_db, "MATCH (n) WHERE n.name = \""+ str(name)+"\" RETURN n").execute()
        for r in result:
            tempNode = r[0]
        try:
            uri = 'http://localhost:7474/db/data/node/' + str(tempNode._id) #Node does exist, dont create node
            node = py2neo.neo4j.Node(uri)
        except:
            #Exception is given when the EAN does not exist
            print "EAN not found!"
        return node

    def createDatabase(self, graph_db):
        self.importDatabaseNodes(graph_db)
        self.importDatabaseRelations(graph_db)

    def deleteWholeDatabase(self, graph_db):
           print "Preparing to delete database"
           graph_db.clear()
           print "Success!"

    def importDatabaseNodes(self, graph_db):
        print "Opening file . . ."
        try:
            file = "crawler/base-database/create_db"
            dbFile=open(file,'r')
        except:
            print "Error while loading file"
            return "Error!"
        print "File " + dbFile.name + " opened! " + "\nin the mode : " + dbFile.mode
        print "Creating Nodes..."
        for line in dbFile.readlines():
            a, = graph_db.create(eval(line))
            a.add_labels("BASE")
        print "Success creating nodes!"

    def importDatabaseRelations(self, graph_db):
        try:
            file = "crawler/base-database/create_rel"
            dbFile=open(file,'r')
        except:
            print "Error while loading file"
            return "Error!"
        for line in dbFile.readlines():
            neo4j.CypherQuery(graph_db, line).execute()






