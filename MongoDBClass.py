# Author: PlanckBit
# MIT License
# Copyright (c) 2019 PlanckBit

import pymongo
from DatabaseClass import DatabaseClass

class MongoDBClass(DatabaseClass):
    mongoDBInstanceCount = 0

    def __init__(self, mongoDBServer: str):
        DatabaseClass.__init__(self, "Mongo Database")
        MongoDBClass.mongoDBInstanceCount += 1
        self.mongoDBInstanceID = DatabaseClass.instanceSeedID
        self.mongoDBServer = mongoDBServer
        self.client = pymongo.MongoClient(self.mongoDBServer)

    def mongoConnectDataBase(self, dataBaseName: str):
        try:
            self.dataBaseName = dataBaseName
            return self.client[self.dataBaseName]
        except pymongo.errors.ConnectionFailure:
            print(e)

    def mongoInsertOneRecord(self, collectionTable: str, dictRecord: dict):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.insert_one(dictRecord)

    def mongoInsertManyRecords(self, collectionTable: str, listRecords: list):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        result = ""
        try:
            result = useCollectionTable.insert_many(listRecords)
        except:
            print(result)

    def mongoDropDataBase(self, dataBaseName: str):
        return self.client.drop_database(dataBaseName)

    def mongoDropCollectionTable(self, collectionTable: str):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.drop()

    def mongoFindOne(self, collectionTable: str):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find_one()

    def mongoFindAll(self, collectionTable: str, limit=0):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        dictNoId = {"_id": 0}
        return useCollectionTable.find({}, dictNoId).limit(limit)

    def mongoFindAllSpecificFields(self, collectionTable: str, dictFields: dict, limit=0):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find({}, dictFields).limit(limit)

    def mongoFindAllFilter(self, collectionTable: str, dictQuery: dict, limit=0):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find(dictQuery).limit(limit)

    def mongoFindAllSpecificFieldsFilter(self, collectionTable: str, dictQuery: dict, dictFields: dict, limit=0):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.find(dictQuery, dictFields).limit(limit)

    def mongoDeleteOneRecord(self, collectionTable: str, dictQuery: dict):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.delete_one(dictQuery)

    def mongoDeleteManyRecords(self, collectionTable: str, dictQuery: dict):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.delete_many(dictQuery)

    def mongoUpdateOneRecord(self, collectionTable: str, dictQuery: dict, dictUpdate: dict):
        useDB = self.client[self.dataBaseName]
        useCollectionTable = useDB[collectionTable]
        return useCollectionTable.update(dictQuery, dictUpdate)

    def printMongoShowDatabases(self):
        print(self.client.list_database_names())

    def getMongoShowDatabases(self):
        return self.client.list_database_names()

    def getMongoDBClassInstanceCount(self):
        return MongoDBClass.mongoDBInstanceCount

    def __del__(self):
        MongoDBClass.mongoDBInstanceCount -= 1
        DatabaseClass.__del__(self, self.description, self.mongoDBInstanceID )

