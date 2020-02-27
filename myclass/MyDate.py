# -*- coding: utf-8 -*-
"""
MyDate is the subclass of datime.date

datetime.date
https://docs.python.org/3.8/library/datetime.html

"""

from datetime import date

class MyDate(date):
    def __init__(self, year, month, day):
        date.__init__(year, month, day)
        
    def jp_format(self):
        result = str(self.year) + "年"
        if self.month < 10:
            result += "0"
        result += str(self.month) + "月"
        if self.day < 10:
            result += "0"
        result += str(self.day) + "日"
        return result 


#######################
# test
#######################
d = MyDate(1999, 9, 9)
print(d.jp_format()) # 1999年09月09日

