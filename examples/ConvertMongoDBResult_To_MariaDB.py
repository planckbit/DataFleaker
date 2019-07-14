#!/usr/bin/python3

# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

from DatabaseClass import DatabaseClass
from MariaDBClass import MariaDBClass, MySQLEngineTypes
from MongoDBClass import MongoDBClass
from DataFleakerClass import DataFleakerClass

mongoServerAddress = "mongodb://localhost:27017"
dbName = "Universe_2"
collectionTableName = "Galaxies_2"
dictRecord = {"galaxy": "Milky Way", "diameter": "105k light years"}

listRecords = [{"galaxy": "Milky Way", "diameter": "105k light years"},
               {"galaxy": "Andromeda", "diameter": "220k light years"},
               {"galaxy": "Butterfly", "diameter": "1.5 light years"},
               {"galaxy": "Cigar", "diameter": "37k light years"},
               {"galaxy": "Pinwheel", "diameter": "170k light years"}]

# Initial Maria DB Connection Instance.
mariaDBClassInstance = MariaDBClass("localhost", "root", "")

# Connect to Maria, but select no DB.
mariaDBClassInstance.mysqlConnect()

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
dataFleakerClassInstance.setMySQLClassObjectToFleaker(mariaDBClassInstance)
# Perform the magic, convert MongoDB results to a Maria DB.
dataFleakerClassInstance.dataFleakerMongoToMySQLMaria(collectionTableName,
                                                      mongoDBClassInstance.mongoFindAll(collectionTableName),
                                                      MySQLEngineTypes.INNODB.value)

# Drop the Database. Uncomment to start fresh.
mongoDBClassInstance.mongoDropDataBase(dbName)