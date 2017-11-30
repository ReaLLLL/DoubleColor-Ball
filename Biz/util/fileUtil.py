#!/usr/bin/python
import xlrd
from model import record
from pymongo import MongoClient
import json


def load_data_to_db(file_name, db_name):
    data = xlrd.open_workbook(file_name)
    table = data.sheet_by_name(u'sheet1')
    client = MongoClient('localhost', 27017)
    db = client.get_database(db_name)
    for i in range(0, table.nrows):
        my_record=record.Record(table.cell_value(i,0),table.cell_value(i,1),table.cell_value(i,2),table.cell_value(i,3),table.cell_value(i,4),table.cell_value(i,5),table.cell_value(i,6),table.cell_value(i,7),table.cell_value(i,8))
        db.col.insert(json.loads(my_record.__repr__()))


def get_data_from_db_aggregate(db_name, pipeline):
    client = MongoClient('localhost', 27017)
    db = client.get_database(db_name)
#    result = db.col.aggregate([{'$group' : {'_id' : {'weekday':'$weekday', 'blue':'$blue'},
    # "totalCount" : {'$sum' : 1}}}])
    result = db.col.aggregate(pipeline)
    return list(result)





