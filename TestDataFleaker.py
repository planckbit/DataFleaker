#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

import os
from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass
from SQLite3Class import SQLite3Class

##################MySQL Database Testing##########################
#Create mySQLDB Object.
mySqlDB = MySQLClass("localhost","root","");

#Select a DB and connect to it.
mySqlDB.mysqlConnectDataBase("mysql")

#Print mysqlDB Description
print(mySqlDB.getDescription())

#Print Total DB count regardless of type of DB
print("Total DB Count="+str(mySqlDB.getInstanceCount()))

#List all MySQL Databases
mySqlDB.getMySqlShowDatabases()

#List all the tables in mysql DB
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))

#Connect to new DB and show tables for it.
mySqlDB.mysqlConnectDataBase("phpmyadmin")
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))

#Create database DataFleaker if it don't exist
if( mySqlDB.mysqlCreateDataBase("DataFleaker") ):
    print("SUCCESS CREATING DB")
else:
    print("NO SUCCESS. DB Already Exist")


##################Mongo Database Testing##########################
#Create mongoDB Object
mongoDB = MongoDBClass("mongodb://localhost:27017")
#Create mongo Database named TestingDB.
# One collection and record must be added before it appears
# in mongo.
mongoDatabase = mongoDB.mongoConnectDataBase("TestingDB")

#Insert one mongo Record Into Database TestingDB, collection Employee
dictRecord = {"fname": "Planck", "address": "Florida"}
mongoResult = mongoDB.mongoInsertOneRecord("Employee", dictRecord)
print(mongoResult)

#Insert one record by getting mongoTable reference
#mongoTable = mongoDatabase["Employee"]
#mongoRecord = {"fname": "Planck-2", "address": "Florida-2"}
#mongoTableRet= mongoTable.insert_one(mongoRecord)
#print(str(mongoTableRet))
#print(mongoTableRet.inserted_id)

#Insert list of records into Database TestingDB, collection Employee
listRecords = [{"fname": "Mercury", "address": "1st"},
               {"fname": "Venus", "address": "2nd"},
               {"fname": "Earth", "address": "3rd"},
               {"fname": "Mars", "address": "4th"},
               {"fname": "Jupiter", "address": "5th"}]
mongoResult = mongoDB.mongoInsertManyRecords("Employee", listRecords)
print(mongoResult)

mongoResult = mongoDB.mongoFindOne("Employee")
print(mongoResult)

mongoResult = mongoDB.mongoFindAll("Employee")
for dbRows in mongoResult:
    print(dbRows)

specificFields = { "_id": 0, "fname": 1, "address": 1}
mongoResult = mongoDB.mongoFindAllSpecificFields("Employee", specificFields)
for dbRows in mongoResult:
    print(dbRows)

filterQuery = { "fname": "Mars"}
mongoResult =  mongoDB.mongoFindAllFilter("Employee", filterQuery)
for dbRows in mongoResult:
    print(dbRows)

mongoResult = mongoDB.mongoFindAllSpecificFieldsFilter("Employee", filterQuery, specificFields)
for dbRows in mongoResult:
    print(dbRows)

#Print Mongo Database list.
mongoDB.printMongoShowDatabases()

#Drop Mongo DB
#mongoDB.mongoDropDataBase("TestingDB")

#Get Mongo DB List.
mongoDBList = mongoDB.getMongoShowDatabases()
for dbs in mongoDBList:
    print(dbs)


##################SQLite3 Database Testing##########################
#Create SQLite3 Object.
sqlite3DBFileLocation = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
sqlite3DB = SQLite3Class(sqlite3DBFileLocation);
sqlite3DB.sqlite3ConnectDataBase()
sqlStr = "SELECT host_key, name, value, encrypted_value FROM cookies"
sqlite3Result = sqlite3DB.sqlite3ExecuteQuery(sqlStr)
for dbRows in sqlite3Result:
    print(dbRows)