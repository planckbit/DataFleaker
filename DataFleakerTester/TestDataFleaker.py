#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

from DataFleakerTester import DataFleakerTester

testDataFleaker = DataFleakerTester()
testDataFleaker.df_Test_1_CreateTempFile(b'Hello DataFleaker')

# Basic Testing of MySQLClass functionality.
testDataFleaker.df_Test_2_MySQL_Connection("mysql")
testDataFleaker.df_Test_3_MySQL_Description_InstanceCount()
testDataFleaker.df_Test_4_MySQL_Show_Databases()
testDataFleaker.df_Test_5_Mysql_ExecuteQuery_Show_Tables()
testDataFleaker.df_Test_6_Mysql_ExecuteQuery_Basic_Query("SELECT * FROM user WHERE user='root'")
testDataFleaker.df_Test_7_MysqlExecuteQuery_SwitchDBs("test")
testDataFleaker.df_Test_8_MysqlCreateDataBaase("DataFleaker")


# Basic Testing of MongoDBClass functionality


