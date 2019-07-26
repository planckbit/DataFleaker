#!/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass, MySQLEngineTypes
from MongoDBClass import MongoDBClass
from DataFleakerClass import DataFleakerClass

mongoServerAddress = "mongodb://localhost:27017"
dbName = "Universe"
collectionTableName = "Galaxies"
dictRecord = {"galaxy": "Milky Way", "diameter": "105k light years"}

listRecords = [{"galaxy": "Milky Way", "diameter": "105k light years"},
               {"galaxy": "Andromeda", "diameter": "220k light years"},
               {"galaxy": "Butterfly", "diameter": "1.5 light years"},
               {"galaxy": "Cigar", "diameter": "37k light years"},
               {"galaxy": "Pinwheel", "diameter": "170k light years"}]

# Initial MySQL/Maria DB Connection Instance.
mySqlDBClassInstance = MySQLClass("localhost", "root", "")
# For local docker testing
#mySqlDBClassInstance = MySQLClass("172.17.0.2", "root", "mypassword")

# Connect to Mysql, but select no DB.
mySqlDBClassInstance.mysqlConnect()

# Create Mongo DB Universe , Collection Galaxies, and Add one record for creation.
mongoDBClassInstance = MongoDBClass(mongoServerAddress)
mongoDBClassInstance.mongoConnectDataBase(dbName)
mongoDBClassInstance.mongoInsertOneRecord(collectionTableName, dictRecord)
# Insert a few records.
mongoDBClassInstance.mongoInsertManyRecords(collectionTableName, listRecords)

# Convert MongoDB Query Result to a MySQL Database
dataFleakerClassInstance = DataFleakerClass("DataFleaker Instance")
# Set the DB object instances where we want DataFleaker to do the result conversion
dataFleakerClassInstance.setMongoClassObjectToFleaker(mongoDBClassInstance)
dataFleakerClassInstance.setMySQLClassObjectToFleaker(mySqlDBClassInstance)
# Perform the magic, convert MongoDB results to a MySQL DB.
dataFleakerClassInstance.dataFleakerMongoToMySQLMaria(collectionTableName,
                                                 mongoDBClassInstance.mongoFindAll(collectionTableName),
                                                 MySQLEngineTypes.MYISAM.value)

# Drop the Database. Uncomment to start fresh.
#mongoDBClassInstance.mongoDropDataBase(dbName)