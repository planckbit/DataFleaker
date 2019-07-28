# DataFleaker  [![Build Status](https://travis-ci.org/planckbit/DataFleaker.svg?branch=master)](https://travis-ci.org/planckbit/DataFleaker) [![Coverage Status](https://coveralls.io/repos/github/planckbit/DataFleaker/badge.svg?branch=master&service=github)](https://coveralls.io/github/planckbit/DataFleaker?branch=master)<img align="right" width="130" height="200" src="images/datafleaker.png"> [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.6.8](https://img.shields.io/badge/python-3.6.8-blue.svg)](https://www.python.org/downloads/release/python-368/)

## DataFleaker - Instantly Convert Query Results Sets From Mongo DB to MySQL DB or Maria DB and Vice Versa.

## Description
DataFleaker provides a robust simple object based API that allows the developer to query 
Mongo(NoSQL) or MySQL/Maria databases and convert the results instantly to another database, specifically between NoSQL 
and SQL  database management systems and vice versa. This allows developers the flexibility to use the additional 
services in specific DBMS when converting from one to the other for their application development. 

For example, converting a result set return by a NoSQL DB such as Mongo which is in JSON format directly into a
MySQL/MariaDB Database as a native JSON field in the table. Then using MySQL/Maria's built in native JSON feature
to query this new result set from the newly created DB. This conversion to MySQL/Maria helps verify document validation,
convenience, and efficient access through the available [JSON Functions](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html)
in MySQL/Maria.  The conversion of MySQL/MariaDB query results to Mongo DB is also supported. 

## Early Prototype Features:
    * Current support for creating specific Class Objects for MongoDB, MySQLDB, MariaDB and SQLite3.
      This allows specific DB class objects to be passed into the DataFleaker for data result sets to be
      converted on the fly through one of the DataFleakers member APIs.
    * Current support for connecting to MongoDB, MySqlDB, MariaDB, and SQLite3 through the object instances.
    * Current support for executing basic queries(DB Creation, Tables/Collections, and simple queries)
      on MongoDB, MySQLDB, MariaDB, and SQLite3.
    * Current support for converting a MongoDB result set(JSON format) to a New DB with JSON Type field
      in MySQL/MariaDB. 
    * New support for converting simple result MariaDB or MysqlDB queries to MongoDB. 
      See examples/ConvertMariaDBResult_To_MongoDB.py
    * Added bulk insert capability for MongoDB to MySQL/Maria DB for faster conversion.
      
 ## Tested with:
    * python3.X
    * pip3 install mysql-connector-python
    * XAMPP 7.3.6 - Running 10.3.16-MariaDB or MySQL 8.0.17 
    * MongoDB - Running v4.0.10
    * Linux Distro: 
        Ubuntu 18.04.2 LTS
        4.15.0-54-generic #58-Ubuntu SMP Mon Jun 24 10:55:24 UTC 2019
        x86_64 x86_64 x86_64 GNU/Linux
    
## Get Started:
    ~/Development/python/workroot$ git clone git@github.com:planckbit/DataFleaker.git
    ~/Development/python/workroot$ cd DataFleaker
    ~/Development/python/workroot/DataFleaker$ PYTHONPATH=~/Development/python/workroot/DataFleaker
    ~/Development/python/workroot/DataFleaker$ export PYTHONPATH
    ~/Development/python/workroot/DataFleaker$ cd examples/
    ~/Development/pythong/workroot/DataFleaker/examples$ chmod 755 ConvertMongoDBResult_To_MySqlDB.py
    ~/Development/python/workroot/DataFleaker/examples$ ./ConvertMongoDBResult_To_MySqlDB.py
   
   <b>Example-1: Simple Mongo DB query result converted to MySQL DB.</b>
     
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
    
    # Connect to Mysql, but select no DB.
    mySqlDBClassInstance.mysqlConnect()

    # Create Mongo DB Universe , Collection Galaxies, and Add one record for creation.
    mongoDBClassInstance = MongoDBClass(mongoServerAddress)
    mongoDBClassInstance.mongoConnectDataBase(dbName)
    mongoDBClassInstance.mongoInsertOneRecord(collectionTableName, dictRecord)
    # Insert a few records.
    mongoDBClassInstance.mongoInsertManyRecords(collectionTableName, listRecords)

    # Create dataFleaker instance for converting MongoDB query result to a MySQL database
    dataFleakerClassInstance = DataFleakerClass("DataFleaker Instance")
    # Set the DB object instances where we want DataFleaker to do the result conversion
    dataFleakerClassInstance.setMongoClassObjectToFleaker(mongoDBClassInstance)
    dataFleakerClassInstance.setMySQLClassObjectToFleaker(mySqlDBClassInstance)
    # Convert Mongo DB results to a MySQL DB.
    dataFleakerClassInstance.dataFleakerMongoToMySQLMaria(collectionTableName,
                                                        mongoDBClassInstance.mongoFindAll(collectionTableName),
                                                        MySQLEngineTypes.MYISAM.value,
                                                        True)
 
## Output:
    /usr/bin/python3.6 DataFleaker/examples/ConvertMongoDBResult_To_MySqlDB.py
    Creating Database Universe
    Deleted - MySQL Database InstanceID=155
    Deleted - Mongo Database InstanceID=209
## MongoDB Results
<p align="left">
    <img width="950" height="300" src="images/mongo_client_universe_galaxy.png">
</p>    

## MySQL/MariaDB Results
<p align="left">
    <img width="650" height="400" src="images/mongo_convert_to_mysql.png">
</p>

   <b>Example-2: Simple Maria DB query result converted to MongoDB.</b>
   
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

    # Create dataFleaker instance for Converting Maria DB Query Result to a Mongo database
    dataFleakerClassInstance = DataFleakerClass("DataFleaker Instance")
    # Set the DB object instances where we want DataFleaker to do the result conversion
    dataFleakerClassInstance.setMongoClassObjectToFleaker(mongoDBClassInstance)
    dataFleakerClassInstance.setMySQLClassObjectToFleaker(mariaDBClassInstance)

    # Convert Maria DB to Mongo DB.
    dataFleakerClassInstance.dataFleakerMySQLMariaToMongoDB("user", result)

## Mongo DB Results - User query from mysql DB converted to Mongo DB.
<p align="left">
    <img width="950" height="450" src="images/maria_convert_to_mongo.png">
</p>   
   

## Final Thoughts
    If you have any questions, ideas or pull request you like to contribute and see implemented you can 
    email me at planckbit@att.net.
    
## License

Copyright (c) 2019 PlanckBit. MIT Licensed

