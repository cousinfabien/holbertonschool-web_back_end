#!/usr/bin/env python3
"""
This module provides a script that displays stats about Nginx logs in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Accès à la collection logs.nginx
    nginx_collection = client.logs.nginx

    # Nombre total de documents
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Stats pour les méthodes
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check (method=GET, path=/status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()
