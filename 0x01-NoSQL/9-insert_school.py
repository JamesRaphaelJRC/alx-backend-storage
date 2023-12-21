#!/usr/bin/env python3
''' Defines an insert_school function '''
from pymongo import MongoClient
from typing import Mapping


def insert_school(mongo_collection: MongoClient, **kwargs: Mapping[str, str])\
                    -> str:
    ''' Inserts a new document in a collection based on kwards and
        returns the new _id
    '''
    # return mongo_collection.insert_One(kwargs).inserted_id
    return mongo_collection.insert_one(kwargs).inserted_id
