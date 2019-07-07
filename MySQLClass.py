import pymysql
import mysql.connector
from DatabaseClass import DatabaseClass

class MySQLClass(DatabaseClass):
    mysqlDBInstanceCount = 0
    
    def __init__(self, host, userName, passWord):
        DatabaseClass.__init__(self, "MySQL Database")
        MySQLClass.mysqlDBInstanceCount += 1
        self.mysqlInstanceID = DatabaseClass.instanceSeedID
        self.host = host
        self.userName = userName
        self.passWord = passWord
        
    def mysqlConnectDataBase(self, databaseName):
        self.databaseName = databaseName
        self.dbConnectorConnect = mysql.connector.connect(user=self.userName, password=self.passWord, host=self.host, database=self.databaseName)

    def mysqlCreateDataBase(self, databaseName):
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

    def mysqlExecuteQuery(self, strSQL):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute(strSQL)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

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
