from pymongo import MongoClient

client = MongoClient('localhost', 27017)

def startCollection(collectionName):
  return client[collectionName]
