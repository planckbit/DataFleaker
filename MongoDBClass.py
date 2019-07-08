#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

import pymongo
from DatabaseClass import DatabaseClass

class MongoDBClass(DatabaseClass):
    mongoDBInstanceCount = 0

    def __init__(self, mongoDBServer):
        DatabaseClass.__init__(self, "Mongo Database")
        MongoDBClass.mongoDBInstanceCount += 1
        self.mongoDBInstanceID = DatabaseClass.instanceSeedID
        self.mongoDBServer = mongoDBServer
        self.client = pymongo.MongoClient(self.mongoDBServer)

    def mongoConnectDataBase(self, databaseName):
        self.databaseName = databaseName
        return self.client[self.databaseName]

    def mongoInsertOneRecord(self, collectionTable, dictRecord):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.insert_one(dictRecord)

    def mongoInsertManyRecords(self, collectionTable, listRecords):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.insert_many(listRecords)

    def mongoDropDataBase(self, databaseName):
        return self.client.drop_database(databaseName)

    def mongoFindOne(self, collectionTable):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find_one()

    def mongoFindAll(self, collectionTable):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find()

    def mongoFindAllSpecificFields(self, collectionTable, dictFields):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find({}, dictFields)

    def mongoFindAllFilter(self, collectionTable, dictQuery):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find(dictQuery)

    def mongoFindAllSpecificFieldsFilter(self, collectionTable, dictQuery, dictFields):
        useDB = self.client[self.databaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find(dictQuery, dictFields)

    def mongoGetCurrentDataBaseSet(self):
        return self.databaseName

    def printMongoShowDatabases(self):
        print(self.client.list_database_names())

    def getMongoShowDatabases(self):
        return self.client.list_database_names()

    def getMongoDBClassInstanceCount(self):
        return MongoDBClass.mongoDBInstanceCount

    def __del__(self):
        MongoDBClass.mongoDBInstanceCount -= 1
        DatabaseClass.__del__(self, self.description, self.mongoDBInstanceID )
