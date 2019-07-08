#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

import os
from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass
from SQLite3Class import SQLite3Class
from DataFleaker import DataFleaker

##################MySQLClass Testing##########################
print("************************Start-MySQLClass Test-1")
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
print("************************End-MySQLClass Test-1")

print("************************Start-MySQLClass Test-2")
#List all the tables in mysql DB
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))
print("************************End-MySQLClass Test-2")


print("************************Start-MySQLClass Test-3")
'''
#Connect to new DB and show tables for it.
mySqlDB.mysqlConnectDataBase("phpmyadmin")
result = mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
for tables in result:
    print(tables[0])
print("result size = "+str(result.__len__()))
'''
#Create database DataFleaker if it don't exist
if( mySqlDB.mysqlCreateDataBase("DataFleaker") ):
    print("SUCCESS CREATING DB")
else:
    print("NO SUCCESS. DB Already Exist")
print("************************End-MySQLClass Test-3")


##################MongoDBClass Testing##########################

print("************************Start-MongoDBClass Test-1")
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
print("************************End-MongoDBClass Test-1")

print("************************Start-MongoDBClass Test-2")
#Insert one mongo Record into Database PlanetsDB, collection Galaxies
dictRecord = {"galaxy": "Milky Way", "diameter": "105k light years"}
mongoResult = mongoDB.mongoInsertOneRecord(collectionTableName2, dictRecord)
print(mongoResult)
print("************************End-MongoDBClass Test-2")

'''
print("************************Start-MongoDBClass Test-3")
#Insert one record by getting mongoTable reference
#mongoTable = mongoDatabase[collectionTableName]
#mongoRecord = {"planet": "Saturn", "location": "6th"}
#mongoTableRet= mongoTable.insert_one(mongoRecord)
#print(str(mongoTableRet))
#print(mongoTableRet.inserted_id)
print("************************End-MongoDBClass Test-3")
'''

print("************************Start-MongoDBClass Test-4")
#Insert list of records into Database PlanetsDB, collection Planets
listRecords = [{"planet": "Mercury", "location": "1st"},
               {"planet": "Venus", "location": "2nd"},
               {"planet": "Earth", "location": "3rd"},
               {"planet": "Mars", "location": "4th"},
               {"planet": "Jupiter", "location": "5th"}]
mongoResult = mongoDB.mongoInsertManyRecords(collectionTableName, listRecords)
print(mongoResult)
print("************************End-MongoDBClass Test-4")

print("************************Start-MongoDBClass Test-5")
mongoResult = mongoDB.mongoFindOne(collectionTableName)
print(mongoResult)
print("************************End-MongoDBClass Test-5")

print("************************Start-MongoDBClass Test-6")
mongoResult = mongoDB.mongoFindAll(collectionTableName)
print(mongoResult)
for dbRows in mongoResult:
    print(dbRows)
print("************************End-MongoDBClass Test-6")

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
#mongoResult = mongoDB.mongoDropCollectionTable(collectionTableName2)
#print(mongoResult)


##################SQLite3Class Testing##########################
'''
#Create SQLite3 Object.
sqlite3DBFileLocation = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
sqlite3DB = SQLite3Class(sqlite3DBFileLocation)
sqlite3DB.sqlite3ConnectDataBase()
sqlStr = "SELECT host_key, name, value, encrypted_value FROM cookies"
sqlite3Result = sqlite3DB.sqlite3ExecuteQuery(sqlStr)
for dbRows in sqlite3Result:
    print(dbRows)
'''

##################DataFleaker Testing##########################
print("************************Start-DataFleaker Test-1")
dataFleaker = DataFleaker("First DataFleaker Mix Test",
                          mySqlDB,
                          mongoDB
                          )

print(dataFleaker.getDescription())
mongoResult = mongoDB.mongoFindAll(collectionTableName)

#Converts mongoDB to mySQL
dataFleaker.dataFleakerMongoToMySQL(mongoResult)
print("************************End-DataFleaker Test-1")