# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

# import pymysql
import mysql.connector
from DatabaseClass import DatabaseClass

class MySQLClass(DatabaseClass):
    mysqlDBInstanceCount = 0
    
    def __init__(self,
                 host: str,
                 userName: str,
                 passWord: str):
        DatabaseClass.__init__(self, "MySQL Database")
        MySQLClass.mysqlDBInstanceCount += 1
        self.mysqlInstanceID = DatabaseClass.instanceSeedID
        self.host = host
        self.userName = userName
        self.passWord = passWord

    def mysqlConnect(self):
        self.dbConnectorConnect = mysql.connector.connect(user=self.userName,
                                                          password=self.passWord,
                                                          host=self.host)
        
    def mysqlConnectDataBase(self, databaseName: str):
        self.databaseName = databaseName
        self.dbConnectorConnect = mysql.connector.connect(user=self.userName,
                                                          password=self.passWord,
                                                          host=self.host,
                                                          database=self.databaseName)
        return self.dbConnectorConnect.connection_id

    def mysqlCreateDataBase(self, databaseName: str):
        ret = True
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute("SHOW DATABASES LIKE '"+databaseName+"'")
        results = self.cursor.fetchall()

        if results.__len__() == 0 :
            print("Creating Database "+databaseName)
            self.cursor.execute("CREATE DATABASE "+databaseName)
        else:
            print("Database "+databaseName+" Exist")
            ret = False
        self.cursor.close()
        return ret

    def mysqlCreateDatabaseTable(self, databaseTableName: str, columnNames: str = ""):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute("CREATE TABLE "+databaseTableName+" "+columnNames)

    def mySQLCreateDatabaseTableJsonType(self, databaseTableName: str):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute("CREATE TABLE " + databaseTableName + " (id INT NOT NULL AUTO_INCREMENT,json_record JSON, PRIMARY KEY (id));")

    def mysqlExecuteQuery(self, strSQL: str):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute(strSQL)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def mysqlExecuteInsert(self, strSQL: str):
        self.cursor = self.dbConnectorConnect.cursor()
        # print(strSQL)
        # print(strValues)
        self.cursor.execute(strSQL)
        self.dbConnectorConnect.commit()
        self.cursor.close()

    #Todo:Test this out. Need better version
    def mysqlExecuteInsertUsingValues(self, strSQL: str, strValues: str):
        self.cursor = self.dbConnectorConnect.cursor()
        #print(strSQL)
        #print(strValues)
        self.cursor.execute(strSQL, strValues)
        self.dbConnectorConnect.commit()
        self.cursor.close()

    def getMySqlShowDatabases(self):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute("SHOW DATABASES")
        for dbs in self.cursor:
            print(dbs)
        self.cursor.close()
        
    def getMySqlClassInstanceCount(self):
        return MySQLClass.mysqlDBInstanceCount
    
    def getMySqlClassInstanceID(self):
        return self.mysqlInstanceID
    
    def __del__(self):
        MySQLClass.mysqlDBInstanceCount -= 1
        DatabaseClass.__del__(self, self.description, self.mysqlInstanceID)

