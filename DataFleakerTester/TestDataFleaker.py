#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

from DataFleakerTester import DataFleakerTester

# Basic temp file creation for fast csv exporting and importing.
testDataFleaker = DataFleakerTester()
testDataFleaker.df_Test_1_CreateTempFile(DataFleakerTester.inputBytes)

# Basic Testing of MySQLClass functionality.
testDataFleaker.df_Test_2_MySQL_Connection("mysql")
testDataFleaker.df_Test_3_MySQL_Description_InstanceCount()
testDataFleaker.df_Test_4_MySQL_Show_Databases()
testDataFleaker.df_Test_5_Mysql_ExecuteQuery_Show_Tables()
testDataFleaker.df_Test_6_Mysql_ExecuteQuery_Basic_Query("SELECT * FROM user WHERE user='root'")
testDataFleaker.df_Test_7_MysqlExecuteQuery_SwitchDBs("test")
testDataFleaker.df_Test_8_MysqlCreateDataBaase("DataFleaker")

# Basic Testing of MongoDBClass functionality
testDataFleaker.df_Test_1000_MongoDBCreateMongoDB(DataFleakerTester.mongoServerAddress,
                                                  DataFleakerTester.dbName,
                                                  DataFleakerTester.collectionTableName,
                                                  DataFleakerTester.dictRecord)

testDataFleaker.df_Test_1001_MongoDBInsertManyRecords(DataFleakerTester.collectionTableName)
testDataFleaker.df_Test_1002_MongoDBFindOneRecord(DataFleakerTester.collectionTableName)
testDataFleaker.df_Test_1003_MongoDBFindManyRecords(DataFleakerTester.collectionTableName)
testDataFleaker.df_Test_1004_MongoDBFindAllSpecificFields(DataFleakerTester.collectionTableName)
testDataFleaker.df_Test_1005_MongoDBFindAllFilter(DataFleakerTester.collectionTableName)



