#!/usr/bin/python3

#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

from DataFleakerTester import DataFleakerTester

testDataFleaker = DataFleakerTester()
testDataFleaker.df_Test_1_CreateTempFile()
testDataFleaker.df_Test_2_MySQL_Connection("mysql")
testDataFleaker.df_Test_3_MySQL_Description_InstanceCount()
testDataFleaker.df_Test_4_MySQL_Show_Databases()
testDataFleaker.df_Test_5_Mysql_ExecuteQuery_Show_Tables()

