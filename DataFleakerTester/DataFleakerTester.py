# !/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import inspect
from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass
from MongoDBClass import MongoDBClass

class DataFleakerTester:
    inputBytes = b'Hello DataFleaker'
    mongoServerAddress = "mongodb://localhost:27017"
    dbName = "PlanetsDB"
    collectionTableName = "Planets"
    collectionTableName2 = "Galaxies"
    dictRecord = {"planet": "Saturn", "location": "6th"}
    dictRecord2 = {"galaxy": "Milky Way", "diameter": "105k light years"}
    listRecords = [{"planet": "Mercury", "location": "1st"},
                   {"planet": "Venus", "location": "2nd"},
                   {"planet": "Earth", "location": "3rd"},
                   {"planet": "Mars", "location": "4th"},
                   {"planet": "Jupiter", "location": "5th"}]

    def __init__(self):
        print("Create")

    #Initial MySQL Test Cases
    def df_Test_1_CreateTempFile(self, inputBytes: b''):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        dbClass = DatabaseClass("Test-1-CreateTempFile")
        dbClass.createTempFile()
        print(dbClass.getTempFileName())
        dbClass.writeTempFileName(inputBytes)
        print(dbClass.readTempFileName().decode("utf-8"))
        dbClass.closeTempFile()

    def df_Test_2_MySQL_Connection(self, databaseName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create mySQLDB Object.
        self.mySqlDB = MySQLClass("localhost", "root", "");
        # Select a DB and connect to it.
        print(self.mySqlDB.mysqlConnectDataBase(databaseName))

    def df_Test_3_MySQL_Description_InstanceCount(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Print mysqlDB Description
        print(self.mySqlDB.getDescription())
        # Print Total DB count regardless of type of DB
        print("Total DB Count=" + str(self.mySqlDB.getInstanceCount()))

    def df_Test_4_MySQL_Show_Databases(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        self.mySqlDB.getMySqlShowDatabases()

    def df_Test_5_Mysql_ExecuteQuery_Show_Tables(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # List all the tables in mysql DB
        result = self.mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
        for tables in result:
            print(tables[0])
        print("Total Tables Result Size = " + str(result.__len__()))

    def df_Test_6_Mysql_ExecuteQuery_Basic_Query(self, sqlStr: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # List records retrieve from Database Query.
        result = self.mySqlDB.mysqlExecuteQuery(sqlStr)
        for rows in result:
            print((rows[0]).decode("utf8"))
        print("Total Rows Result Size = " + str(result.__len__()))

    def df_Test_7_MysqlExecuteQuery_SwitchDBs(self,databaseName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Connect to new DB and show tables for it.
        self.mySqlDB.mysqlConnectDataBase(databaseName)
        result = self.mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
        for tables in result:
            print(tables[0])
        print("Table Total Length = " + str(result.__len__()))

    def df_Test_8_MysqlCreateDataBaase(self, newDatabaseName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create database DataFleaker if it don't exist
        if (self.mySqlDB.mysqlCreateDataBase(newDatabaseName)):
            print("SUCCESS CREATING DB")
        else:
            print("NO SUCCESS. DB Already Exist")

    #Initial MongoDB Test Cases
    def df_Test_1000_MongoDBCreateMongoDB(self,
                                           mongoServerAddress: str,
                                           dbName: str,
                                           collectionTableName: str,
                                           dictRecord: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create mongoDB Object
        self.mongoDBClass = MongoDBClass(mongoServerAddress)
        mongoDatabase = self.mongoDBClass.mongoConnectDataBase(dbName)
        mongoResult = self.MongoDBClass.mongoInsertOneRecord(collectionTableName, dictRecord)
        print(mongoResult)

    def df_Test_1000_MongoDBCreateMongoDB(self,
                                           mongoServerAddress: str,
                                           dbName: str,
                                           collectionTableName: str,
                                           dictRecord: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create mongoDB Object
        self.mongoDBClass = MongoDBClass(mongoServerAddress)
        mongoDatabase = self.mongoDBClass.mongoConnectDataBase(dbName)
        mongoResult = self.mongoDBClass.mongoInsertOneRecord(collectionTableName, dictRecord)
        print(mongoResult)

    def df_Test_1001_MongoDBInsertManyRecords(self, collectionTableName: str, listRecords: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoInsertManyRecords(collectionTableName, listRecords)
        print(mongoResult)

    def df_Test_1002_MongoDBFindOneRecord(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindOne(collectionTableName)
        print(mongoResult)

    def df_Test_1003_MongoDBFindManyRecords(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindAll(collectionTableName)
        print(mongoResult)

    def df_Test_1004_MongoDB(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        specificFields = {"_id": 0, "planet": 1, "location": 1}
        mongoResult = self.mongoDBClass.mongoFindAllSpecificFields(collectionTableName, specificFields)
        for dbRows in mongoResult:
            print(dbRows)






