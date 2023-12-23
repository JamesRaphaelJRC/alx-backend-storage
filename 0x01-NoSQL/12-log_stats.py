#!/usr/bin/env python3
''' Defines a function that provides stats of Nginx logs '''
from pymongo import MongoClient


def provide_stats():
    ''' Provides some stats about NGINX logs stored in MongoDB '''
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    number_of_logs = nginx_collection.count_documents({})

    num_GET_method = nginx_collection.count_documents({"method": "GET"})
    num_POST_method = nginx_collection.count_documents({"method": "POST"})
    num_PUT_method = nginx_collection.count_documents({"method": "PUT"})
    num_PATCH_method = nginx_collection.count_documents({"method": "PATCH"})
    num_DELETE_method = nginx_collection.count_documents({"method": "DELETE"})

    num_GET_path_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    output = f"{number_of_logs} logs\n\
Methods:\n\
    \tmethod GET: {num_GET_method}\n\
    \tmethod POST: {num_POST_method}\n\
    \tmethod PUT: {num_PUT_method}\n\
    \tmethod PATCH: {num_PATCH_method}\n\
    \tmethod DELETE: {num_DELETE_method}\n\
{num_GET_path_status} status check\
    "
    print(output)


if __name__ == '__main__':
    provide_stats()
