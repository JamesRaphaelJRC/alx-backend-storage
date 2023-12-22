#!/usr/bin/env python3
''' Defines a schools_by_topic function '''
from pymongo import MongoClient
from typing import List


def schools_by_topic(mongo_collection: MongoClient, topic: str) ->\
                    List[object]:
    ''' Returns a list of school having a specific topic '''
    return mongo_collection.find({"topics": topic})
