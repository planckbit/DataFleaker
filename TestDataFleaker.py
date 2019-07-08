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
mongoServerAddress = "mongodb://localhost:27017"
mongoDB = MongoDBClass(mongoServerAddress)
#Create mongo Database named PlanetsDB.
# One collection and record must be added before it appears
# in mongo.
dbName = "PlanetsDB"
collectionTableName = "Planets"
collectionTableName2 = "Galaxies"
mongoDatabase = mongoDB.mongoConnectDataBase(dbName)

#Insert one mongo Record Into Database PlanetsDB, collection Planets
dictRecord = {"planet": "Saturn", "location": "6th"}
mongoResult = mongoDB.mongoInsertOneRecord(collectionTableName, dictRecord)
print(mongoResult)

#Insert one mongo Record into Database PlanetsDB, collection Galaxies
dictRecord = {"galaxy": "Milky Way", "diameter": "105k light years"}
mongoResult = mongoDB.mongoInsertOneRecord(collectionTableName2, dictRecord)
print(mongoResult)

#Insert one record by getting mongoTable reference
#mongoTable = mongoDatabase[collectionTableName]
#mongoRecord = {"planet": "Saturn", "location": "6th"}
#mongoTableRet= mongoTable.insert_one(mongoRecord)
#print(str(mongoTableRet))
#print(mongoTableRet.inserted_id)

#Insert list of records into Database PlanetsDB, collection Planets
listRecords = [{"planet": "Mercury", "location": "1st"},
               {"planet": "Venus", "location": "2nd"},
               {"planet": "Earth", "location": "3rd"},
               {"planet": "Mars", "location": "4th"},
               {"planet": "Jupiter", "location": "5th"}]
mongoResult = mongoDB.mongoInsertManyRecords(collectionTableName, listRecords)
print(mongoResult)

mongoResult = mongoDB.mongoFindOne(collectionTableName)
print(mongoResult)

mongoResult = mongoDB.mongoFindAll(collectionTableName)
for dbRows in mongoResult:
    print(dbRows)

specificFields = { "_id": 0, "planet": 1, "location": 1}
mongoResult = mongoDB.mongoFindAllSpecificFields(collectionTableName, specificFields)
for dbRows in mongoResult:
    print(dbRows)

filterQuery = { "planet": "Mars"}
mongoResult =  mongoDB.mongoFindAllFilter(collectionTableName, filterQuery)
for dbRows in mongoResult:
    print(dbRows)

mongoResult = mongoDB.mongoFindAllSpecificFieldsFilter(collectionTableName, filterQuery, specificFields)
for dbRows in mongoResult:
    print(dbRows)

#Print Mongo Database list.
mongoDB.printMongoShowDatabases()

#Drop Mongo DB
#mongoDB.mongoDropDataBase(dbName)

#Get Mongo DB List.
mongoDBList = mongoDB.getMongoShowDatabases()
for dbs in mongoDBList:
    print(dbs)

#Delete One record
deleteOneRecordQuery = {"location": "3rd"}
mongResult = mongoDB.mongoDeleteOneRecord(collectionTableName, deleteOneRecordQuery)
print(mongoResult)

#Delete many records starting with planet name letter 'M'
deleteManyQuery = {"planet": {"$regex": "^M"}}
mongoResult = mongoDB.mongoDeleteManyRecords(collectionTableName, deleteManyQuery)
print(mongoResult.deleted_count)

#Test Limit
mongoResult = mongoDB.mongoFindAll(collectionTableName,5)
for dbRows in mongoResult:
    print(dbRows)

#Drop collectionTableName2 - Galaxies
mongoResult = mongoDB.mongoDropCollectionTable(collectionTableName2)
print(mongoResult)


##################SQLite3 Database Testing##########################
'''
#Create SQLite3 Object.
sqlite3DBFileLocation = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
sqlite3DB = SQLite3Class(sqlite3DBFileLocation);
sqlite3DB.sqlite3ConnectDataBase()
sqlStr = "SELECT host_key, name, value, encrypted_value FROM cookies"
sqlite3Result = sqlite3DB.sqlite3ExecuteQuery(sqlStr)
for dbRows in sqlite3Result:
    print(dbRows)
'''