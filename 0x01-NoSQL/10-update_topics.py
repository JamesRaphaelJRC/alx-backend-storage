#!/usr/bin/env python3
''' Defines an update_topics function '''
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    ''' Changes all topics of a school document based on the name '''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
