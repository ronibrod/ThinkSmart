import json
from pymongo import ASCENDING
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
  sorted_sale_data = get_sorted_sale_data(requestData['XAxis'], list_of_sales)
  
  sales_sum_by_time_division = [len(sale) for sale in sorted_sale_data]
  
  print(sales_sum_by_time_division)

  return jsonify(sales_sum_by_time_division)

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

    return list(salesCollection.find(query).sort('date', ASCENDING))
  
def get_sorted_sale_data(division, list_of_sales):
    if division['type'] == 'byPeriod':
        return get_sorted_sale_data_by_period(division)
    # elif division['type'] == 'byCertain':
    #     return get_sorted_sale_data_by_byCertain(division)
    elif division['type'] == 'bySequence':
        return get_sorted_sale_data_by_sequence(division, list_of_sales)
    else:
      return []    

def get_sorted_sale_data_by_period(division, list_of_sales):
    sorted_sales = []
    for sale in list_of_sales:
        time = sale[division['timeDivision']]
        sorted_sales[time].append(sale)

    return sorted_sales

def get_sorted_sale_data_by_sequence(division, list_of_sales):
    time_division = division['timeDivision']
    first_year = list_of_sales[0]['year']  

    sorted_sales = []        
    for sale in list_of_sales:
        year = sale['year']
        month = sale['month'] - 1
        day_of_month = sale['day_of_month'] - 1
        hour = sale['hour']
        
        while len(sorted_sales) <= year - first_year:
            sorted_sales.append([])
        while len(sorted_sales[year - first_year]) <= month:
            sorted_sales[year - first_year].append([])
        while len(sorted_sales[year - first_year][month]) <= day_of_month:
            sorted_sales[year - first_year][month].append([])
        while len(sorted_sales[year - first_year][month][day_of_month]) <= hour:
            sorted_sales[year - first_year][month][day_of_month].append([])

        sorted_sales[year - first_year][month][day_of_month][hour].append(sale)
        
    sorted_sale_data_by_sequence = []
    sorted_sale_data = []
    for year in sorted_sales:
        for month in year:
            for day in month:
                for hour in day:
                    for sale in hour:
                        sorted_sale_data.append(sale)
                    if time_division == 'hourly':
                        sorted_sale_data_by_sequence.append(sorted_sale_data)
                        sorted_sale_data = []
                if time_division == 'daily':
                    sorted_sale_data_by_sequence.append(sorted_sale_data)
                    sorted_sale_data = []
            if time_division == 'monthly':
                sorted_sale_data_by_sequence.append(sorted_sale_data)
                sorted_sale_data = []
        if time_division == 'yearly':
            sorted_sale_data_by_sequence.append(sorted_sale_data)
            sorted_sale_data = []
         
    while sorted_sale_data_by_sequence and len(sorted_sale_data_by_sequence[0]) == 0:
        sorted_sale_data_by_sequence.pop(0)
        
    return sorted_sale_data_by_sequence
    
    # sorted_sale_data_by_sequence = []
    # if time_division == 'yearly':
    #     for year in sorted_sales:
    #         sales_for_year = []
    #         for month in year:
    #             for day in month:
    #                 for hour in day:
    #                     for sale in hour:
    #                         sales_for_year.append(sale)
    #         sorted_sale_data_by_sequence.append(sales_for_year)
            
    # elif time_division == 'monthly':
    #     for year in sorted_sales:
    #         for month in year:
    #             sales_for_month = []
    #             for day in month:
    #                 for hour in day:
    #                     for sale in hour:
    #                         sales_for_month.append(sale)
    #             sorted_sale_data_by_sequence.append(sales_for_month)
                
    # elif time_division == 'weekly':
    #     sales_for_week = []
    #     for year in sorted_sales:
    #         for month in year:
    #             for day in month:
    #                 for hour in day:
    #                     for sale in hour:
    #                         sales_for_week.append(sale)
    #                 if sales_for_week[-1]['day_of_week'] % 7 == 0:
    #                     sorted_sale_data_by_sequence.append(sales_for_week)
    #                     sales_for_week = []
                        
    # elif time_division == 'daily':
    #     for year in sorted_sales:
    #         for month in year:
    #             for day in month:
    #                 sales_for_day = []
    #                 for hour in day:
    #                     for sale in hour:
    #                         sales_for_day.append(sale)
    #                 sorted_sale_data_by_sequence.append(sales_for_day)
                    
    # elif time_division == 'hourly':
    #     for year in sorted_sales:
    #         for month in year:
    #             for day in month:
    #                 for hour in day:
    #                     sales_for_hour = []
    #                     for sale in hour:
    #                         sales_for_hour.append(sale)
    #                     sorted_sale_data_by_sequence.append(sales_for_hour)
                    
    # sorted_sales_by_year = []
    # sorted_sales_by_month = []
    # sorted_sales_by_week = []
    # sorted_sales_by_day = []
    # sorted_sales_by_hour = []
    # sales_for_week = []
  
    # for year in sorted_sales:
    #     sales_for_year = []
    #     for month in year:
    #         sales_for_month = []
    #         for day in month:
    #             sales_for_day = []
    #             for hour in day:
    #                 sorted_sales_by_hour.append(hour)
    #                 for sale in hour:
    #                     sales_for_day.append(sale)
    #                     sales_for_month.append(sale)
    #                     sales_for_year.append(sale)
    #             sorted_sales_by_day.append(sales_for_day)
    #             # if len(sales_for_day):
    #                 # print(sales_for_day)
    #             if len(sales_for_day) and sales_for_day[0]['day_of_week'] % 7 == 1:
    #                 sorted_sales_by_week.append(sales_for_week)
    #                 sales_for_week = []
    #             sales_for_week.append(sales_for_day)
    #         sorted_sales_by_month.append(sales_for_month)
    #     sorted_sales_by_year.append(sales_for_year)

    # if time_division == 'yearly':
    #     return sorted_sales_by_year
    # elif time_division == 'monthly':
    #     return sorted_sales_by_month
    # elif time_division == 'weekly':
    #     return sorted_sales_by_week
    # elif time_division == 'daily':
    #     return sorted_sales_by_day
    # elif time_division == 'hourly':
    #     return sorted_sales_by_hour
    # else:
    #     return []
    
    # if time_division == 'yearly':
    #     return sorted_sales
    # elif time_division == 'monthly':
    #     return [[month_data for month_data in year_data] for year_data in sorted_sales]
    # elif time_division == 'weekly':
    #     return [[[day_data for day_data in month_data] for month_data in year_data] for year_data in sorted_sales]
    # elif time_division == 'daily':
    #     return [[[[hour_data for hour_data in day_data] for day_data in month_data] for month_data in year_data] for year_data in sorted_sales]
    # elif time_division == 'hourly':
    #     return [[[[[sale for sale in hour_data] for hour_data in day_data] for day_data in month_data] for month_data in year_data] for year_data in sorted_sales]
    # else:
    #     return []

    # if time_division == 'year':
    #     return sorted_sales_by_year
      
    # sorted_sales_by_month = []
    # for year_sales in sorted_sales_by_year:
    #     for sale in year_sales:
    #         time = sale['month']
    #         sorted_sales_by_month[time].append(sale)
