# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import pymongo
import mysql.connector
import json
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
                                     mysqlDBEngineType: str = MySQLEngineTypes.INNODB.value,
                                     bulkInsert: bool = False):
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
        strQuery_1 = "INSERT INTO " + collectionTable + "(json_record) VALUES"
        strQuery_2 = ""
        for records in mongoDBCursor:
            #print(str(records))
            #For Mysql 5.7 and greater we need double double quotes for it to be accepted as a json_type.
            # This issue is not the case for MariaDB. This works for both.
            if not bulkInsert:
                strQuery_2 = "(\""+json.dumps(records).replace("\"","\"\"")+"\")"
                #print(strQuery)
                self.mysqlClassObject.mysqlExecuteInsert(strQuery_1 + strQuery_2)
            else:
                strQuery_2 += "(\""+json.dumps(records).replace("\"","\"\"")+"\"),"

        if bulkInsert:
            #strip last char ','
            strQuery_2 = strQuery_2[:-1]
            #print(strQuery_1 + strQuery_2)
            self.mysqlClassObject.mysqlExecuteInsert(strQuery_1 + strQuery_2)

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
                try:
                    dictEntry[str(columnNames[columnCount])] = rowRecords[columnCount].decode("utf-8")
                except:
                    dictEntry[str(columnNames[columnCount])] = str(rowRecords[columnCount])

                columnCount += 1
            #print(dictEntry)
            listDictRecords.append(dictEntry)
            dictEntry = {}
            columnCount = 0

        #print(listDictRecords)
        #for i in listDictRecords:
        #    print(i)
        #Create mongoDB and Insert the converted MySQL records in JSON to mongoDB.
        self.mongoDBObject.mongoConnectDataBase(self.mysqlClassObject.getDataBaseName())
        self.mongoDBObject.mongoInsertManyRecords(mysqlMariaTableName, listDictRecords)

    def __del__(self):
        DataFleakerClass.dataFleakerInstanceCount -= 1






