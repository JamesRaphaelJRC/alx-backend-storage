#!/usr/bin/env python3
''' Defines a function '''
from pymongo import MongoClient
from typing import Iterator


def list_all(mongo_collection: MongoClient) -> Iterator:
    ''' Lists all documents in a mongoDB collection 

        mongo_collection: The collection ( a pymongo collection object )
    '''
    return mongo_collection.find()
