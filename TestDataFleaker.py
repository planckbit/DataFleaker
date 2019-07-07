#!/usr/bin/python3

from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass

#Create mySQLDB Object.
mySqlDB = MySQLClass("localhost","root","");
#Select a DB and connect to it.
mySqlDB.mysqlConnectDataBase("netmon")
#Print mysqlDB Description
print(mySqlDB.getDescription())
#Print Total DB count regardless of type of DB
print("Total DB Count="+str(mySqlDB.getInstanceCount()))
mySqlDB.getMySqlShowDatabases()


if( mySqlDB.mysqlCreateDataBase("DataFleaker") ):
    print("SUCCESS CREATING DB")
else:
    print("NO SUCCESS")

result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))

mySqlDB.mysqlConnectDataBase("monitoring")
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))

