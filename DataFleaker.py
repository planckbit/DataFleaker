#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

import pymongo
from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass
from SQLite3Class import SQLite3Class

class DataFleaker:
    dataFleakerInstanceCount = 0

    def __init__(self,
                 description: str,
                 mysqlClassObject: MySQLClass = None,
                 mongoDBObject: MongoDBClass = None,
                 sqlite3Object: SQLite3Class = None):
        DataFleaker.dataFleakerInstanceCount += 1
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

    def dataFleakerMongoToMySQL(self, mongoDBCursor: pymongo.cursor.Cursor):
        if self.mongoDBObject == None:
            print("No Valid MongoDBClass Object")
            return False
        if self.mysqlClassObject == None:
            print("No Valid MySQLClass Object")
            return False

        #MongoDB Fleaker to MySQL DB
        if(self.mysqlClassObject.mysqlCreateDataBase(self.mongoDBObject.mongoGetCurrentDataBaseSet())):

            return True
        else:
            return False

    def __del__(self):
        DataFleaker.dataFleakerInstanceCount -= 1




