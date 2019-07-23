# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

# import pymysql
from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass, MySQLEngineTypes

# Inherit from MySQLClass
class MariaDBClass(MySQLClass):
    mariaDBInstanceCount = 0

    def __init__(self,
                 host: str,
                 userName: str,
                 passWord: str):
        DatabaseClass.__init__(self, "Maria Database")
        MariaDBClass.mariaDBInstanceCount += 1
        self.mariaInstanceID = DatabaseClass.instanceSeedID
        self.host = host
        self.userName = userName
        self.passWord = passWord

    def getMariaDBClassInstanceCount(self):
        return MariaDBClass.mariaDBInstanceCount

    def getMariaDBClassInstanceID(self):
        return self.mariaInstanceID

    def __del__(self):
        MariaDBClass.mariaDBInstanceCount -= 1
        DatabaseClass.__del__(self, self.description, self.mariaInstanceID)