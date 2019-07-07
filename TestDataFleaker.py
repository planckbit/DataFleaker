#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass

##################MySQL Database Testing##########################
#Create mySQLDB Object.
mySqlDB = MySQLClass("localhost","root","");
#Select a DB and connect to it.
mySqlDB.mysqlConnectDataBase("mysql")
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

mySqlDB.mysqlConnectDataBase("phpmyadmin")
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))

##################Mongo Database Testing##########################
#Create mongoDB Object
mongoDB = MongoDBClass("mongodb://localhost:27017")

#Create mongo Database named TestingDB
mongoDatabase = mongoDB.mongoConnectDataBase("TestingDB")
mongoTable = mongoDatabase["NAMES"]
mongoRecord = {"name": "PlanckBit", "address": "Florida"}
mongoTableRet= mongoTable.insert_one(mongoRecord)
print(str(mongoTableRet))

#Get Mongo DB List.
mongoDB.getMongoShowDatabases()

#Drop Mongo DB
mongoDB.mongoDropDataBase("TestingDB")

#Get Mongo DB List.
mongoDB.getMongoShowDatabases()