# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import pymongo
import mysql.connector
from MySQLClass import MySQLClass, MySQLEngineTypes
from MongoDBClass import MongoDBClass
from SQLite3Class import SQLite3Class

class DataFleakerClass:
    dataFleakerInstanceCount = 0

    def __init__(self,
                 description: str,
                 mysqlClassObject: MySQLClass = None,
                 mongoDBObject: MongoDBClass = None,
                 sqlite3Object: SQLite3Class = None):
        DataFleakerClass.dataFleakerInstanceCount += 1
        self.description = description
        self.mysqlClassObject = mysqlClassObject
        self.mongoDBObject = mongoDBObject
        self.sqlite3Object = sqlite3Object

    def getDescription(self):
        return self.description

    def setDatabaseClassObjectsToFleaker(self,
                                         mysqlClassObject: MySQLClass = None,
                                         mongoDBObject: MongoDBClass = None,
                                         sqlite3Object: SQLite3Class = None):
        self.mysqlClassObject = mysqlClassObject
        self.mongoDBObject = mongoDBObject
        self.sqlite3Object = sqlite3Object

    def setMySQLClassObjectToFleaker(self, mysqlClassObject: MySQLClass=None):
        self.mysqlClassObject = mysqlClassObject

    def setMongoClassObjectToFleaker(self, mongoDBObject: MongoDBClass = None):
        self.mongoDBObject = mongoDBObject

    def setSQLite3ClassClassObjectToFleaker(self, sqlite3Object: SQLite3Class = None):
        self.sqlite3Object = sqlite3Object

    def dataFleakerMongoToMySQLMaria(self,
                                     collectionTable: str,
                                     mongoDBCursor: pymongo.cursor.Cursor,
                                     mysqlDBEngineType: str = MySQLEngineTypes.INNODB.value):
        if self.mongoDBObject == None:
            print("No Valid MongoDBClass Object")
            return False
        if self.mysqlClassObject == None:
            print("No Valid MySQLClass Object")
            return False

        #Create DB
        self.mysqlClassObject.mysqlCreateDataBase(self.mongoDBObject.getDataBaseName())
        #Connect to DB
        self.mysqlClassObject.mysqlConnectDataBase(self.mongoDBObject.getDataBaseName())
        #Create Table
        self.mysqlClassObject.mySQLCreateDatabaseTableJsonType(collectionTable, mysqlDBEngineType)

        #Insert mongoDB records into JSON type field in MySQL
        for records in mongoDBCursor:
            strQuery = "INSERT INTO "+collectionTable+"(json_record) VALUES(\""+str(records)+"\")"
            #print(strQuery)
            self.mysqlClassObject.mysqlExecuteInsert(strQuery)

    def dataFleakerMySQLMariaToMongoDB(self,
                                       mysqlMariaTableName: str,
                                       mysqlDBCursorResults):
        if self.mongoDBObject == None:
            print("No Valid MongoDBClass Object")
            return False
        if self.mysqlClassObject == None:
            print("No Valid MySQLClass Object")
            return False

        dictEntry = {}
        listDictRecords = []
        columnCount = 0
        columnNames = self.mysqlClassObject.columnNames
        columnLen = len(columnNames)

        for rowRecords in mysqlDBCursorResults:
            while columnCount < columnLen:
                dictEntry[str(columnNames[columnCount])] = rowRecords[columnCount].decode("utf-8")
                columnCount += 1
            #print(dictEntry)
            listDictRecords.append(dictEntry)
            dictEntry = {}
            columnCount = 0

        print(listDictRecords)
        #Create mongoDB and Insert the converted MySQL records in JSON to mongoDB.
        self.mongoDBObject.mongoConnectDataBase(self.mysqlClassObject.getDataBaseName())
        mongoResult = self.mongoDBObject.mongoInsertManyRecords(mysqlMariaTableName, listDictRecords)
        #print(mongoResult)

    def __del__(self):
        DataFleakerClass.dataFleakerInstanceCount -= 1






