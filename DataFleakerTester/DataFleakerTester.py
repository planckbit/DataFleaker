# !/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass

class DataFleakerTester:

    def __init__(self):
        print("Create")

    def df_Test_1_CreateTempFile(self):
        dbClass = DatabaseClass("Test-1-CreateTempFile")
        dbClass.createTempFile()
        print(dbClass.getTempFileName())
        dbClass.writeTempFileName()
        print(dbClass.readTempFileName().decode("utf-8"))
        dbClass.closeTempFile()

    def df_Test_2_MySQL_Connection(self, databaseName: str):
        # Create mySQLDB Object.
        self.mySqlDB = MySQLClass("localhost", "root", "");
        # Select a DB and connect to it.
        print(self.mySqlDB.mysqlConnectDataBase(databaseName))

    def df_Test_3_MySQL_Description_InstanceCount(self):
        # Print mysqlDB Description
        print(self.mySqlDB.getDescription())
        # Print Total DB count regardless of type of DB
        print("Total DB Count=" + str(self.mySqlDB.getInstanceCount()))

    def df_Test_4_MySQL_Show_Databases(self):
        self.mySqlDB.getMySqlShowDatabases()

    def df_Test_5_Mysql_ExecuteQuery_Show_Tables(self):
        # List all the tables in mysql DB
        result = self.mySqlDB.mysqlExecuteQuery("SHOW TABLES;")
        for tables in result:
            print(tables[0])
        print("result size = " + str(result.__len__()))




