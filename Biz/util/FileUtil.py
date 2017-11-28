#!/usr/bin/python
import xlrd
from model import record


class FileUtil:

    def __init__(self):
        pass

    def load_data_to_db(self, filename):
        data = xlrd.open_workbook(filename)
        table = data.sheet_by_name(u'sheet1')