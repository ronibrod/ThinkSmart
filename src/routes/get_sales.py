import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps
from datetime import datetime
from ..mongo.pymongoServer import startCollection

collectionName = 'lizCafeteria'

get_sales_bp = Blueprint('get_sales', __name__)
@get_sales_bp.route('/getSales', methods=['GET'])
def get_sales():
  collection = startCollection(collectionName)
  dayCollection = collection['day']
  productCollection = collection['product']
  salesCollection = collection['sale']

  requestData = json.loads(request.args.to_dict()['query'])

  query = {
    # 'date': {
      # '$lte': datetime.strptime(requestData['startTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
      # '$gte': datetime.strptime(requestData['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
    # },
  }
  
  if 'products' in requestData:
    query['product'] = {'$in': requestData['product']}

  if 'categories' in requestData:
    query['category'] = {'$in': requestData['category']}
    
  print(requestData)
  # list_of_sales = list(salesCollection.find(query))
  list_of_sales = list(salesCollection.find(query))
  for sale in list_of_sales:
    if '_id' in sale:
      sale['_id'] = str(sale['_id'])
  
  print("MongoDB server is connected.")
  print(len(list_of_sales))
  print("MongoDB server is connected.")
  return jsonify(list_of_sales)
