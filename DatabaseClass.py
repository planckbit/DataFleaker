#Author: PlanckBit
#MIT License
#Copyright (c) 2019 PlanckBit

import random

class DatabaseClass:
    #Keep track of total instances.
    instanceCount = 0
    #Used for creating a unique instance ID
    instanceSeedID=99
    
    def __init__(self, description):
        DatabaseClass.instanceCount += 1
        DatabaseClass.instanceSeedID = random.randint(DatabaseClass.instanceSeedID+1,
                                                      DatabaseClass.instanceSeedID+100)
        self.description = description
        
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description

    def getInstanceCount(self):
        return DatabaseClass.instanceCount
    
    def __del__(self, description, instanceID):
        print("Deleted - "+description+" InstanceID="+str(instanceID))
        DatabaseClass.instanceCount -= 1


