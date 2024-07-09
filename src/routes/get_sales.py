import json
import pymongo
from flask import Blueprint, jsonify, request
from bson.json_util import dumps
from datetime import datetime
from ..mongo.pymongoServer import startCollection

collectionName = 'lizCafeteria'

get_sales_bp = Blueprint('get_sales', __name__)
@get_sales_bp.route('/getSales', methods=['GET'])
def get_sales():
  requestData = json.loads(request.args.to_dict()['query'])

  list_of_sales = get_list_of_sales(requestData)
  sorted_sale_data = get_sorted_sale_data(requestData.XAxis, list_of_sales)
  # for sale in list_of_sales:
  #   if '_id' in sale:
  #     sale['_id'] = str(sale['_id'])

  print(len(list_of_sales))
  # return jsonify(list_of_sales)
  return True

def get_list_of_sales(requestData):
    collection = startCollection(collectionName)
    salesCollection = collection['sale']
    query = {}

    if requestData['relevantTime']:
        query['date'] = {}
        
        if requestData['relevantTime']['start']:
            query['date']['$gte'] = datetime.strptime(requestData['relevantTime']['start'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if requestData['relevantTime']['start']:
            query['date']['$lte'] = datetime.strptime(requestData['relevantTime']['end'], '%Y-%m-%dT%H:%M:%S.%fZ')

    if requestData['subject']['type'] == 'byProduct':
        query['product'] = { '$in': requestData['subject']['products'] }
    if requestData['subject']['type'] == 'byCategory':
        query['product'] = { '$in': requestData['subject']['categories'] }

    return list(salesCollection.find(query).sort('hour', pymongo.ASCENDING))
  
def get_sorted_sale_data(division, list_of_sales):
    division_time = get_division_time(division)

    sorted_sales = []
    for sale in list_of_sales:
        time = sale[division_time]
        sorted_sales[time].append(sale)

    return sorted_sales

def get_division_time(division):
    
