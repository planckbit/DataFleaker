#!/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

from DatabaseClass import DatabaseClass
from MariaDBClass import MariaDBClass, MySQLEngineTypes
from MongoDBClass import MongoDBClass
from DataFleakerClass import DataFleakerClass

mongoServerAddress = "mongodb://localhost:27017"

# Initial Maria DB Connection Instance.
mariaDBClassInstance = MariaDBClass("localhost", "root", "")

# Create MariaDBClass instance, Connect and select a Database.
mariaDBClassInstance.mysqlConnect()
mariaDBClassInstance.mysqlConnectDataBase("mysql")
# Execute simple select query
result = mariaDBClassInstance.mysqlExecuteQuery("SELECT * FROM user")

# Create MongoDBClass instance, Connect and select a Database.
mongoDBClassInstance = MongoDBClass(mongoServerAddress)

# Convert mariaDB Query Result to a Mongo Database
dataFleakerClassInstance = DataFleakerClass("DataFleaker Instance")
# Set the DB object instances where we want DataFleaker to do the result conversion
dataFleakerClassInstance.setMongoClassObjectToFleaker(mongoDBClassInstance)
dataFleakerClassInstance.setMySQLClassObjectToFleaker(mariaDBClassInstance)

# Perform the magic, convert Maria DB to MongoDB.
dataFleakerClassInstance.dataFleakerMySQLMariaToMongoDB("user", result)

# Drop the Database. Uncomment to start fresh.
#mongoDBClassInstance.mongoDropDataBase("mysql")