#!/usr/bin/env python3
''' Defines a function '''


def list_all(mongo_collection):
    ''' Lists all documents in a mongoDB collection 

        mongo_collection: The collection ( a pymongo collection object )
    '''
    return mongo_collection.find()
