import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps
from ..mongo.pymongoServer import startCollection

collectionName = 'lizCafeteria'

get_all_products_bp = Blueprint('get_all_products', __name__)
@get_all_products_bp.route('/getAllProducts', methods=['GET'])
def get_all_products():
  requestData = json.loads(request.args.to_dict()['query'])
  collection = startCollection(collectionName)
  productCollection = collection['product']

  list_of_products = list(productCollection.find({}))
  for product in list_of_products:
    if '_id' in product:
      product['_id'] = str(product['_id'])

  return jsonify(list_of_products)
