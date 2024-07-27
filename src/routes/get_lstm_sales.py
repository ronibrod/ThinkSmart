import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps
from datetime import datetime
from ..neuran.get_LSTM_output_data import get_LSTM_output_data

user_name = 'lizCafeteria'
products = ['Espresso']

get_lstm_sales_bp = Blueprint('get_lstm_sales', __name__)
@get_lstm_sales_bp.route('/getLstmSales', methods=['GET'])
def get_sales():
  requestData = json.loads(request.args.to_dict()['query'])
  # print(requestData)
  
  list_of_sales = get_LSTM_output_data(user_name, requestData)
  # for sale in list_of_sales:
  #   if '_id' in sale:
  #     sale['_id'] = str(sale['_id'])
  
  # print("MongoDB server is connected.")
  # print(list_of_sales)
  # print("MongoDB server is connected.")
  # return jsonify(list_of_sales)
  return jsonify(list_of_sales)
