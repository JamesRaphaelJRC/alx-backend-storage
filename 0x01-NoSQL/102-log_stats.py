#!/usr/bin/env python3
''' Defines a function that provides stats of Nginx logs '''
from pymongo import MongoClient


def provide_stats():
    ''' Provides some stats about NGINX logs stored in MongoDB '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    stats = ""

    stats += "{} logs\nMethods:\n".format(nginx_collection.count_documents({}))

    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        stats += '\tmethod {}: {}\n'.format(method, method_count)
    stats += "{} status check".format(
            nginx_collection.count_documents({"path": "/status"}))
    stats += '\nIPs:\n'
    top_ips = nginx_collection.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}])
    for ip in top_ips:
        stats += '\t{}: {}\n'.format(ip.get('_id'), ip.get('count'))
    print(stats, end='')


if __name__ == '__main__':
    provide_stats()
