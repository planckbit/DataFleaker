#!/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import inspect
import os

from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass
from MariaDBClass import MariaDBClass
from MongoDBClass import MongoDBClass
from SQLite3Class import SQLite3Class
from DataFleakerClass import DataFleakerClass

class DataFleakerTesterClass:
    inputBytes = b'Hello DataFleaker'
    mongoServerAddress = "mongodb://localhost:27017"
    dbName = "PlanetsDB"
    dbTable = "PlanetLocations"
    dbColumns = "(id INT NOT NULL, name VARCHAR(20))"
    collectionTableName = "Planets"
    collectionTableName2 = "Galaxies"
    dictRecord = {"planet": "Saturn", "location": "6th"}
    dictRecord2 = {"galaxy": "Milky Way", "diameter": "105k light years"}
    listRecords = [{"planet": "Mercury", "location": "1st"},
                   {"planet": "Venus", "location": "2nd"},
                   {"planet": "Earth", "location": "3rd"},
                   {"planet": "Mars", "location": "4th"},
                   {"planet": "Jupiter", "location": "5th"}]

    specificFields = {"_id": 0, "planet": 1, "location": 1}
    filterQuery = {"planet": "Mars"}
    deleteOneRecordQuery = {"location": "3rd"}
    deleteManyQuery = {"planet": {"$regex": "^M"}}
    findAllLimit = 5

    def __init__(self):
        print("Create DataFleakerTester Instance")

    # Initial MySQL Test Cases
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
        self.mySqlDB = MySQLClass("localhost", "root", "")
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

    def df_Test_8_MysqlCreateDataBase(self, newDatabaseName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create database DataFleaker
        self.mySqlDB.mysqlCreateDataBase(newDatabaseName)

    def df_Test_9_MysqlCreateDataBaseTable(self,
                                           dataBaseTableName: str,
                                           dataBaseTableColumns: str,
                                           dataBaseEngineType: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        print(dataBaseTableName)
        print(dataBaseTableColumns)
        print(dataBaseEngineType)
        self.mySqlDB.mysqlCreateDatabaseTable(dataBaseTableName,
                                              dataBaseTableColumns,
                                              dataBaseEngineType)


    # Initial MariaDB Test Cases
    def df_Test_500_MariaDB_Connection(self, databaseName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create mariaDB Object.
        self.mariaDB = MariaDBClass("localhost", "root", "")
        # Select a DB and connect to it.
        print(self.mariaDB.mysqlConnectDataBase(databaseName))

    def df_Test_501_MariaDB_Description_InstanceCount(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Print mariaDB Description
        print(self.mariaDB.getDescription())
        # Print Total DB count regardless of type of DB
        print("Total DB Count=" + str(self.mariaDB.getInstanceCount()))

    def df_Test_502_MariaDB_Show_Databases(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        self.mariaDB.getMySqlShowDatabases()

    # Initial MongoDB Test Cases
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

    def df_Test_1001_MongoDBInsertManyRecords(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoInsertManyRecords(collectionTableName, DataFleakerTesterClass.listRecords)
        print(mongoResult)

    def df_Test_1002_MongoDBFindOneRecord(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindOne(collectionTableName)
        print(mongoResult)

    def df_Test_1003_MongoDBFindManyRecords(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindAll(collectionTableName)
        print(mongoResult)

    def df_Test_1004_MongoDBFindAllSpecificFields(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindAllSpecificFields(collectionTableName,
                                                                   DataFleakerTesterClass.specificFields)
        for dbRows in mongoResult:
            print(dbRows)

    def df_Test_1005_MongoDBFindAllFilter(self, collectionTableName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindAllFilter(collectionTableName, DataFleakerTesterClass.filterQuery)
        for dbRows in mongoResult:
            print(dbRows)

    def df_Test_1006_PrintMongoShowDatabases(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        self.mongoDBClass.printMongoShowDatabases()

    def df_Test_1007_GetMongoShowDatabases(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoDBList = self.mongoDBClass.getMongoShowDatabases()
        for dbs in mongoDBList:
            print(dbs)

    def df_Test_1008_MongoDropDatabase(self, dbName: str):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        self.mongoDBClass.mongoDropDataBase(dbName)

    def df_Test_1009_MongoDeleteOneRecord(self, collectionTableName):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoDeleteOneRecord(collectionTableName, DataFleakerTesterClass.deleteOneRecordQuery)
        print(mongoResult)

    def df_Test_1010_MongoDeleteManyRecords(self, collectionTableName):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Delete many records starting with planet name letter 'M'
        mongoResult = self.mongoDBClass.mongoDeleteManyRecords(collectionTableName, DataFleakerTesterClass.deleteManyQuery)
        print(mongoResult.deleted_count)

    def df_Test_1011_MongoFindAllWithLimit(self, collectionTableName):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        mongoResult = self.mongoDBClass.mongoFindAll(collectionTableName, DataFleakerTesterClass.findAllLimit)
        for dbRows in mongoResult:
            print(dbRows)

    # Initial SQLite3Class Test Cases
    def df_Test_2000_SQLite3ConnectQuery(self):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        # Create SQLite3 Object.
        sqlite3DBFileLocation = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
        sqlite3DB = SQLite3Class(sqlite3DBFileLocation)
        sqlite3DB.sqlite3ConnectDataBase()
        sqlStr = "SELECT host_key, name, value, encrypted_value FROM cookies"
        sqlite3Result = sqlite3DB.sqlite3ExecuteQuery(sqlStr)
        for dbRows in sqlite3Result:
            print(dbRows)

    # Initial DataFleakerClass Testing.
    def df_Test_3000_DataFleakerMongoToMySQL(self, collectionTable):
        DatabaseClass.printClassFunctionName(self.__class__.__name__, inspect.stack()[0][3])
        self.dataFleakerClass = DataFleakerClass("DataFleaker Instance")
        self.dataFleakerClass.setMongoClassObjectToFleaker(self.mongoDBClass)
        self.dataFleakerClass.setMySQLClassObjectToFleaker(self.mySqlDB)
        return self.dataFleakerClass.dataFleakerMongoToMySQL(collectionTable,
                                                             self.mongoDBClass.mongoFindAll(DataFleakerTesterClass.collectionTableName),
                                                             MySQLClass.MYISAM)





