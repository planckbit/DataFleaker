# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import sqlite3
from DatabaseClass import DatabaseClass

class SQLite3Class(DatabaseClass):
    sqlite3DBInstanceCount = 0

    def __init__(self, dataBaseFileLocation: str):
        DatabaseClass.__init__(self, "SQLite3 Database")
        SQLite3Class.sqlite3DBInstanceCount += 1
        self.sqlite3InstanceID = DatabaseClass.instanceSeedID
        self.dataBaseFileLocation = dataBaseFileLocation

    def sqlite3ConnectDataBase(self):
        self.dbConnectorConnect = sqlite3.connect(self.dataBaseFileLocation)
        return self.dbConnectorConnect

    def sqlite3ExecuteQuery(self, strSQL: str):
        self.cursor = self.dbConnectorConnect.cursor()
        self.cursor.execute(strSQL)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result
