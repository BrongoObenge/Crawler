#!/usr/bin/env python
import sys
from crawler.dbmanager import Neo4jDatabaseManager

print "Connecting to database!"
neo4jManager = Neo4jDatabaseManager.DatabaseConnectionNeo4j()
graph_db = neo4jManager.openDb()

help = "Usage ./start.py [Command]\n" \
       "\tcreate : Creates the Nodes and Relationships.\n" \
       "\tdelete : Deleletes the entire database.\n" \
       "\thelp : Prints this window."

#takes commands from commandline
if  sys.argv[1] == "create":
    neo4jManager.createDatabase(graph_db)
if  sys.argv[1] == "delete":
    neo4jManager.deleteWholeDatabase(graph_db)
if sys.argv[1] == "help":
    print help









