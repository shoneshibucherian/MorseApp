from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://shonecherian04:helloWorld@cluster0.4m4ic.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
db = client['database']
collection = db['BRCA']
#CSV to JSON Conversion
def sentData(json):
    collection.insert_many(json);