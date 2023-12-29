#!/usr/bin/env python3
''' Defines a function 'top_students' '''
from pymongo import MongoClient
from typing import List


def top_students(mongo_collection: MongoClient):
    '''
    Returns all students sorted by average score

    Arguments:
        mongo_collection: A pymongo collection object
    '''
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}
    ])
