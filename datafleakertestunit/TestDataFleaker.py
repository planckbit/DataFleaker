#!/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit
import os
from DataFleakerTesterClass import DataFleakerTesterClass
from MySQLClass import MySQLEngineTypes

# Basic temp file creation for fast csv exporting and importing.
# will be used for converting one DB to Another.
testDataFleaker = DataFleakerTesterClass()
testDataFleaker.df_Test_1_CreateTempFile(DataFleakerTesterClass.inputBytes)

# Basic Testing of MySQLClass functionality.
testDataFleaker.df_Test_2_MySQL_Connection("mysql")
testDataFleaker.df_Test_3_MySQL_Description_InstanceCount()
testDataFleaker.df_Test_4_MySQL_Show_Databases()
testDataFleaker.df_Test_5_Mysql_ExecuteQuery_Show_Tables()
testDataFleaker.df_Test_6_Mysql_ExecuteQuery_Basic_Query("SELECT * FROM user")
testDataFleaker.df_Test_8_MysqlCreateDataBase("DataFleaker")
testDataFleaker.df_Test_7_MysqlExecuteQuery_SwitchDBs("DataFleaker")
testDataFleaker.df_Test_9_MysqlCreateDataBaseTable(testDataFleaker.dbTable,
                                                   testDataFleaker.dbColumns,
                                                   MySQLEngineTypes.MYISAM.value)
# Basic MariaDBClass Testing
testDataFleaker.df_Test_500_MariaDB_Connection("information_schema")
testDataFleaker.df_Test_501_MariaDB_Description_InstanceCount()
testDataFleaker.df_Test_502_MariaDB_Show_Databases()

# Basic Testing of MongoDBClass functionality
testDataFleaker.df_Test_1000_MongoDBCreateMongoDB(DataFleakerTesterClass.mongoServerAddress,
                                                  DataFleakerTesterClass.dbName,
                                                  DataFleakerTesterClass.collectionTableName,
                                                  DataFleakerTesterClass.dictRecord)

testDataFleaker.df_Test_1001_MongoDBInsertManyRecords(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1002_MongoDBFindOneRecord(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1003_MongoDBFindManyRecords(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1004_MongoDBFindAllSpecificFields(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1005_MongoDBFindAllFilter(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1006_PrintMongoShowDatabases()
testDataFleaker.df_Test_1007_GetMongoShowDatabases()
# Uncomment to drop DB.
testDataFleaker.df_Test_1008_MongoDropDatabase(DataFleakerTesterClass.dbName)
testDataFleaker.df_Test_1009_MongoDeleteOneRecord(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1010_MongoDeleteManyRecords(DataFleakerTesterClass.collectionTableName)
testDataFleaker.df_Test_1011_MongoFindAllWithLimit(DataFleakerTesterClass.collectionTableName)


# Basic Testing of SQLite3Class functionality
#testDataFleaker.df_Test_2000_SQLite3ConnectQuery()

# Basic DataFleaker Testing.
testDataFleaker.df_Test_3000_DataFleakerMongoToMySQL(DataFleakerTesterClass.collectionTableName)
