import pymongo
from DatabaseClass import DatabaseClass

class MongoDBClass(DatabaseClass):
    mongoDBInstanceCount = 0
    def __init__(self, mongoDBServer):
        DatabaseClass.__init__(self, "Mongo Database Instance")
        MongoDBClass.mongoDBInstanceCount += 1
        self.mongoDBServer = mongoDBServer
        self.client = pymongo.MongoClient(mongoDBServer)

    def mongoConnectDataBase(self, databaseName):
        self.databaseName = databaseName
        self.dbConnectorConnect = pymongo.MongoClient(self.mongoDBServer)

    def getMongoShowDatabases(self):
        mongoClient = self.dbConnectorConnect = pymongo.MongoClient(self.mongoDBServer)
        print(mongoClient.list_database_names())

        
    def getMongoDBClassInstanceCount(self):
        return MongoDBClass.mongoDBInstanceCount