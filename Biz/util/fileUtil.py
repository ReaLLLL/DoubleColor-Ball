#!/usr/bin/python
import xlrd
from model import record
from pymongo import MongoClient
import json


data = xlrd.open_workbook('/Users/alexsong/Downloads/DCB.xls')
table = data.sheet_by_name(u'sheet1')
client = MongoClient('localhost', 27017)
db = client.get_database('DOUBLECOLOR_BALL')
for i in range(0, table.nrows):
    myrecord=record.Record(table.cell_value(i,0),table.cell_value(i,1),table.cell_value(i,2),table.cell_value(i,3),table.cell_value(i,4),table.cell_value(i,5),table.cell_value(i,6),table.cell_value(i,7),table.cell_value(i,8))
    db.col.insert(json.loads(myrecord.__repr__()))