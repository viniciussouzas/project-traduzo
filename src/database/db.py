from pymongo import MongoClient
from os import environ


client = MongoClient(environ.get('MONGO_URI') or 'mongodb://localhost:27017/')

db = client[environ.get('DB_NAME') or 'test_db_traduzo']
