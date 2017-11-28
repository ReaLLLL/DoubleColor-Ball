#!/usr/bin/python


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
        return '{no: %s, date: %s, red1: %d, red2: %d, red3: %d, red4: %d, red5: %d, red6: %d, blue: %d}' %(self.no, self.date, self.red1, self.red2, self.red3, self.red4, self.red5, self.red6, self.blue)
