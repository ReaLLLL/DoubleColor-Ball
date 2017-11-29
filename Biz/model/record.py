#!/usr/bin/python
from datetime import datetime
import xlrd

class Record:
    def __init__(self, no, date, red1, red2, red3, red4, red5, red6, blue):
        self.no = no
        self.date = date
        self.red1 = red1
        self.red2 = red2
        self.red3 = red3
        self.red4 = red4
        self.red5 = red5
        self.red6 = red6
        self.blue = blue

    def __repr__(self):
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(self.date, 0)
        date = datetime(year, month, day, hour, minute, second)
        return '{"no": "%s", "weekday": %d, "red1": %d, "red2": %d, "red3": %d, "red4": %d, "red5": %d, "red6": %d, "blue": %d}'%(self.no, date.weekday()+1, self.red1, self.red2, self.red3, self.red4, self.red5, self.red6, self.blue)